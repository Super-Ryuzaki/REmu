import sys
import os
import zipfile
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMainWindow
from PyQt5.QtCore import Qt
import REmu

# Dictionaries of games and their URLs
games_dict = {
    "Playstation 1": {
        "Tomba! 2": "ADD URL",
        "Digimon World": "ADD URL",
        "Yu-gi-oh! Forbidden Memories": "ADD URL"
        # ...
    },
    "Playstation 2": {
        "Grand Theft Auto: San Andreas": "ADD URL",
        "Dragon Quest VIII: Journey of the Cursed King": "ADD URL",
        "God of War": "ADD URL"
        # ...
    },
    "PSP": {
        "MediEvil Resurrection": "ADD URL",
        "Digimon World Re:Digitize": "ADD URL",
        "Naruto: Ultimate Ninja Heroes": "ADD URL"
        # ...
    },
    "Wii U": {
        "Mario Kart 8": "ADD URL",
        "The Legend of Zelda: Twilight Princess": "ADD URL",
        "Mario Party 10": "ADD URL"
        # ...
    },    
    "Switch": {
        "Fire Emblem: Engage": "ADD URL",
        "Super Smash Bros. Ultimate": "ADD URL",
        "The Legend of Zelda: Breath of the Wild": "ADD URL"
        # ...
    },
    "Nintendo DS": {
        "Pokemon: Pearl": "ADD URL",
        "Nintendogs": "ADD URL",
        "Pokemon: Diamond": "ADD URL"
        # ...
    }
}

# Create the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the widgets
        self.title_label = QLabel("Download Games")
        self.option_label = QLabel("Select Option:")
        self.option_list = QListWidget()
        self.option_list.addItems(games_dict.keys())
        self.search_label = QLabel("Search Game:")
        self.search_input = QLineEdit()
        self.download_button = QPushButton("Download")
        self.download_button.setStyleSheet("background-color: #8b008b; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")
        self.output_list = QListWidget()
        self.back_button = QPushButton("Back")
        self.back_button.setStyleSheet("background-color: #0066CC; color: #ffffff; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px;")
        # Create the layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.option_label)
        self.layout.addWidget(self.option_list)
        self.layout.addWidget(self.search_label)
        self.layout.addWidget(self.search_input)
        self.layout.addWidget(self.download_button)
        self.layout.addWidget(self.output_list)
        self.layout.addWidget(self.back_button)
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        central_widget.setStyleSheet("background-color: #2f2f2f; color: #ffffff; font-size: 15px;")
        self.setCentralWidget(central_widget)

        # Connect the signals to the slots
        self.option_list.currentItemChanged.connect(self.update_game_list)
        self.search_input.textChanged.connect(self.search_games)
        self.download_button.clicked.connect(self.download_game)
        self.back_button.clicked.connect(self.back_to_main)
    # Slot to update the list of games for the selected option
    def update_game_list(self, current, previous):
        self.output_list.clear()
        if current is not None:
            for game in games_dict[current.text()]:
                item = QListWidgetItem(game)
                item.setData(Qt.UserRole, games_dict[current.text()][game])
                self.output_list.addItem(item)

    # Slot to search for games
    def search_games(self, text):
        self.output_list.clear()
        for option in games_dict:
            for game in games_dict[option]:
                if text.lower() in game.lower():
                    item = QListWidgetItem(game)
                    item.setData(Qt.UserRole, games_dict[option][game])
                    self.output_list.addItem(item)

    # Slot to download the selected game

    def download_game(self):
        current_item = self.output_list.currentItem()
        if current_item is not None:
            game_title = current_item.text()
            game_url = current_item.data(Qt.UserRole)
            option = self.option_list.currentItem().text()
            print(f"Downloading '{game_title}' from the '{option}' option at URL '{game_url}'")
            
            # Create the directory if it doesn't exist
            games_folder = os.path.join("C:/", "REmu", "Games", option)
            os.makedirs(games_folder, exist_ok=True)
            
            # Download the game
            response = requests.get(game_url)
            with open(os.path.join(games_folder, f"{game_title}.zip"), "wb") as f:
                f.write(response.content)
            
            # Extract the game
            with zipfile.ZipFile(os.path.join(games_folder, f"{game_title}.zip"), 'r') as zip_ref:
                zip_ref.extractall(games_folder)

            print(f"'{game_title}' has been downloaded and extracted to '{games_folder}'.")


    # Slot to go back to the main window of REmu.py
    def back_to_main(self):
        remu_window = REmu.MainWindow()
        self.setCentralWidget(remu_window)
        self.resize(100, 100)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
