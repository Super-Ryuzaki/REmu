import os
import sys
import Emuchecker
import Switch
import Psx
import Ps2
import Dlgames
import subprocess
import Ds
import Wiiu
import psp

try:
    from PyQt5.QtGui import QPalette, QColor
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy
    from PyQt5.QtCore import Qt
except:
    os.system("pip install pyqt5")
    os.system("pip install wget")
    os.system("pip install requests")
    from PyQt5.QtGui import QPalette, QColor
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy
    from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("REmu")
        self.setFixedSize(400, 400)

        # Set the background color of the window
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#2f2f2f"))
        palette.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(palette)

        # Check if REmu folder exists in C:/
        remu_folder = "C:/REmu"
        if not os.path.exists(remu_folder):
            os.mkdir(remu_folder)
            emulators = ["Playstation1", "Playstation2", "Switch", "WiiU", "Nintendo DS","PSP"]
            for emulator in emulators:
                os.mkdir(os.path.join(remu_folder, emulator))

        # Create buttons for different game consoles
        playstation1_button = QPushButton("Playstation 1")
        playstation2_button = QPushButton("Playstation 2")
        psp_button = QPushButton("PlayStation Portable")
        switch_button = QPushButton("Switch")
        ds_button = QPushButton("DS")
        wiiu_button = QPushButton("Wii U")
        
        # Create buttons for Download Games and Exit
        dlgames_button = QPushButton("Download Games")

        # Connect buttons to their respective functions
        playstation1_button.clicked.connect(self.show_playstation1)
        playstation1_button.setStyleSheet("background-color: #8b008b; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")
        
        playstation2_button.clicked.connect(self.show_playstation2)
        playstation2_button.setStyleSheet("background-color: #8b008b; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")
        
        psp_button.clicked.connect(self.show_psp)
        psp_button.setStyleSheet("background-color: #8b008b; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")
        
        switch_button.clicked.connect(self.show_switch)
        switch_button.setStyleSheet("background-color: #8b008b; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")
        
        ds_button.clicked.connect(self.show_nintendo_ds)
        ds_button.setStyleSheet("background-color: #8b008b; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")
        
        wiiu_button.clicked.connect(self.show_wiiu)
        wiiu_button.setStyleSheet("background-color: #8b008b; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")
        
        dlgames_button.clicked.connect(self.show_dlgames)
        dlgames_button.setStyleSheet("background-color: #0066CC; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")

        # Add buttons to a vertical layout
        sony_layout = QVBoxLayout()
        sony_layout.addWidget(playstation1_button)
        sony_layout.addWidget(playstation2_button)
        sony_layout.addWidget(psp_button)
        sony_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        nintendo_layout = QVBoxLayout()
        nintendo_layout.addWidget(switch_button)
        nintendo_layout.addWidget(ds_button)
        nintendo_layout.addWidget(wiiu_button)
        nintendo_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # Add a spacer item to create some space between the Emulators and Download Games button
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Add the Download Games and Exit button to the bottom of the UI
        bottom_layout = QHBoxLayout()
        bottom_layout.addItem(spacer)
        bottom_layout.addWidget(dlgames_button)


        # Add the buttons layouts and the bottom layout to a vertical layout
        v_layout =QVBoxLayout()
        v_layout.addLayout(sony_layout)
        v_layout.addLayout(nintendo_layout)
        v_layout.addLayout(bottom_layout)
        
        # Create a widget to hold the layout and set it as the main widget of the window
        widget = QWidget()
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)

    def show_playstation1(self):
        epsxe_path = Emuchecker.get_epsxe_path()
        psx_ui = Psx.LaunchGameUI()
        self.setCentralWidget(psx_ui)

    def show_playstation2(self):
        pcsx2_path = Emuchecker.get_pcsx2_path()
        pcsx2_ui = Ps2.LaunchGameUI()
        self.setCentralWidget(pcsx2_ui)

    def show_switch(self):
        switch_ui = Switch.LaunchGameUI()
        self.setCentralWidget(switch_ui)
        
    def show_wiiu(self):
        wiiu_ui = Wiiu.LaunchGameUI()
        self.setCentralWidget(wiiu_ui)

    def show_nintendo_ds(self):
        ds_ui = Ds.LaunchGameUI()
        self.setCentralWidget(ds_ui)

    def show_dlgames(self):
        dlgames_ui = Dlgames.MainWindow()
        self.setCentralWidget(dlgames_ui)

    def show_psp(self):
        psp_ui = psp.LaunchGameUI()
        self.setCentralWidget(psp_ui)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
