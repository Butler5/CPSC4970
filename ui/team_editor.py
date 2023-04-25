import sys

from PyQt6 import uic, QtWidgets

Ui_MainWindow, QtBaseWindow = uic.loadUiType("team_editor.ui")

class TeamEditor(QtBaseWindow, Ui_MainWindow):
    def __init__(self, add=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        if add:
            self.names_text_edit.setPlainText(add.name)

    def update_add(self, add):
        add.name = self.member_text_edit.toPlainText()

    def delete_member_button_clicked(self):
        dialog = QMessageBox(self)
        dialog.setIcon(QMessageBox.Icon.Question)
        dialog.setWindowTitle("Delete member")
        dialog.setText("Are you sure you want to delete this member?")
        no_way_button = dialog.addButton("No!", QMessageBox.ButtonRole.RejectRole)
        yes_button = dialog.addButton("Yes", QMessageBox.ButtonRole.AcceptRole)

        dialog.exec()
        if dialog.clickedButton() == yes_button:
            del self._add[self.address_list_widget.currentRow()]
            self.update_ui()
        else:
            print("Not clicked")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TeamEditor()
    window.show()
    sys.exit(app.exec())
