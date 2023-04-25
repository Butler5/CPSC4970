import sys
from add import Add
from league_editor import LeagueEditor

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QFileDialog

Ui_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")

class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._add = []
        self.add_button.clicked.connect(self.add_button_clicked)
        self.delete_button.clicked.connect(self.delete_button_clicked)
        self.load_button.clicked.connect(self.load_button_clicked)
        self.save_button.clicked.connect(self.save_button_clicked)

    def warn(self, title, message):
        mb = QMessageBox(QMessageBox.Icon.NoIcon, title, message, QMessageBox.StandardButton.Ok)
        return mb.exec()

    def edit_button_clicked(self):
        row = self.address_list_selected_row()
        print(row)
        if row == -1:
            return self.warn("Select name", "You must select the row to edit")
        add = self._add[row]
        dialog = LeagueEditor(add)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            dialog.update_add(add)
        self.update_ui

    def address_list_selected_row(self):
        selection = self.address_list_widget.selectedItems()
        if len(selection) == 0:
            return -1
        assert len(selection) == 1
        selected_item = selection[0]
        for i, a in enumerate(self._add):
            if str(a) == selected_item.text():
                return a
        return -1

    def load_button_clicked(self):
        dialog = QFileDialog.getOpenFileName(self, "Open File", "", "All Files(*);;Python Files (*.py)")
        if dialog:
            self.label.setText(str(dialog))
        else:
            print("Cancel")

    def save_button_clicked(self):
        dialog = FileMode()
        dialog.exec()

    def add_button_clicked(self):
        a = Add(self.name_line_edit.text())
        self._add.append(a)
        self.update_ui()

    def update_ui(self):
        self.address_list_widget.clear()
        for a in self._add:
            self.address_list_widget.addItem(str(a))

    def delete_button_clicked(self):
        dialog = QMessageBox(self)
        dialog.setIcon(QMessageBox.Icon.Question)
        dialog.setWindowTitle("Delete league name")
        dialog.setText("Are you sure you want to delete this name?")
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
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


