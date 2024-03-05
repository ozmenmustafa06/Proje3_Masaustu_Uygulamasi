import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
                             QMessageBox, QComboBox, QListWidget, QHBoxLayout, QInputDialog)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.language = 'English'  # Default language
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('PyQt5 Multi-function App - English')
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.language_selector = QComboBox()
        self.language_selector.addItems(['English', 'Turkish'])
        self.language_selector.currentTextChanged.connect(self.update_language)
        self.layout.addWidget(self.language_selector)

        self.create_widgets()
        self.show_widgets()

    def create_widgets(self):
        self.password_label = QLabel('Enter your password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.on_login_clicked)
        self.function_menu = QComboBox()
        self.function_menu.addItems(["Select Function", "Inch to CM Converter", "Contact Book"])
        self.function_menu.currentIndexChanged.connect(self.on_function_selected)

    def show_widgets(self):
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.function_menu)
        self.function_menu.setVisible(False)

    def update_language(self, language):
        self.language = language
        if self.language == 'English':
            self.setWindowTitle('PyQt5 Multi-function App - English')
            self.password_label.setText('Enter your password:')
            self.login_button.setText('Login')
            self.function_menu.setItemText(0, "Select Function")
            self.function_menu.setItemText(1, "Inch to CM Converter")
            self.function_menu.setItemText(2, "Contact Book")
        else:
            self.setWindowTitle('PyQt5 Çok Fonksiyonlu Uygulama - Türkçe')
            self.password_label.setText('Şifrenizi girin:')
            self.login_button.setText('Giriş Yap')
            self.function_menu.setItemText(0, "Fonksiyon Seçin")
            self.function_menu.setItemText(1, "İnçten CM'ye Dönüştürücü")
            self.function_menu.setItemText(2, "İletişim Defteri")

    def on_login_clicked(self):
        password = self.password_input.text()
        if password == "secret":
            QMessageBox.information(self, '', 'Login successful!' if self.language == 'English' else 'Giriş başarılı!')
            self.function_menu.setVisible(True)
        else:
            QMessageBox.warning(self, '', 'Incorrect password!' if self.language == 'English' else 'Yanlış şifre!')

    def on_function_selected(self, index):
        if index == 1:
            self.open_converter()
        elif index == 2:
            self.open_contact_book()
        self.function_menu.setCurrentIndex(0)

    def open_converter(self):
        self.converter_window = ConverterWindow(self.language)
        self.converter_window.show()

    def open_contact_book(self):
        self.contact_book_window = ContactBookWindow(self.language)
        self.contact_book_window.show()


class ConverterWindow(QWidget):
    def __init__(self, language):
        super().__init__()
        self.language = language
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Inch-CM Converter" if self.language == 'English' else "İnç-CM Dönüştürücü")
        layout = QVBoxLayout()

        self.value_input = QLineEdit()
        layout.addWidget(QLabel("Enter value:" if self.language == 'English' else "Değer girin:"))
        layout.addWidget(self.value_input)
        
        self.convert_button = QPushButton('Convert' if self.language == 'English' else 'Dönüştür')
        self.convert_button.clicked.connect(self.on_convert_clicked)
        layout.addWidget(self.convert_button)
        
        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def on_convert_clicked(self):
        try:
            value = float(self.value_input.text())
            result = value * 2.54 if self.language == 'English' else value / 2.54
            self.result_label.setText(f"{value} inches is {result:.2f} cm" if self.language == 'English' else f"{value} cm {result:.2f} inçtir")
        except ValueError:
            QMessageBox.warning(self, '', 'Please enter a valid number.' if self.language == 'English' else 'Lütfen geçerli bir sayı girin.')


class ContactBookWindow(QWidget):
    def __init__(self, language):
        super().__init__()
        self.language = language
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Contact Book" if self.language == 'English' else "İletişim Defteri")
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        layout.addWidget(QLabel("Name:" if self.language == 'English' else "İsim:"))
        layout.addWidget(self.name_input)
        
        self.phone_input = QLineEdit()
        layout.addWidget(QLabel("Phone Number:" if self.language == 'English' else "Telefon Numarası:"))
        layout.addWidget(self.phone_input)
        
        self.add_button = QPushButton('Add Contact' if self.language == 'English' else 'Kontak Ekle')
        self.add_button.clicked.connect(self.on_add_clicked)
        layout.addWidget(self.add_button)

        self.contact_list = QListWidget()
        layout.addWidget(self.contact_list)

        self.setLayout(layout)

    def on_add_clicked(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        if name and phone:
            # Here you should add logic to actually store the contacts.
            self.contact_list.addItem(f"{name}: {phone}")
        else:
            QMessageBox.warning(self, '', 'Please enter both name and phone number.' if self.language == 'English' else 'Lütfen hem adı hem de telefon numarasını girin.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec_())
