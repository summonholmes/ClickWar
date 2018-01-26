#!/usr/bin/env python3
from sys import argv, exit
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_win_Title(object):
    def setupUi(self, win_Title):
        win_Title.setObjectName("win_Title")
        win_Title.resize(419, 419)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(win_Title)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushExtinf = QtWidgets.QPushButton(win_Title)
        self.pushExtinf.setObjectName("pushExtinf")
        self.verticalLayout_3.addWidget(self.pushExtinf)
        self.pushMult = QtWidgets.QPushButton(win_Title)
        self.pushMult.setObjectName("pushMult")
        self.verticalLayout_3.addWidget(self.pushMult)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.ClickCount = QtWidgets.QLabel(win_Title)
        self.ClickCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ClickCount.setAlignment(QtCore.Qt.AlignCenter)
        self.ClickCount.setObjectName("ClickCount")
        self.horizontalLayout.addWidget(self.ClickCount)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushAutom = QtWidgets.QPushButton(win_Title)
        self.pushAutom.setObjectName("pushAutom")
        self.verticalLayout_2.addWidget(self.pushAutom)
        self.pushBot = QtWidgets.QPushButton(win_Title)
        self.pushBot.setObjectName("pushBot")
        self.verticalLayout_2.addWidget(self.pushBot)
        self.pushDread = QtWidgets.QPushButton(win_Title)
        self.pushDread.setObjectName("pushDread")
        self.verticalLayout_2.addWidget(self.pushDread)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushRoll = QtWidgets.QPushButton(win_Title)
        self.pushRoll.setObjectName("pushRoll")
        self.verticalLayout.addWidget(self.pushRoll)
        self.pushPull = QtWidgets.QPushButton(win_Title)
        self.pushPull.setObjectName("pushPull")
        self.verticalLayout.addWidget(self.pushPull)
        self.pushPry = QtWidgets.QPushButton(win_Title)
        self.pushPry.setObjectName("pushPry")
        self.verticalLayout.addWidget(self.pushPry)
        self.pushStuff = QtWidgets.QPushButton(win_Title)
        self.pushStuff.setObjectName("pushStuff")
        self.verticalLayout.addWidget(self.pushStuff)
        self.pushClick = QtWidgets.QPushButton(win_Title)
        self.pushClick.setObjectName("pushClick")
        self.verticalLayout.addWidget(self.pushClick)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushVote = QtWidgets.QPushButton(win_Title)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushVote.setFont(font)
        self.pushVote.setObjectName("pushVote")
        self.horizontalLayout_3.addWidget(self.pushVote)
        self.pushQuit = QtWidgets.QPushButton(win_Title)
        self.pushQuit.setObjectName("pushQuit")
        self.horizontalLayout_3.addWidget(self.pushQuit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi(win_Title)
        QtCore.QMetaObject.connectSlotsByName(win_Title)

    def retranslateUi(self, win_Title):
        clickVal = 500

        _translate = QtCore.QCoreApplication.translate
        win_Title.setWindowTitle(_translate("win_Title", "ClickWarQt5"))
        self.pushExtinf.setText(_translate("win_Title", "Extra Influence:"))
        self.pushMult.setText(_translate("win_Title", "Influence Multiplier:"))
        self.ClickCount.setText(_translate("win_Title", "%d" % clickVal))
        self.pushAutom.setText(_translate("win_Title", "Vote Automatron:"))
        self.pushBot.setText(_translate("win_Title", "Vote Bot:"))
        self.pushDread.setText(_translate("win_Title", "Vote Dreadnought:"))
        self.pushRoll.setText(_translate("win_Title", "Roll Some Clicks Your Way:"))
        self.pushPull.setText(_translate("win_Title", "Pull Some Clicks To You:"))
        self.pushPry.setText(_translate("win_Title", "Pry Some Clicks Up:"))
        self.pushStuff.setText(_translate("win_Title", "Stuff Some Extra Clicks In There:"))
        self.pushClick.setText(_translate("win_Title", "Click The Old Fashioned Way:"))
        self.pushVote.setText(_translate("win_Title", "Vote!"))
        self.pushQuit.setText(_translate("win_Title", "Quit"))

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
    def __init__(self):
    # def __init__(self, parent):
        # self.parent = parent
        self.current_clicks = 500
        self.gear = dict()
        self.gear_init()

    def gear_init(self):
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

    def increment(self):
        self.current_clicks += self.gear['influence'].quantity * 2**self.gear['multiplier'].quantity


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    win_Title = QtWidgets.QDialog()
    ui = Ui_win_Title()
    ui.setupUi(win_Title)
    click = Clicker(Gear)

    # ui.pushVote.clicked.connect(ui.blah) - link function to do thang
    ui.pushQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)
    ui.pushVote.clicked.connect(click.increment)

    win_Title.show()
    exit(app.exec_())
