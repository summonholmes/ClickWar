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
        win_Title.resize(419, 419)
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
        self.pushAutom = QtGui.QPushButton(win_Title)
        self.pushAutom.setObjectName(_fromUtf8("pushAutom"))
        self.verticalLayout_2.addWidget(self.pushAutom)
        self.pushBot = QtGui.QPushButton(win_Title)
        self.pushBot.setObjectName(_fromUtf8("pushBot"))
        self.verticalLayout_2.addWidget(self.pushBot)
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
        clickVal = 500

        win_Title.setWindowTitle(_translate("win_Title", "ClickWarQt4", None))
        self.pushExtinf.setText(_translate("win_Title", "Extra Influence:", None))
        self.pushMult.setText(_translate("win_Title", "Influence Multiplier:", None))
        self.ClickCount.setText(_translate("win_Title", "%d" % clickVal, None))
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

if __name__ == "__main__":
    app = QtGui.QApplication(argv)
    win_Title = QtGui.QDialog()
    ui = Ui_win_Title()
    ui.setupUi(win_Title)

    # ui.pushVote.clicked.connect(ui.blah) - link function to do thang
    ui.pushQuit.clicked.connect(QtCore.QCoreApplication.instance().quit)

    win_Title.show()
    exit(app.exec_())