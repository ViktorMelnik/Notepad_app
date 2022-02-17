# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notes_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 570)
        MainWindow.setMinimumSize(QtCore.QSize(874, 570))
        MainWindow.setMaximumSize(QtCore.QSize(874, 570))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\vikto\\.vscode\\MyWork\\Notes\\image\\notes_icon2.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(200, 200, 200);")
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"border-radius: 10px")
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 800, 530))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(70, 70, 70);\n"
"color: rgb(240, 240, 240);")
        self.plainTextEdit.setLineWidth(1)
        self.plainTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.b_openfile = QtWidgets.QPushButton(self.centralwidget)
        self.b_openfile.setGeometry(QtCore.QRect(820, 10, 48, 48))
        self.b_openfile.setMinimumSize(QtCore.QSize(48, 48))
        self.b_openfile.setMaximumSize(QtCore.QSize(48, 48))
        self.b_openfile.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"border-radius: 12px")
        self.b_openfile.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\vikto\\.vscode\\MyWork\\Notes\\image\\plus_icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.b_openfile.setIcon(icon1)
        self.b_openfile.setIconSize(QtCore.QSize(40, 40))
        self.b_openfile.setObjectName("b_openfile")
        self.b_savefile = QtWidgets.QPushButton(self.centralwidget)
        self.b_savefile.setGeometry(QtCore.QRect(820, 70, 48, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_savefile.sizePolicy().hasHeightForWidth())
        self.b_savefile.setSizePolicy(sizePolicy)
        self.b_savefile.setMinimumSize(QtCore.QSize(48, 48))
        self.b_savefile.setMaximumSize(QtCore.QSize(48, 48))
        self.b_savefile.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"border-radius: 12px")
        self.b_savefile.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\vikto\\.vscode\\MyWork\\Notes\\image\\save_as.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.b_savefile.setIcon(icon2)
        self.b_savefile.setIconSize(QtCore.QSize(40, 40))
        self.b_savefile.setObjectName("b_savefile")
        self.b_print = QtWidgets.QPushButton(self.centralwidget)
        self.b_print.setGeometry(QtCore.QRect(820, 480, 48, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_print.sizePolicy().hasHeightForWidth())
        self.b_print.setSizePolicy(sizePolicy)
        self.b_print.setMinimumSize(QtCore.QSize(48, 48))
        self.b_print.setMaximumSize(QtCore.QSize(48, 48))
        self.b_print.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"border-radius: 12px")
        self.b_print.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\vikto\\.vscode\\MyWork\\Notes\\image\\print.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.b_print.setIcon(icon3)
        self.b_print.setIconSize(QtCore.QSize(40, 40))
        self.b_print.setObjectName("b_print")
        self.b_undo = QtWidgets.QPushButton(self.centralwidget)
        self.b_undo.setGeometry(QtCore.QRect(820, 130, 48, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_undo.sizePolicy().hasHeightForWidth())
        self.b_undo.setSizePolicy(sizePolicy)
        self.b_undo.setMinimumSize(QtCore.QSize(48, 48))
        self.b_undo.setMaximumSize(QtCore.QSize(48, 48))
        self.b_undo.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"border-radius: 12px")
        self.b_undo.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\vikto\\.vscode\\MyWork\\Notes\\image\\undo_icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.b_undo.setIcon(icon4)
        self.b_undo.setIconSize(QtCore.QSize(40, 40))
        self.b_undo.setObjectName("b_undo")
        self.b_copy = QtWidgets.QPushButton(self.centralwidget)
        self.b_copy.setGeometry(QtCore.QRect(820, 190, 48, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_copy.sizePolicy().hasHeightForWidth())
        self.b_copy.setSizePolicy(sizePolicy)
        self.b_copy.setMinimumSize(QtCore.QSize(48, 48))
        self.b_copy.setMaximumSize(QtCore.QSize(48, 48))
        self.b_copy.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"border-radius: 12px")
        self.b_copy.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:\\Users\\vikto\\.vscode\\MyWork\\Notes\\image\\copy1.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.b_copy.setIcon(icon5)
        self.b_copy.setIconSize(QtCore.QSize(40, 40))
        self.b_copy.setObjectName("b_copy")
        self.b_paste = QtWidgets.QPushButton(self.centralwidget)
        self.b_paste.setGeometry(QtCore.QRect(820, 250, 48, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_paste.sizePolicy().hasHeightForWidth())
        self.b_paste.setSizePolicy(sizePolicy)
        self.b_paste.setMinimumSize(QtCore.QSize(48, 48))
        self.b_paste.setMaximumSize(QtCore.QSize(48, 48))
        self.b_paste.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"border-radius: 12px")
        self.b_paste.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:\\Users\\vikto\\.vscode\\MyWork\\Notes\\image\\paste_icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.b_paste.setIcon(icon6)
        self.b_paste.setIconSize(QtCore.QSize(40, 40))
        self.b_paste.setObjectName("b_paste")
        self.b_cut = QtWidgets.QPushButton(self.centralwidget)
        self.b_cut.setGeometry(QtCore.QRect(820, 320, 48, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_cut.sizePolicy().hasHeightForWidth())
        self.b_cut.setSizePolicy(sizePolicy)
        self.b_cut.setMinimumSize(QtCore.QSize(48, 48))
        self.b_cut.setMaximumSize(QtCore.QSize(48, 48))
        self.b_cut.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"border-radius: 12px")
        self.b_cut.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:\\Users\\vikto\\.vscode\\MyWork\\Notes\\image\\cut.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.b_cut.setIcon(icon7)
        self.b_cut.setIconSize(QtCore.QSize(40, 40))
        self.b_cut.setObjectName("b_cut")
        self.b_select_all = QtWidgets.QPushButton(self.centralwidget)
        self.b_select_all.setGeometry(QtCore.QRect(820, 400, 48, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_select_all.sizePolicy().hasHeightForWidth())
        self.b_select_all.setSizePolicy(sizePolicy)
        self.b_select_all.setMinimumSize(QtCore.QSize(48, 48))
        self.b_select_all.setMaximumSize(QtCore.QSize(48, 48))
        self.b_select_all.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"border-radius: 12px")
        self.b_select_all.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("C:\\Users\\vikto\\.vscode\\MyWork\\Notes\\image\\select_icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.b_select_all.setIcon(icon8)
        self.b_select_all.setIconSize(QtCore.QSize(40, 40))
        self.b_select_all.setObjectName("b_select_all")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(78)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setMaximumSize(QtCore.QSize(874, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setToolTipDuration(-6)
        self.menubar.setStyleSheet("background-color: rgb(70, 70, 70);\n"
"color: rgb(240, 240, 240);\n"
"border-radius: 5px;")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionOpen_file.setFont(font)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionSave_file = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionSave_file.setFont(font)
        self.actionSave_file.setObjectName("actionSave_file")
        self.actionSave_file_as = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionSave_file_as.setFont(font)
        self.actionSave_file_as.setObjectName("actionSave_file_as")
        self.actionPrint_file = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionPrint_file.setFont(font)
        self.actionPrint_file.setObjectName("actionPrint_file")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionUndo.setFont(font)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionRedo.setFont(font)
        self.actionRedo.setObjectName("actionRedo")
        self.actionClear = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionClear.setFont(font)
        self.actionClear.setObjectName("actionClear")
        self.actionCut = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionCut.setFont(font)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionCopy.setFont(font)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionPaste.setFont(font)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSelect_all = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionSelect_all.setFont(font)
        self.actionSelect_all.setObjectName("actionSelect_all")
        self.actionWrap_text = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionWrap_text.setFont(font)
        self.actionWrap_text.setObjectName("actionWrap_text")
        self.actionOpen_file_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionOpen_file_2.setFont(font)
        self.actionOpen_file_2.setObjectName("actionOpen_file_2")
        self.actionSave_file_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionSave_file_2.setFont(font)
        self.actionSave_file_2.setObjectName("actionSave_file_2")
        self.actionSave_file_as_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionSave_file_as_2.setFont(font)
        self.actionSave_file_as_2.setObjectName("actionSave_file_as_2")
        self.actionPrint_file_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionPrint_file_2.setFont(font)
        self.actionPrint_file_2.setObjectName("actionPrint_file_2")
        self.actionUndo_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionUndo_2.setFont(font)
        self.actionUndo_2.setObjectName("actionUndo_2")
        self.actionRedo_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionRedo_2.setFont(font)
        self.actionRedo_2.setObjectName("actionRedo_2")
        self.actionClear_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionClear_2.setFont(font)
        self.actionClear_2.setObjectName("actionClear_2")
        self.actionCut_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionCut_2.setFont(font)
        self.actionCut_2.setObjectName("actionCut_2")
        self.actionCopy_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionCopy_2.setFont(font)
        self.actionCopy_2.setObjectName("actionCopy_2")
        self.actionPaste_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionPaste_2.setFont(font)
        self.actionPaste_2.setObjectName("actionPaste_2")
        self.actionSelect_all_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionSelect_all_2.setFont(font)
        self.actionSelect_all_2.setObjectName("actionSelect_all_2")
        self.actionWrap_text_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.actionWrap_text_2.setFont(font)
        self.actionWrap_text_2.setObjectName("actionWrap_text_2")
        self.menuFile.addAction(self.actionOpen_file_2)
        self.menuFile.addAction(self.actionSave_file_2)
        self.menuFile.addAction(self.actionSave_file_as_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint_file_2)
        self.menuEdit.addAction(self.actionUndo_2)
        self.menuEdit.addAction(self.actionRedo_2)
        self.menuEdit.addAction(self.actionClear_2)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut_2)
        self.menuEdit.addAction(self.actionCopy_2)
        self.menuEdit.addAction(self.actionPaste_2)
        self.menuEdit.addAction(self.actionSelect_all_2)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionWrap_text_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.b_cut.pressed.connect(self.plainTextEdit.clear)
        self.b_select_all.pressed.connect(self.plainTextEdit.selectAll)
        self.b_copy.pressed.connect(self.plainTextEdit.copy)
        self.b_undo.pressed.connect(self.plainTextEdit.undo)
        self.b_paste.pressed.connect(self.plainTextEdit.paste)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Notepad"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        self.actionSave_file.setText(_translate("MainWindow", "Save file"))
        self.actionSave_file_as.setText(_translate("MainWindow", "Save file as"))
        self.actionPrint_file.setText(_translate("MainWindow", "Print file"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionSelect_all.setText(_translate("MainWindow", "Select all"))
        self.actionWrap_text.setText(_translate("MainWindow", "Wrap text"))
        self.actionOpen_file_2.setText(_translate("MainWindow", "Open file"))
        self.actionSave_file_2.setText(_translate("MainWindow", "Save file"))
        self.actionSave_file_as_2.setText(_translate("MainWindow", "Save file as"))
        self.actionPrint_file_2.setText(_translate("MainWindow", "Print file"))
        self.actionUndo_2.setText(_translate("MainWindow", "Undo"))
        self.actionRedo_2.setText(_translate("MainWindow", "Set Yellow text"))
        self.actionClear_2.setText(_translate("MainWindow", "Clear"))
        self.actionCut_2.setText(_translate("MainWindow", "Cut"))
        self.actionCopy_2.setText(_translate("MainWindow", "Copy"))
        self.actionPaste_2.setText(_translate("MainWindow", "Paste"))
        self.actionSelect_all_2.setText(_translate("MainWindow", "Select all"))
        self.actionWrap_text_2.setText(_translate("MainWindow", "Wrap text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
