# Copied from tutorial on youtube by TigerHawkT3
import tkinter as tk
from idlelib.ToolTip import ToolTip as Tip


class Gear:
    def __init__(self, name, description, tip, cost, quantity=0, per_second=0, limit=0):
        self.name = name
        self.description = description
        self.tip = tip
        self.cost = cost
        self.quantity = quantity
        self.per_second = per_second
        self.limit = limit  # I think having an 'appreciation' value that determines how much the cost increases per purchase would be better.


class Clicker:
    def __init__(self, parent):
        self.parent = parent
        self.the_button = tk.Button(parent, text="Vote!", width=20, height=5, command=self.increment)
        self.current_clicks = 500  # set to 500 for fast testing. Needs to be set to 0
        self.gear = dict()
        self.building = dict()
        self.tooltips = dict()

        self.gear['influence'] = Gear('influence', 'Extra influence: (%d): 1',
                                      'Increases number of votes per click.', 10, quantity=1, limit=100)
        self.gear['bot'] = Gear('bot', 'Vote bot: (%d): 0',
                                'Have a bot vote for you; has its own influence.',  15, 0, per_second=1)
        self.gear['automatron'] = Gear('automatron', 'Vote automatron: (%d): 0',
                                       'More powerful bots for smashing that vote button.', 50, per_second=5)
        self.gear['dreadnought'] = Gear('dreadnought', 'Vote dreadnought: (%d): 0',
                                        'Beastly bot for annihilating that vote button.', 100, per_second=20)
        self.gear['multiplier'] = Gear('multiplier', 'Influence multiplier: (%d): 0',
                                       'Doubles influence.', 50, limit=5)
        self.gear['inclined plane'] = Gear('inclined plane', 'Roll some clicks your way: (%d): 0',
                                           'Observe clicks in slow motion.',  500, per_second=125)
        self.gear['pulley'] = Gear('pulley', 'Pull some clicks to you: (%d): 0',
                                   'Not frictionless.', 2000, per_second=750)
        self.gear['lever'] = Gear('lever', 'Pry some clicks up: (%d): 0',
                                  'Archimedes would be proud.',  10000, per_second=5000)
        self.gear['wedge'] = Gear('wedge', 'Stuff some extra clicks in there: (%d): 0',
                                  'Can I axe you a question?', 100000, per_second=75000)
        self.gear['elbow greese'] = Gear('elbow greese', 'Click the old-fashioned way: (%d): 0',
                                         'Easy.', 500000, per_second=500000)

        for gear in self.gear.values():
            gear.button = tk.Button(parent, text=gear.description % self.gear[gear.name].cost,
                                    command=lambda x=gear.name: self.purchase(x))  # (x=name) - avoid returning most current updated name instead of current item in the loop.
            gear.tooltip = Tip(gear.button, gear.tip)  # tooltip is object, tip is the text.

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
            self.gear[name].button.grid(row=row, column=column)

        self.update()  # inherits 'update' method from tk.Tk()

    def increment(self):
        self.current_clicks += self.gear['influence'].quantity * 2**self.gear['multiplier'].quantity
        self.current_click_label.config(text='%d' % self.current_clicks)

    def purchase(self, name):
        if self.current_clicks >= self.gear[name].cost:
            self.gear[name].quantity += 1
            self.current_clicks -= self.gear[name].cost
            self.current_click_label.config(text='%d' % self.current_clicks)
            self.gear[name].button.config(text=self.gear[name].button['text'].split(':')[0] +
                                          ': ({:.1f}): {}'.format(self.gear[name].cost, self.gear[name].quantity))
            self.gear[name].cost *= 1.1  # 10% cost increase after purchasing (should be a baseline and altered based on power.)
            if self.gear[name].limit and self.gear[name].quantity >= self.gear[name].limit:
                self.gear[name].button.config(state=tk.DISABLED)
                self.gear[name].button.config(text=self.gear[name].button['text'].split(':')[0] +
                                              ': (Limit reached!): {}'.format(self.gear[name].quantity))

    def update(self):
        for gear in self.gear.values():
            self.current_clicks += gear.per_second * gear.quantity
        self.current_click_label.config(text='%d' % self.current_clicks)
        self.parent.after(1000, self.update)  # 1000 ms and then schedule the next update (not recursive)

root = tk.Tk()
clicker = Clicker(root)
root.mainloop()
