import sys
from ui.ui_main_menu import Ui_MainWindow
import buttons
import password
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
import ui.resources


class PassGen(QMainWindow):
    def __init__(self):
        super(PassGen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connect_slider_to_spinbox()
        self.set_password()
        self.edit_pass()

        # зєднюємо кнопку з методом в конструкторі
        for btn in buttons.Generate_Password:
            getattr(self.ui,btn).clicked.connect(self.set_password)

        self.ui.btn_visibility.clicked.connect(self.change_password_visibility_method)
        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)

    # звязуємо метод класу програми який буде звязувати значення слайдера й лічильника
    def connect_slider_to_spinbox(self) -> None:
        self.ui.slider_length.valueChanged.connect(self.ui.spinbox_length.setValue)
        self.ui.spinbox_length.valueChanged.connect(self.ui.slider_length.setValue)
        self.ui.spinbox_length.valueChanged.connect(self.set_password)


    #зміна ентропії при самостійній зміні паролю *кончено зроблено*
    def edit_pass(self) -> None:
        self.ui.line_password.textEdited.connect(self.set_entropy)
        self.ui.line_password.textEdited.connect(self.set_strength)


    # получаємо строку символів для паролю. Створимо новий метод для получення відмічених кнопок
    def get_characters(self) -> str:
        chars = ""
        for btn in buttons.Characters:
            if getattr(self.ui, btn.name).isChecked():
                chars += btn.value
        return chars

    #ставимо метод установки паролю й оброблюємо помилку при відсутності символів
    def set_password(self) -> None:
        try:
            self.ui.line_password.setText(
                password.create_new(
                    length=self.ui.slider_length.value(),
                    characters=self.get_characters())
                )
        except IndexError:
            self.ui.line_password.clear()
        self.set_entropy()
        self.set_strength()

    #получаємо к-сть символів. Працюємо з словником
    def get_character_number(self) -> int:
        numb = 0
        for btn in buttons.Character_Number.items():
            if getattr(self.ui, btn[0]).isChecked():
                numb += btn[1]
        return numb

    #Ставимо ентропію паролю
    def set_entropy(self) -> None:
        length = len(self.ui.line_password.text()) #беремо довжину іменно з тексту паролю а не з слайледа і лічильника
        char_num = self.get_character_number()
        self.ui.label_entropy.setText(
            f"Entropy: {password.get_entropy(length, char_num)} bit" #лейбл ставимо вираз за допомогою f-строки
        )

    #ставимо метод повідомлення про важкість паролю
    def set_strength(self) -> None:
        length = len(self.ui.line_password.text())
        char_num = self.get_character_number()

        for strength in password.StrengthToEntropy:
            if password.get_entropy(length, char_num) >= strength.value:
                self.ui.label_strength.setText(f"Strength: {strength.name}")

    #створюємо метод видимості паролю. Незабуваємо додати необхідні модулі для QlineEdit
    def change_password_visibility_method(self) -> None:
        if self.ui.btn_visibility.isChecked():
            self.ui.line_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.line_password.setEchoMode(QLineEdit.Password)

    #копіюємо пароль в буфер обміну
    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.ui.line_password.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PassGen()
    window.show()

    sys.exit(app.exec())