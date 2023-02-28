import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QPushButton, QVBoxLayout, QMainWindow, QWidget
from Emugame import get_ds_games, get_game_path
import REmu
import Emuchecker

class LaunchGameUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel("Select a game:")
        self.game_combo = QComboBox()
        self.game_combo.addItems(get_ds_games())

        button = QPushButton("Launch")
        button.clicked.connect(self.launch_game)
        button.setStyleSheet("background-color: #8b008b; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")

        back_button = QPushButton("Back")
        back_button.clicked.connect(self.back)
        back_button.setStyleSheet("background-color: #0066CC; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.game_combo)
        layout.addWidget(button)
        layout.addWidget(back_button)

        # Create a widget to hold the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        central_widget.setStyleSheet("background-color: #2f2f2f; color: #ffffff; font-size: 15px;")
        # Set the central widget of the main window
        self.setCentralWidget(central_widget)
        Emuchecker.get_desmume_path()

    def launch_game(self):
        game = self.game_combo.currentText()
        game_path = get_game_path('Nintendo DS', game)
        desmume_path = Emuchecker.get_desmume_path()

        if not os.path.exists(desmume_path):
            print(f"Error: {desmume_path} does not exist")
            sys.exit()

        command = f'"{desmume_path}" "{game_path}"'
        subprocess.Popen(command, shell=True)

    def back(self):
        remu_window = REmu.MainWindow()
        self.setCentralWidget(remu_window)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    launch_game_ui = LaunchGameUI()
    launch_game_ui.show()
