import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.uic import loadUi

class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        loadUi("untitled.ui", self)

        self.setWindowTitle("Noten Rechner")


#inputs
        self.lineEdit1 = self.findChild(QtWidgets.QLineEdit, "lineEdit1")
        self.lineEdit2 = self.findChild(QtWidgets.QLineEdit, "lineEdit2")
#buttons append, delete and calculate
        self.btn_1 = self.findChild(QtWidgets.QPushButton, "btn_1")
        self.btn_1.clicked.connect(self.getNotesSteh)
        self.btn_2 = self.findChild(QtWidgets.QPushButton, "btn_2")
        self.btn_2.clicked.connect(self.getNotesSch)
        self.btn_3 = self.findChild(QtWidgets.QPushButton, "btn_3")
        self.btn_3.clicked.connect(self.berechnen)
        self.btn_4 = self.findChild(QtWidgets.QPushButton, "btn_4")
        self.btn_4.clicked.connect(self.entfernen)

#label for result or exception
        self.labelNote = self.findChild(QtWidgets.QLabel, "labelNote")
        self.labelEx = self.findChild(QtWidgets.QLabel, "label_4")
        self.labelEx.setHidden(True)
#tablewidget add two culumns
        self.table = self.findChild(QtWidgets.QTableWidget, "tableWidget")
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(('Steh', 'Schriftlich'))
#list for each note
        self.ListSteh = []
        self.ListSch = []
#functions for the note; get from input, set row in table, add to row
    def getNotesSteh(self):
        try:
            NoteSteh = self.lineEdit1.text()
            NoteSteh = int(NoteSteh)
            if NoteSteh > 6:
                self.labelNote.setText("Diese Note existriert nicht")

            else:
                self.ListSteh.append(NoteSteh)
                self.table.setRowCount(max(len(self.ListSteh), len(self.ListSch)))
                self.table.setItem(len(self.ListSteh) - 1, 0, QtWidgets.QTableWidgetItem(str(NoteSteh)))
                self.labelEx.setHidden(True)
        except:
            self.labelEx.setHidden(False)

    def getNotesSch(self):
        try:

            NoteSch = self.lineEdit2.text()
            NoteSch = int(NoteSch)
            if NoteSch > 6:
                self.labelNote.setText("Diese Note existriert nicht")
            else:
                self.ListSch.append(NoteSch)
                self.table.setRowCount(max(len(self.ListSch), len(self.ListSteh)))
                self.table.setItem(len(self.ListSch) - 1, 1, QtWidgets.QTableWidgetItem(str(NoteSch)))
                self.labelEx.setHidden(True)
        except:
            self.labelEx.setHidden(False)
#calculate function
    def berechnen(self):
        try:
            average_steh = sum(self.ListSteh) / len(self.ListSteh)
            average_sch = sum(self.ListSch) / len(self.ListSch)
            final_average = (average_sch * 2 + average_steh)/3
            final_average = round(final_average, 2)
            self.labelNote.setText(str(final_average))
            self.labelNote.setStyleSheet("QLabel {font-size: 20pt;}")

        except:
            self.labelNote.setText("Kein Durchschnitt zu berechen")
            self.labelNote.setStyleSheet("color: red;")
#delete function
    def entfernen(self):
        self.ListSteh.clear()
        self.ListSch.clear()
        self.table.clear()
        self.table.setRowCount(0)
        self.labelNote.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())