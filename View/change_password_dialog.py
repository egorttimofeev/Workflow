from PyQt6 import QtWidgets, QtCore

class ChangePasswordDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Смена пароля")
        self.setFixedSize(400, 150)
        
        # Создаем лэйаут
        layout = QtWidgets.QVBoxLayout()
        
        # Метка и поле для старого пароля
        old_password_layout = QtWidgets.QHBoxLayout()
        old_password_label = QtWidgets.QLabel("Текущий пароль:")
        self.old_password_input = QtWidgets.QLineEdit()
        self.old_password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        old_password_layout.addWidget(old_password_label)
        old_password_layout.addWidget(self.old_password_input)
        
        # Метка и поле для нового пароля
        new_password_layout = QtWidgets.QHBoxLayout()
        new_password_label = QtWidgets.QLabel("Новый пароль:    ")
        self.new_password_input = QtWidgets.QLineEdit()
        self.new_password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        new_password_layout.addWidget(new_password_label)
        new_password_layout.addWidget(self.new_password_input)
        
        # Кнопка для изменения пароля
        button_layout = QtWidgets.QHBoxLayout()
        self.change_button = QtWidgets.QPushButton("Сохранить")
        self.change_button.setStyleSheet("background-color: lightblue;")
        self.cancel_button = QtWidgets.QPushButton("Отмена")
        self.cancel_button.setStyleSheet("background-color: lightblue;")

        button_layout.addStretch()
        button_layout.addWidget(self.change_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addStretch()
        
        # Добавляем все элементы в вертикальный лэйаут
        layout.addLayout(old_password_layout)
        layout.addLayout(new_password_layout)
        layout.addStretch()
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        
        # Связываем сигналы с слотами
        self.change_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
    
    def get_passwords(self):
        return self.old_password_input.text(), self.new_password_input.text()