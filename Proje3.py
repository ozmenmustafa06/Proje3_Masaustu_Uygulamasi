import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
                             QMessageBox, QComboBox, QListWidget, QInputDialog)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.language = 'Turkish'  # Default language set to Turkish
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('MustiZone Çok Fonksiyonlu Uygulama - Türkçe' if self.language == 'Turkish' else 'MustiZone Multi-function App - English')
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Dil seçimi için etiket ekleniyor
        self.language_label = QLabel('Dil:' if self.language == 'Turkish' else 'Language:')
        self.layout.addWidget(self.language_label)

        self.language_selector = QComboBox()
        self.language_selector.addItems(['Türkçe', 'English'])
        self.language_selector.currentTextChanged.connect(self.update_language)
        self.layout.addWidget(self.language_selector)

        self.create_widgets()
        self.show_widgets()

    def create_widgets(self):
        self.password_label = QLabel('Şifrenizi girin:' if self.language == 'Turkish' else 'Enter your password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Giriş Yap' if self.language == 'Turkish' else 'Login')
        self.login_button.clicked.connect(self.on_login_clicked)
        self.function_menu = QComboBox()
        self.function_menu.addItems(["Fonksiyon Seçin", "Çeviri Uygulaması", "Rehber Uygulaması"] if self.language == 'Turkish' else ["Select Function", "Translation Application", "Contact Application"])
        self.function_menu.currentIndexChanged.connect(self.on_function_selected)

    def show_widgets(self):
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.function_menu)
        self.function_menu.setVisible(False)

    def update_language(self, language):
        self.language = language
        self.setWindowTitle('MustiZone Çok Fonksiyonlu Uygulama - Türkçe' if self.language == 'Turkish' else 'MustiZone Multi-function App - English')
        self.password_label.setText('Şifrenizi girin:' if self.language == 'Turkish' else 'Enter your password:')
        self.login_button.setText('Giriş Yap' if self.language == 'Turkish' else 'Login')
        self.function_menu.setItemText(0, "Fonksiyon Seçin" if self.language == 'Turkish' else "Select Function")
        self.function_menu.setItemText(1, "Çeviri Uygulaması" if self.language == 'Turkish' else "Translation Application")
        self.function_menu.setItemText(2, "Rehber Uygulaması" if self.language == 'Turkish' else "Contact Application")
        self.language_label.setText('Dil:' if self.language == 'Turkish' else 'Language:')

    def on_login_clicked(self):
        password = self.password_input.text()
        if password == "mustafa123":
            QMessageBox.information(self, '', 'Giriş başarılı!' if self.language == 'Turkish' else 'Login successful!')
            self.function_menu.setVisible(True)
        else:
            QMessageBox.warning(self, '', 'Yanlış şifre!' if self.language == 'Turkish' else 'Incorrect password!')

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
        
        self.info_label = QLabel()
        layout.addWidget(self.info_label)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.update_info_label()

        self.converter_type.currentIndexChanged.connect(self.update_info_label)

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

    def update_info_label(self):
        if self.converter_type.currentText() == ("İnçten CM'ye" if self.language == 'Turkish' else "Inch to CM"):
            self.info_label.setText("1 inç 2.54 cm'dir." if self.language == 'Turkish' else "1 inch is 2.54 cm.")
        else:
            self.info_label.setText("1 cm 0.3937 inçtir." if self.language == 'Turkish' else "1 cm is 0.3937 inches.")

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

        self.edit_button = QPushButton('Kontak Düzenle' if self.language == 'Turkish' else 'Edit Contact')
        self.edit_button.clicked.connect(self.on_edit_clicked)
        layout.addWidget(self.edit_button)

        self.contact_list = QListWidget()
        layout.addWidget(self.contact_list)

        self.delete_selected_button = QPushButton('Seçileni Sil' if self.language == 'Turkish' else 'Delete Selected')
        self.delete_selected_button.clicked.connect(self.on_delete_selected_clicked)
        layout.addWidget(self.delete_selected_button)

        self.delete_all_button = QPushButton('Tümünü Sil' if self.language == 'Turkish' else 'Delete All')
        self.delete_all_button.clicked.connect(self.on_delete_all_clicked)
        layout.addWidget(self.delete_all_button)

        self.setLayout(layout)
        self.load_contacts()

    def on_add_clicked(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        if not name or not phone:
            QMessageBox.warning(self, '', 'Lütfen hem adı hem de telefon numarasını girin.' if self.language == 'Turkish' else 'Please enter both name and phone number.')
            return
        if not phone.isdigit() or len(phone) < 10:
            QMessageBox.warning(self, '', 'Lütfen geçerli bir telefon numarası girin (en az 10 rakam ve sadece sayılar).' if self.language == 'Turkish' else 'Please enter a valid phone number (at least 10 digits and only numbers).')
            return
        self.contact_list.addItem(f"{name}: {phone}")
        self.save_contact(name, phone)
        self.name_input.clear()
        self.phone_input.clear()

    def on_edit_clicked(self):
        selected_item = self.contact_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, '', 'Lütfen düzenlemek için bir kontak seçin.' if self.language == 'Turkish' else 'Please select a contact to edit.')
            return
        old_data = selected_item.text().split(': ')
        new_name, ok1 = QInputDialog.getText(self, 'Kontak Düzenle' if self.language == 'Turkish' else 'Edit Contact', 'İsim:' if self.language == 'Turkish' else 'Name:', QLineEdit.Normal, old_data[0])
        if ok1 and new_name:
            new_phone, ok2 = QInputDialog.getText(self, 'Kontak Düzenle' if self.language == 'Turkish' else 'Edit Contact', 'Telefon Numarası:' if self.language == 'Turkish' else 'Phone Number:', QLineEdit.Normal, old_data[1])
            if ok2 and new_phone:
                if not new_phone.isdigit() or len(new_phone) < 10:
                    QMessageBox.warning(self, '', 'Lütfen geçerli bir telefon numarası girin (en az 10 rakam ve sadece sayılar).' if self.language == 'Turkish' else 'Please enter a valid phone number (at least 10 digits and only numbers).')
                else:
                    selected_item.setText(f"{new_name}: {new_phone}")
                    self.update_contacts()

    def save_contact(self, name, phone):
        with open("contacts.txt", "a") as file:
            file.write(f"{name}: {phone}\n")

    def load_contacts(self):
        try:
            with open("contacts.txt", "r") as file:
                for line in file:
                    self.contact_list.addItem(line.strip())
        except FileNotFoundError:
            open("contacts.txt", "w").close()

    def update_contacts(self):
        with open("contacts.txt", "w") as file:
            for index in range(self.contact_list.count()):
                file.write(self.contact_list.item(index).text() + "\n")

    def on_delete_selected_clicked(self):
        for item in self.contact_list.selectedItems():
            self.contact_list.takeItem(self.contact_list.row(item))
        self.update_contacts()

    def on_delete_all_clicked(self):
        self.contact_list.clear()
        self.update_contacts()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec_())
