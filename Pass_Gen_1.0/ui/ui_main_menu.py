# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QIcon)
from PySide6.QtWidgets import (QAbstractSpinBox, QFrame, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(541, 542)
        MainWindow.setStyleSheet(u"QWidget {                            \n"
"    background: #191919;\n"
"    color: white;                    \n"
"    font-family:Dialog;              \n"
"    margin: 10px;                    \n"
"    font-size: 16pt;                 \n"
"}                                    \n"
"                                     \n"
"QPushButton {                        \n"
"    border: 2px solid lightslategray;\n"
"    border-radius: 5px;              \n"
"}                                    \n"
"                                     \n"
"QPushButton #low upper dig spec {    \n"
"    padding: 10px;                   \n"
"}                                    \n"
"                                     \n"
"QPushButton:hover {                  \n"
"    border-color: #090;              \n"
"}                                    \n"
"                                     \n"
"QPushButton:pressed {                \n"
"    border: 4px solid #090;          \n"
"    border-radius: 5px;              \n"
"}                             "
                        "       \n"
"                                     \n"
"QPushButton:checked {                \n"
"    background-color: #006300;       \n"
"    border-color: #090;\n"
"}              \n"
"\n"
"QFrame {                   \n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;    \n"
"    margin-right: 0;       \n"
"}                          \n"
"                           \n"
"QFrame:hover {             \n"
"    border-color: #090;    \n"
"}             \n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"    margin: 0;\n"
"    font-size: 20pt;\n"
"}             \n"
"                         ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border: none;\n"
"font-family: Foldit;       \n"
"")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.iconlock = QPushButton(self.centralwidget)
        self.iconlock.setObjectName(u"iconlock")
        self.iconlock.setEnabled(False)
        self.iconlock.setStyleSheet(u"QPushButton {               \n"
"	border: none\n"
"}                                    ")
        icon = QIcon()
        icon.addFile(u":/newPrefix/ui/icons/lock-32.ico", QSize(), QIcon.Disabled, QIcon.On)
        self.iconlock.setIcon(icon)
        self.iconlock.setIconSize(QSize(150, 150))

        self.verticalLayout.addWidget(self.iconlock)

        self.layout_password = QHBoxLayout()
        self.layout_password.setObjectName(u"layout_password")
        self.frame_password = QFrame(self.centralwidget)
        self.frame_password.setObjectName(u"frame_password")
        self.frame_password.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_password.sizePolicy().hasHeightForWidth())
        self.frame_password.setSizePolicy(sizePolicy)
        self.frame_password.setFrameShape(QFrame.StyledPanel)
        self.frame_password.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_password)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.line_password = QLineEdit(self.frame_password)
        self.line_password.setObjectName(u"line_password")

        self.horizontalLayout_6.addWidget(self.line_password)

        self.btn_visibility = QPushButton(self.frame_password)
        self.btn_visibility.setObjectName(u"btn_visibility")
        self.btn_visibility.setEnabled(True)
        self.btn_visibility.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visibility.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    margin: 0;\n"
"    background-color: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/ui/icons/visibility_off_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/newPrefix/ui/icons/visibility_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_visibility.setIcon(icon1)
        self.btn_visibility.setIconSize(QSize(35, 35))
        self.btn_visibility.setCheckable(True)
        self.btn_visibility.setChecked(True)

        self.horizontalLayout_6.addWidget(self.btn_visibility)


        self.layout_password.addWidget(self.frame_password)

        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"btn_refresh")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_refresh.sizePolicy().hasHeightForWidth())
        self.btn_refresh.setSizePolicy(sizePolicy1)
        self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"QPushButton {\n"
"    margin-right: 0;\n"
"    margin-left: 0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/ui/icons/refresh_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_refresh.setIcon(icon2)
        self.btn_refresh.setIconSize(QSize(50, 50))
        self.btn_refresh.setCheckable(False)
        self.btn_refresh.setChecked(False)

        self.layout_password.addWidget(self.btn_refresh)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_copy.sizePolicy().hasHeightForWidth())
        self.btn_copy.setSizePolicy(sizePolicy2)
        self.btn_copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_copy.setStyleSheet(u"QPushButton {\n"
"    padding: 5px;\n"
"    margin-left: 0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/ui/icons/content_copy_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_copy.setIcon(icon3)
        self.btn_copy.setIconSize(QSize(40, 40))
        self.btn_copy.setCheckable(False)
        self.btn_copy.setChecked(False)

        self.layout_password.addWidget(self.btn_copy)


        self.verticalLayout.addLayout(self.layout_password)

        self.layout_info = QHBoxLayout()
        self.layout_info.setObjectName(u"layout_info")
        self.label_entropy = QLabel(self.centralwidget)
        self.label_entropy.setObjectName(u"label_entropy")
        sizePolicy.setHeightForWidth(self.label_entropy.sizePolicy().hasHeightForWidth())
        self.label_entropy.setSizePolicy(sizePolicy)
        self.label_entropy.setStyleSheet(u"border: none")

        self.layout_info.addWidget(self.label_entropy, 0, Qt.AlignHCenter)

        self.label_strength = QLabel(self.centralwidget)
        self.label_strength.setObjectName(u"label_strength")
        sizePolicy.setHeightForWidth(self.label_strength.sizePolicy().hasHeightForWidth())
        self.label_strength.setSizePolicy(sizePolicy)
        self.label_strength.setStyleSheet(u"border: none")

        self.layout_info.addWidget(self.label_strength, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.layout_info)

        self.layout_lenght = QHBoxLayout()
        self.layout_lenght.setObjectName(u"layout_lenght")
        self.slider_length = QSlider(self.centralwidget)
        self.slider_length.setObjectName(u"slider_length")
        self.slider_length.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_length.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background-color: transparent;\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #090;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"    width: 22px;\n"
"    border-radius: 10px;\n"
"    margin-top: -8px;\n"
"    margin-bottom: -8px;\n"
"}")
        self.slider_length.setMaximum(100)
        self.slider_length.setValue(12)
        self.slider_length.setOrientation(Qt.Horizontal)

        self.layout_lenght.addWidget(self.slider_length)

        self.spinbox_length = QSpinBox(self.centralwidget)
        self.spinbox_length.setObjectName(u"spinbox_length")
        self.spinbox_length.setMouseTracking(False)
        self.spinbox_length.setStyleSheet(u"QSpinBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    background: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border-color: #009900;\n"
"}")
        self.spinbox_length.setReadOnly(False)
        self.spinbox_length.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinbox_length.setAccelerated(False)
        self.spinbox_length.setMaximum(100)
        self.spinbox_length.setValue(12)

        self.layout_lenght.addWidget(self.spinbox_length, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addLayout(self.layout_lenght)

        self.layout_characters = QHBoxLayout()
        self.layout_characters.setObjectName(u"layout_characters")
        self.btn_upper = QPushButton(self.centralwidget)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.layout_characters.addWidget(self.btn_upper)

        self.btn_lower = QPushButton(self.centralwidget)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.layout_characters.addWidget(self.btn_lower)

        self.btn_digits = QPushButton(self.centralwidget)
        self.btn_digits.setObjectName(u"btn_digits")
        self.btn_digits.setCheckable(True)
        self.btn_digits.setChecked(True)

        self.layout_characters.addWidget(self.btn_digits)

        self.bnt_special = QPushButton(self.centralwidget)
        self.bnt_special.setObjectName(u"bnt_special")
        self.bnt_special.setCheckable(True)

        self.layout_characters.addWidget(self.bnt_special)


        self.verticalLayout.addLayout(self.layout_characters)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pass_gen_1.0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"August Feuerbach", None))
        self.iconlock.setText("")
#if QT_CONFIG(shortcut)
        self.iconlock.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_visibility.setText("")
        self.btn_refresh.setText("")
#if QT_CONFIG(shortcut)
        self.btn_refresh.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.btn_copy.setText("")
#if QT_CONFIG(shortcut)
        self.btn_copy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.label_entropy.setText("")
        self.label_strength.setText("")
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_digits.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.bnt_special.setText(QCoreApplication.translate("MainWindow", u"!@#$%^&*()_+", None))
    # retranslateUi

