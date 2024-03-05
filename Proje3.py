import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QComboBox, QListWidget, QHBoxLayout, QInputDialog

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('PyQt5 Multi-function App')
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.password_label = QLabel('Enter your password:')
        layout.addWidget(self.password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)
        
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.on_login_clicked)
        layout.addWidget(self.login_button)

        self.function_menu = QComboBox()
        self.function_menu.addItem("Select Function")
        self.function_menu.addItem("Inch to CM Converter")
        self.function_menu.addItem("Contact Book")
        self.function_menu.currentIndexChanged.connect(self.on_function_selected)
        layout.addWidget(self.function_menu)
        self.function_menu.setVisible(False)

    def on_login_clicked(self):
        if self.password_input.text() == "secret":
            QMessageBox.information(self, 'Login Successful', 'You have successfully logged in.')
            self.function_menu.setVisible(True)
        else:
            QMessageBox.warning(self, 'Login Failed', 'The password you entered is incorrect.')

    def on_function_selected(self, index):
        if index == 1:
            self.open_converter()
        elif index == 2:
            self.open_contact_book()
        self.function_menu.setCurrentIndex(0)

    def open_converter(self):
        self.converter_window = ConverterWindow()
        self.converter_window.show()

    def open_contact_book(self):
        self.contact_book_window = ContactBookWindow()
        self.contact_book_window.show()


class ConverterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Inch-CM Converter")
        layout = QVBoxLayout()
        
        self.converter_type = QComboBox()
        self.converter_type.addItem("Inch to CM")
        self.converter_type.addItem("CM to Inch")
        layout.addWidget(self.converter_type)
        
        self.value_input = QLineEdit()
        layout.addWidget(QLabel("Enter value:"))
        layout.addWidget(self.value_input)
        
        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.on_convert_clicked)
        layout.addWidget(self.convert_button)
        
        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def on_convert_clicked(self):
        try:
            value = float(self.value_input.text())
            if self.converter_type.currentText() == "Inch to CM":
                result = value * 2.54
                self.result_label.setText(f"{value} inches is {result:.2f} cm")
            else:
                result = value / 2.54
                self.result_label.setText(f"{value} cm is {result:.2f} inches")
        except ValueError:
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid number.')


class ContactBookWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Contact Book")
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        input_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        
        self.name_input = QLineEdit()
        input_layout.addWidget(QLabel("Name:"))
        input_layout.addWidget(self.name_input)
        
        self.phone_input = QLineEdit()
        input_layout.addWidget(QLabel("Phone Number:"))
        input_layout.addWidget(self.phone_input)
        
        self.add_button = QPushButton('Add Contact')
        self.add_button.clicked.connect(self.on_add_clicked)
        input_layout.addWidget(self.add_button)

        self.contact_list = QListWidget()
        self.contact_list.setSelectionMode(QListWidget.MultiSelection)
        main_layout.addWidget(self.contact_list)

        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        self.edit_button = QPushButton('Edit Selected Contact')
        self.edit_button.clicked.connect(self.on_edit_clicked)
        button_layout.addWidget(self.edit_button)

        self.delete_button = QPushButton('Delete Selected Contacts')
        self.delete_button.clicked.connect(self.on_delete_clicked)
        button_layout.addWidget(self.delete_button)

        self.delete_all_button = QPushButton('Delete All Contacts')
        self.delete_all_button.clicked.connect(self.on_delete_all_clicked)
        button_layout.addWidget(self.delete_all_button)

        self.load_contacts()

    def load_contacts(self):
        self.contact_list.clear()
        try:
            with open('rehber_listesi.txt', 'r') as file:
                for line in file:
                    self.contact_list.addItem(line.strip())
        except FileNotFoundError:
            open('rehber_listesi.txt', 'w').close()

    def on_add_clicked(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        new_contact = f"{name}: {phone}"
        if name and phone:
            with open('rehber_listesi.txt', 'a') as file:
                file.write(new_contact + "\n")
            self.load_contacts()
            self.name_input.clear()
            self.phone_input.clear()
        else:
            QMessageBox.warning(self, 'Invalid Input', 'Please enter both name and phone number.')

    def on_edit_clicked(self):
        selected_items = self.contact_list.selectedItems()
        if len(selected_items) == 1:
            selected_item = selected_items[0]
            new_name, ok1 = QInputDialog.getText(self, 'Edit Contact', 'Enter new name:', QLineEdit.Normal, selected_item.text().split(":")[0])
            new_phone, ok2 = QInputDialog.getText(self, 'Edit Contact', 'Enter new phone number:', QLineEdit.Normal, selected_item.text().split(":")[1].strip())
            if ok1 and ok2 and new_name and new_phone:
                current_contacts = [self.contact_list.item(i).text() for i in range(self.contact_list.count())]
                current_contacts[current_contacts.index(selected_item.text())] = f"{new_name}: {new_phone}"
                with open('rehber_listesi.txt', 'w') as file:
                    for contact in current_contacts:
                        file.write(contact + "\n")
                self.load_contacts()
        else:
            QMessageBox.warning(self, 'Selection Error', 'Please select a single contact to edit.')

    def on_delete_clicked(self):
        selected_items = self.contact_list.selectedItems()
        if selected_items:
            current_contacts = [self.contact_list.item(i).text() for i in range(self.contact_list.count())]
            for item in selected_items:
                current_contacts.remove(item.text())
            with open('rehber_listesi.txt', 'w') as file:
                for contact in current_contacts:
                    file.write(contact + "\n")
            self.load_contacts()
        else:
            QMessageBox.warning(self, 'No Selection', 'Please select at least one contact to delete.')

    def on_delete_all_clicked(self):
        confirm = QMessageBox.question(self, 'Delete All', 'Are you sure you want to delete all contacts?', QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            open('rehber_listesi.txt', 'w').close()
            self.load_contacts()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec_())
