import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
                             QMessageBox, QComboBox, QListWidget, QHBoxLayout, QInputDialog)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.language = 'Turkish'  # Default language set to Turkish
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('PyQt5 Çok Fonksiyonlu Uygulama - Türkçe')
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.language_selector = QComboBox()
        self.language_selector.addItems(['Türkçe', 'English'])  # 'Türkçe' is listed first as it is the default language
        self.language_selector.currentTextChanged.connect(self.update_language)
        self.layout.addWidget(self.language_selector)

        self.create_widgets()
        self.show_widgets()

    def create_widgets(self):
        self.password_label = QLabel('Şifrenizi girin:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Giriş Yap')
        self.login_button.clicked.connect(self.on_login_clicked)
        self.function_menu = QComboBox()
        self.function_menu.addItems(["Fonksiyon Seçin", "Çeviri Uygulaması", "Rehber Uygulaması"])
        self.function_menu.currentIndexChanged.connect(self.on_function_selected)

    def show_widgets(self):
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.function_menu)
        self.function_menu.setVisible(False)

    def update_language(self, language):
        self.language = 'English' if language == 'English' else 'Turkish'
        if self.language == 'English':
            self.setWindowTitle('PyQt5 Multi-function App - English')
            self.password_label.setText('Enter your password:')
            self.login_button.setText('Login')
            self.function_menu.setItemText(0, "Select Function")
            self.function_menu.setItemText(1, "Translation Application")
            self.function_menu.setItemText(2, "Contact Application")
        else:
            self.setWindowTitle('PyQt5 Çok Fonksiyonlu Uygulama - Türkçe')
            self.password_label.setText('Şifrenizi girin:')
            self.login_button.setText('Giriş Yap')
            self.function_menu.setItemText(0, "Fonksiyon Seçin")
            self.function_menu.setItemText(1, "Çeviri Uygulaması")
            self.function_menu.setItemText(2, "Rehber Uygulaması")

    def on_login_clicked(self):
        password = self.password_input.text()
        if password == "secret":
            QMessageBox.information(self, '', 'Login successful!' if self.language == 'English' else 'Giriş başarılı!')
            self.function_menu.setVisible(True)
        else:
            QMessageBox.warning(self, '', 'Incorrect password!' if self.language == 'English' else 'Yanlış şifre!')

    def on_function_selected(self, index):
        if index == 1:
            self.open_translation_application()
        elif index == 2:
            self.open_contact_application()
        self.function_menu.setCurrentIndex(0)

    def open_translation_application(self):
        self.translation_application_window = TranslationApplicationWindow(self.language)
        self.translation_application_window.show()

    def open_contact_application(self):
        self.contact_application_window = ContactApplicationWindow(self.language)
        self.contact_application_window.show()


class TranslationApplicationWindow(QWidget):
    def __init__(self, language):
        super().__init__()
        self.language = language
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Çeviri Uygulaması" if self.language == 'Turkish' else "Translation Application")
        layout = QVBoxLayout()

        self.converter_type = QComboBox()
        self.converter_type.addItem("İnçten CM'ye" if self.language == 'Turkish' else "Inch to CM")
        self.converter_type.addItem("CM'den İnçe" if self.language == 'Turkish' else "CM to Inch")
        layout.addWidget(self.converter_type)

        self.value_input = QLineEdit()
        layout.addWidget(QLabel("Değer girin:" if self.language == 'Turkish' else "Enter value:"))
        layout.addWidget(self.value_input)
        
        self.convert_button = QPushButton('Dönüştür' if self.language == 'Turkish' else 'Convert')
        self.convert_button.clicked.connect(self.on_convert_clicked)
        layout.addWidget(self.convert_button)
        
        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def on_convert_clicked(self):
        try:
            value = float(self.value_input.text())
            if self.converter_type.currentText() == ("İnçten CM'ye" if self.language == 'Turkish' else "Inch to CM"):
                result = value * 2.54
                self.result_label.setText(f"{value} inç {result:.2f} cm'dir" if self.language == 'Turkish' else f"{value} inches is {result:.2f} cm")
            else:
                result = value / 2.54
                self.result_label.setText(f"{value} cm {result:.2f} inçtir" if self.language == 'Turkish' else f"{value} cm is {result:.2f} inches")
        except ValueError:
            QMessageBox.warning(self, '', 'Lütfen geçerli bir sayı girin.' if self.language == 'Turkish' else 'Please enter a valid number.')


class ContactApplicationWindow(QWidget):
    def __init__(self, language):
        super().__init__()
        self.language = language
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Rehber Uygulaması" if self.language == 'Turkish' else "Contact Application")
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        layout.addWidget(QLabel("İsim:" if self.language == 'Turkish' else "Name:"))
        layout.addWidget(self.name_input)
        
        self.phone_input = QLineEdit()
        layout.addWidget(QLabel("Telefon Numarası:" if self.language == 'Turkish' else "Phone Number:"))
        layout.addWidget(self.phone_input)
        
        self.add_button = QPushButton('Kontak Ekle' if self.language == 'Turkish' else 'Add Contact')
        self.add_button.clicked.connect(self.on_add_clicked)
        layout.addWidget(self.add_button)

        self.contact_list = QListWidget()
        layout.addWidget(self.contact_list)

        self.setLayout(layout)

    def on_add_clicked(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        if name and phone:
            # Add logic to actually store the contacts
            self.contact_list.addItem(f"{name}: {phone}")
        else:
            QMessageBox.warning(self, '', 'Lütfen hem adı hem de telefon numarasını girin.' if self.language == 'Turkish' else 'Please enter both name and phone number.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec_())
