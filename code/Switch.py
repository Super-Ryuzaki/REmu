import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QPushButton, QVBoxLayout, QMainWindow, QWidget, QFileDialog, QMessageBox
from Emugame import get_switch_games, get_game_path
import Emuchecker
import REmu

ryujinx_path = ""

class LaunchGameUI(QMainWindow):
    def __init__(self):
        super().__init__()
        Emuchecker.get_ryujinx_path()
        global ryujinx_path
        ryujinx_path = Emuchecker.get_ryujinx_path()
        if not os.path.exists(ryujinx_path):
            print(f"Error: {ryujinx_path} does not exist")
            sys.exit()
        self.init_ui()

    def init_ui(self):
        # List all switch games
        games = get_switch_games()

        # Create the UI elements
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.game_label = QLabel("Select a game to launch:")
        self.game_combo = QComboBox()
        self.launch_button = QPushButton("Launch game")
        self.launch_button.setStyleSheet("background-color: #8b008b; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")
        self.back_button = QPushButton("Back")
        self.back_button.setStyleSheet("background-color: #0066CC; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")
        self.layout.addWidget(self.game_label)
        self.layout.addWidget(self.game_combo)
        self.layout.addWidget(self.launch_button)
        self.layout.addWidget(self.back_button)
        self.central_widget.setStyleSheet("background-color: #2f2f2f; color: #ffffff; font-size: 15px;")

        # Populate the drop-down menu with the list of switch games
        for game in games:
            self.game_combo.addItem(game)

        # Connect the launch button to the launch_game function
        self.launch_button.clicked.connect(self.launch_game)

        # Connect the back button to the back function
        self.back_button.clicked.connect(self.back)

        # Set the window properties
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Launch Game")
        self.show()

    def launch_game(self):
        # Get the selected game
        game = self.game_combo.currentText()
        # Construct the path to the game
        game_path = get_game_path('Switch',game)
        # Construct the command to launch Ryujinx with the game
        cmd = f'"{ryujinx_path}" "{game_path}"'
        # Launch Ryujinx with the game
        subprocess.Popen(cmd, shell=True)

    def back(self):
        remu_window = REmu.MainWindow()
        self.setCentralWidget(remu_window)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = LaunchGameUI()
    ui.show()
    sys.exit(app.exec_())
