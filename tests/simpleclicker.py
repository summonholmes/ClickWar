# Copied from tutorial on youtube by TigerHawkT3
import tkinter as tk
from idlelib.tooltip import ToolTip as Tip


class Gear:
    def __init__(self, name, cost, quantity=0, per_second=0, limit=0):
        self.name = name
        self.cost = cost
        self.quantity = quantity
        self.per_second = per_second
        self.limit = limit  # I think having an 'appreciation' value that determines how much the cost increases per purchase would be better.


class Clicker:
    def __init__(self, parent):
        self.parent = parent
        self.purchase_buttons = dict()
        self.the_button = tk.Button(parent, text="Vote!", width=20, height=5, command=self.increment)
        self.current_clicks = 500  # set to 500 for fast testing. Needs to be set to 0
        self.gear = dict()
        self.building = dict()

        self.gear['influence'] = Gear('influence', 10, quantity=1, limit=100)
        self.gear['bot'] = Gear('bot', 15, 0, per_second=1)
        self.gear['automatron'] = Gear('automatron', 50, per_second=5)
        self.gear['multiplier'] = Gear('multiplier', 50, limit=5)

        self.purchase_buttons['influence'] = tk.Button(parent, text='Extra influence: (%d): 1' % self.gear['influence'].cost,
                                                       command=lambda: self.purchase('influence'))
        self.purchase_buttons['bot'] = tk.Button(parent, text='Vote bot: (%d): 0' % self.gear['bot'].cost,
                                                 command=lambda: self.purchase('bot'))
        self.purchase_buttons['multiplier'] = tk.Button(parent, text='Influence multiplier: (%d): 0' % self.gear[
                                                        'multiplier'].cost, command=lambda: self.purchase('multiplier'))
        self.purchase_buttons['automatron'] = tk.Button(parent, text='Vote automatron: (%d): 0' % self.gear['automatron'].cost,
                                                        command=lambda: self.purchase('automatron'))

        self.tooltips = {'influence': Tip(self.purchase_buttons['influence'], 'Increases number of votes per click.'),
                         'bot': Tip(self.purchase_buttons['bot'], 'Have a bot vote for you; has its own influence.'),
                         'automatron': Tip(self.purchase_buttons['automatron'], 'More powerful bots for smashing that vote button.'),
                         'multiplier': Tip(self.purchase_buttons['multiplier'], 'Doubles influence.')
                         }
        self.current_click_label = tk.Label(parent, text='0')
        self.the_button.grid(row=0, column=0)
        self.current_click_label.grid(row=0, column=1, columnspan=2)
        manual_row = 0
        auto_row = 0
        for name in sorted(self.gear, key=lambda x: self.gear[x].cost):
            if self.gear[name].per_second:
                manual_row += 1
                row = manual_row
                column = 2
            else:
                auto_row += 1
                row = auto_row
                column = 1
            self.purchase_buttons[name].grid(row=row, column=column)

        self.update()  # inherits 'update' method from tk.Tk()

    def increment(self):
        self.current_clicks += self.gear['influence'].quantity * 2**self.gear['multiplier'].quantity
        self.current_click_label.config(text='%d' % self.current_clicks)

    def purchase(self, name):
        if self.current_clicks >= self.gear[name].cost:
            self.gear[name].quantity += 1
            self.current_clicks -= self.gear[name].cost
            self.current_click_label.config(text='%d' % self.current_clicks)
            self.purchase_buttons[name].config(text=self.purchase_buttons[name]['text'].split(':')[0] +
                                               ': ({:.1f}): {}'.format(self.gear[name].cost, self.gear[name].quantity))
            self.gear[name].cost *= 1.1  # Make the next purchase 10% higher after purchasing (this should be a baseline that should be altered based on the power of what you're purchasing.)
            if self.gear[name].limit and self.gear[name].quantity >= self.gear[name].limit:
                self.purchase_buttons[name].config(state=tk.DISABLED)
                self.purchase_buttons[name].config(text=self.purchase_buttons[name]['text'].split(':')[0] +
                                                   ': (Limit reached!): {}'.format(self.gear[name].quantity))

    def update(self):
        for gear in self.gear.values():
            self.current_clicks += gear.per_second * gear.quantity
        self.current_click_label.config(text='%d' % self.current_clicks)
        self.parent.after(1000, self.update)  # 1000 ms and then schedule the next update (not recursive)

root = tk.Tk()
clicker = Clicker(root)
root.mainloop()
