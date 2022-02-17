import notes_design
from notes_design import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore              
from PyQt5.QtGui import QFontDatabase, QIcon, QKeySequence
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtWidgets import QMessageBox, QAction


class Note_app(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self._connectActions()
        
        self.b_openfile.pressed.connect(self.file_open)
        self.b_savefile.pressed.connect(self.file_save_as)
        self.b_print.pressed.connect(self.file_print)
        
    def _connectActions(self):
        self.actionOpen_file_2.triggered.connect(self.file_open)
        self.actionSave_file_as_2.triggered.connect(self.file_save_as)
        self.actionPrint_file_2.triggered.connect(self.file_print)
        self.actionSave_file_2.triggered.connect(self.file_save)
        self.actionRedo_2.triggered.connect(self.file_set_yellow)
        
        self.actionUndo_2.triggered.connect(self.plainTextEdit.undo)
        self.actionCut_2.triggered.connect(self.plainTextEdit.clear)
        self.actionSelect_all_2.triggered.connect(self.plainTextEdit.selectAll)
        self.actionCopy_2.triggered.connect(self.plainTextEdit.copy)
        self.actionPaste_2.triggered.connect(self.plainTextEdit.paste)
        
    def file_set_yellow(self):
        self.plainTextEdit.setStyleSheet("background-color: rgb(70, 70, 70);\n" "color: rgb(250, 250, 0);")

    def file_open(self):
        file = QtWidgets.QFileDialog.getOpenFileName(parent=note_app, 
                                                     filter='Text Document (*.txt)', 
                                                     caption='Open file')
        try:
            o = open(file[0])
            r = o.read()
            self.plainTextEdit.appendPlainText(r)
        except:
            return
        
    def file_save_as(self):
        file = QtWidgets.QFileDialog.getSaveFileName(parent=note_app, 
                                                     filter='Text Document (*.txt)', 
                                                     caption='Save file')
        try:
            with open(file[0], 'w') as file_write:
                text = self.plainTextEdit.toPlainText()
                text = str(text)
                file_write.write(text)
                file_write.close()
        except:
            return
        
    def file_save(self):
        file = QtWidgets.QFileDialog.getSaveFileName(parent=note_app, 
                                                     filter='Text Document (*.txt)', directory='C:\\Users\\vikto\\Documents',
                                                     caption='Save file in C:\\Users\\vikto\\Documents')
        try:
            with open(file[0], 'w') as file_write:
                text = self.plainTextEdit.toPlainText()
                text = str(text)
                file_write.write(text)
                file_write.close()
        except:
            return
        
        
    def file_print(self):
        try:
            self.plainTextEdit.print()
        except:
            error = QMessageBox()
            error.setWindowTitle('Print error')
            error.setText('Install printer')
            error.setIcon(QMessageBox.Warning)
            error.setInformativeText('QPrinter::Selection as print range')
            error.setDetailedText('QPagedPaintDevice::A4	0	210 x 297 мм, 8.26 x 11,69 дюйм')
            error.exec_()
                      

app = QApplication(sys.argv)
note_app = Note_app()
note_app.show()
sys.exit(app.exec_())


