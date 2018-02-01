#!/usr/bin/env python3
from sys import argv, exit
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_win_Title(object):
    def setupUi(self, win_Title):
        win_Title.setObjectName(_fromUtf8("win_Title"))
        win_Title.resize(419, 420)
        self.verticalLayout_5 = QtGui.QVBoxLayout(win_Title)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushExtinf = QtGui.QPushButton(win_Title)
        self.pushExtinf.setObjectName(_fromUtf8("pushExtinf"))
        self.verticalLayout_3.addWidget(self.pushExtinf)
        self.pushMult = QtGui.QPushButton(win_Title)
        self.pushMult.setObjectName(_fromUtf8("pushMult"))
        self.verticalLayout_3.addWidget(self.pushMult)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.ClickCount = QtGui.QLabel(win_Title)
        self.ClickCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ClickCount.setAlignment(QtCore.Qt.AlignCenter)
        self.ClickCount.setObjectName(_fromUtf8("ClickCount"))
        self.horizontalLayout.addWidget(self.ClickCount)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushBot = QtGui.QPushButton(win_Title)
        self.pushBot.setObjectName(_fromUtf8("pushBot"))
        self.verticalLayout_2.addWidget(self.pushBot)
        self.pushAutom = QtGui.QPushButton(win_Title)
        self.pushAutom.setObjectName(_fromUtf8("pushAutom"))
        self.verticalLayout_2.addWidget(self.pushAutom)
        self.pushDread = QtGui.QPushButton(win_Title)
        self.pushDread.setObjectName(_fromUtf8("pushDread"))
        self.verticalLayout_2.addWidget(self.pushDread)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushRoll = QtGui.QPushButton(win_Title)
        self.pushRoll.setObjectName(_fromUtf8("pushRoll"))
        self.verticalLayout.addWidget(self.pushRoll)
        self.pushPull = QtGui.QPushButton(win_Title)
        self.pushPull.setObjectName(_fromUtf8("pushPull"))
        self.verticalLayout.addWidget(self.pushPull)
        self.pushPry = QtGui.QPushButton(win_Title)
        self.pushPry.setObjectName(_fromUtf8("pushPry"))
        self.verticalLayout.addWidget(self.pushPry)
        self.pushStuff = QtGui.QPushButton(win_Title)
        self.pushStuff.setObjectName(_fromUtf8("pushStuff"))
        self.verticalLayout.addWidget(self.pushStuff)
        self.pushClick = QtGui.QPushButton(win_Title)
        self.pushClick.setObjectName(_fromUtf8("pushClick"))
        self.verticalLayout.addWidget(self.pushClick)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushVote = QtGui.QPushButton(win_Title)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushVote.setFont(font)
        self.pushVote.setObjectName(_fromUtf8("pushVote"))
        self.horizontalLayout_3.addWidget(self.pushVote)
        self.pushQuit = QtGui.QPushButton(win_Title)
        self.pushQuit.setObjectName(_fromUtf8("pushQuit"))
        self.horizontalLayout_3.addWidget(self.pushQuit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi(win_Title)
        QtCore.QMetaObject.connectSlotsByName(win_Title)

    def retranslateUi(self, win_Title):
        win_Title.setWindowTitle(_translate("win_Title", "ClickWarQt4", None))
        self.pushExtinf.setText(_translate("win_Title", "Extra Influence:", None))
        self.pushMult.setText(_translate("win_Title", "Influence Multiplier:", None))
        self.ClickCount.setText(_translate("win_Title", "500", None))
        self.pushAutom.setText(_translate("win_Title", "Vote Automatron:", None))
        self.pushBot.setText(_translate("win_Title", "Vote Bot:", None))
        self.pushDread.setText(_translate("win_Title", "Vote Dreadnought:", None))
        self.pushRoll.setText(_translate("win_Title", "Roll Some Clicks Your Way:", None))
        self.pushPull.setText(_translate("win_Title", "Pull Some Clicks To You:", None))
        self.pushPry.setText(_translate("win_Title", "Pry Some Clicks Up:", None))
        self.pushStuff.setText(_translate("win_Title", "Stuff Some Extra Clicks In There:", None))
        self.pushClick.setText(_translate("win_Title", "Click The Old Fashioned Way:", None))
        self.pushVote.setText(_translate("win_Title", "Vote!", None))
        self.pushQuit.setText(_translate("win_Title", "Quit", None))
    
class Gear(Ui_win_Title):
    def __init__(self, name, description, tip, cost, quantity=0, per_second=0, limit=0):
        self.name = name
        self.description = description
        self.tip = tip
        self.cost = cost
        self.quantity = quantity
        self.per_second = per_second
        self.limit = limit

class Clicker(Ui_win_Title):
    # def __init__(self):
    def __init__(self, parent):
        self.parent = parent
        self.current_clicks = 500
        self.gear = dict()
        self.gear_assign()
        self.gear_init()

    def gear_assign(self):
        self.gear['influence'] = Gear('influence', 'Extra Influence: ',
                                      'Increases number of votes per click.', 10, quantity=1, limit=100)
        self.gear['bot'] = Gear('bot', 'Vote Bot: ',
                                'Have a bot vote for you; has its own influence.',  15, 0, per_second=1)
        self.gear['automatron'] = Gear('automatron', 'Vote Automatron: ',
                                       'More powerful bots for smashing that vote button.', 50, per_second=5)
        self.gear['dreadnought'] = Gear('dreadnought', 'Vote Dreadnought: ',
                                        'Beastly bot for annihilating that vote button.', 100, per_second=20)
        self.gear['multiplier'] = Gear('multiplier', 'Influence Multiplier: ',
                                       'Doubles influence.', 50, limit=5)
        self.gear['inclined plane'] = Gear('inclined plane', 'Roll Some Clicks Your Way: ',
                                           'Observe clicks in slow motion.',  500, per_second=125)
        self.gear['pulley'] = Gear('pulley', 'Pull Some Clicks To You: ',
                                   'Not frictionless.', 2000, per_second=750)
        self.gear['lever'] = Gear('lever', 'Pry Some Clicks Up: ',
                                  'Archimedes would be proud.',  10000, per_second=5000)
        self.gear['wedge'] = Gear('wedge', 'Stuff Some Extra Clicks In There: ',
                                  'Can I axe you a question?', 100000, per_second=75000)
        self.gear['elbow greese'] = Gear('elbow greese', 'Click the Old Fashioned Way: ',
                                         'Easy.', 500000, per_second=500000)
    
    def increment(self):
        self.current_clicks += click.gear['influence'].quantity * 2**click.gear['multiplier'].quantity
        ui.ClickCount.setText(_translate("win_Title", "%d" % self.current_clicks, None))
    
    def gear_init(self, buttonName, gearName):
        for gear in self.gear.values():
            gear.button = ui.Button(parent, text=gear.description % self.gear[gear.name].cost, 
            command=lambda x=gear.name: self.purchase(x))
    
    def update_extra_inf(self):
        ui.pushExtinf.setText(_translate("win_Title", "%s(%d): %d" % 
        (click.gear['influence'].description, click.gear['influence'].cost, 
        click.gear['influence'].quantity), None))

    def update_multi(self):
        ui.pushMult.setText(_translate("win_Title", "%s(%d): %d" % 
        (click.gear['multiplier'].description, click.gear['multiplier'].cost, 
        click.gear['multiplier'].quantity), None))
    
    def update_bot(self):
        ui.pushBot.setText(_translate("win_Title", "%s(%d): %d" % 
        (click.gear['bot'].description, click.gear['bot'].cost, 
        click.gear['bot'].quantity), None))
    
    def update_autom(self):
        ui.pushAutom.setText(_translate("win_Title", "%s(%d): %d" % 
        (click.gear['automatron'].description, click.gear['automatron'].cost, 
        click.gear['automatron'].quantity), None))
    
    def update_dread(self):
        ui.pushDread.setText(_translate("win_Title", "%s(%d): %d" % 
        (click.gear['dreadnought'].description, click.gear['dreadnought'].cost, 
        click.gear['dreadnought'].quantity), None))
    
    def update_roll(self):
        ui.pushRoll.setText(_translate("win_Title", "%s(%d): %d" % 
        (click.gear['inclined plane'].description, click.gear['inclined plane'].cost, 
        click.gear['inclined plane'].quantity), None))
    
    def update_pull(self):
        ui.pushPull.setText(_translate("win_Title", "%s(%d): %d" % 
        (click.gear['pulley'].description, click.gear['pulley'].cost, 
        click.gear['pulley'].quantity), None))
    
    def update_pry(self):
        ui.pushPry.setText(_translate("win_Title", "%s(%d): %d" % 
        (click.gear['lever'].description, click.gear['lever'].cost, 
        click.gear['lever'].quantity), None))
    
    def update_stuff(self):
        ui.pushStuff.setText(_translate("win_Title", "%s(%d): %d" % 
        (click.gear['wedge'].description, click.gear['wedge'].cost, 
        click.gear['wedge'].quantity), None))

    def update_click(self):
        ui.pushClick.setText(_translate("win_Title", "%s(%d): %d" % 
        (click.gear['elbow greese'].description, click.gear['elbow greese'].cost, 
        click.gear['elbow greese'].quantity), None))
    
if __name__ == "__main__":
    app = QtGui.QApplication(argv)
    win_Title = QtGui.QDialog()
    ui = Ui_win_Title()
    ui.setupUi(win_Title)
    click = Clicker(Gear)

    # ui.pushVote.clicked.connect(ui.blah) - link function to do thang
    ui.pushQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)
    ui.pushVote.clicked.connect(click.increment)
    # ui.pushExtinf.clicked.connect(click.update_extra_inf)
    ui.pushExtinf.clicked.connect(click.gear_init('pushExtinf', 'multiplier'))
    ui.pushMult.clicked.connect(click.update_multi)
    ui.pushAutom.clicked.connect(click.update_autom)
    ui.pushBot.clicked.connect(click.update_bot)
    ui.pushDread.clicked.connect(click.update_dread)
    ui.pushRoll.clicked.connect(click.update_roll)
    ui.pushPull.clicked.connect(click.update_pull)
    ui.pushPry.clicked.connect(click.update_pry)
    ui.pushStuff.clicked.connect(click.update_stuff)
    ui.pushClick.clicked.connect(click.update_click)
    
    win_Title.show()
    exit(app.exec_())
