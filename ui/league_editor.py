import sys

from PyQt6 import uic, QtWidgets

Ui_MainWindow, QtBaseWindow = uic.loadUiType("league_editor.ui")

class LeagueEditor(QtBaseWindow, Ui_MainWindow):
    def __init__(self, add=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        if add:
            self.names_text_edit.setPlainText(add.name)

    def update_add(self, add):
        add.name = self.name_text_edit.toPlainText()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LeagueEditor()
    window.show()
    sys.exit(app.exec())

