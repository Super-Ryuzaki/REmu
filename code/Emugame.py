import os
from PyQt5.QtWidgets import QFileDialog, QMessageBox

# Define the base directory for all emulator game folders
EMULATOR_BASE_DIR = "C:/REmu/"

# Define the game folder name for each emulator
EMULATOR_GAME_FOLDERS = {
    "Switch": "Games",
    "PS1": "PS1Games",
    "PS2": "PS2Games",
    "Wii U": "WiiU",
    "Nintendo DS": "Nintendo DS",
    "PSP": "PSP",
}

# Define the file extension for each emulator's game files
EMULATOR_FILE_EXTENSIONS = {
    "Switch": ".nsp",
    "PS1": ".bin",
    "PS2": ".iso",
    "Wii U": ".rpx",
    "Nintendo DS": ".nds",
    "PSP": ".iso"
}


def create_game_folder():
    """Create a game folder in C:/REmu/Games"""
    game_folder = os.path.join(EMULATOR_BASE_DIR, "Games")
    if not os.path.exists(game_folder):
        os.makedirs(game_folder)
    return game_folder

def get_game_folder_path(emulator):
    """Get the game folder path for the specified emulator"""
    game_folder = os.path.join(EMULATOR_BASE_DIR, emulator, EMULATOR_GAME_FOLDERS[emulator])
    
    # Check if gamepath.txt exists and read the game folder path from it
    if os.path.exists("C:/REmu/gamepath.txt"):
        with open("C:/REmu/gamepath.txt", "r") as f:
            saved_game_folder = f.read().strip()
        if os.path.exists(saved_game_folder):
            return saved_game_folder
    
    # If gamepath.txt doesn't exist or the saved game folder path is invalid, prompt the user to select the folder
    msg_box = QMessageBox()
    msg_box.setText(f"Do you have a {emulator} game folder?")
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    result = msg_box.exec_()
    if result == QMessageBox.Yes:
        game_folder = QFileDialog.getExistingDirectory(None, f"Select {emulator} game folder")
        if not game_folder:
            game_folder = os.path.join(EMULATOR_BASE_DIR, emulator, EMULATOR_GAME_FOLDERS[emulator])
    else:
        game_folder = create_game_folder()
    
    # Save the selected game folder path to gamepath.txt
    with open("C:/REmu/gamepath.txt", "w") as f:
        f.write(game_folder)
    
    return game_folder

def get_psp_games():
    """Get a list of all DS games that are 600MB or larger"""
    game_folder = get_game_folder_path("PSP")
    games = []
    for root, dirs, files in os.walk(game_folder):
        for file in files:
            if file.endswith(EMULATOR_FILE_EXTENSIONS["PSP"]):
                game_path = os.path.join(root, file)
                if os.path.getsize(game_path) >= 600 * 1024 * 1024:
                    games.append(game_path)
    return games


def get_ds_games():
    """Get a list of all DS games that are 32MB or larger"""
    game_folder = get_game_folder_path("Nintendo DS")
    games = []
    for root, dirs, files in os.walk(game_folder):
        for file in files:
            if file.endswith(EMULATOR_FILE_EXTENSIONS["Nintendo DS"]):
                game_path = os.path.join(root, file)
                if os.path.getsize(game_path) >= 32 * 1024 * 1024:
                    games.append(game_path)
    return games

def get_wiiu_games():
    """Get a list of all Wii U games"""
    game_folder = get_game_folder_path("Wii U")
    games = []
    for root, dirs, files in os.walk(game_folder):
        for file in files:
            if file.endswith(EMULATOR_FILE_EXTENSIONS["Wii U"]):
                game_path = os.path.join(root, file)
                games.append(game_path)
    return games

def get_switch_games():
    """Get a list of all Switch games that are 4GB or larger"""
    game_folder = get_game_folder_path("Switch")
    games = []
    for root, dirs, files in os.walk(game_folder):
        for file in files:
            if file.endswith(EMULATOR_FILE_EXTENSIONS["Switch"]):
                game_path = os.path.join(root, file)
                if os.path.getsize(game_path) >= 4 * 1024 * 1024 * 1024:
                    games.append(game_path)
    return games

def get_ps1_games():
    """Get a list of all PS1 games that are 300MB or larger"""
    game_folder = get_game_folder_path("PS1")
    games = []
    for root, dirs, files in os.walk(game_folder):
        for file in files:
            if file.endswith(EMULATOR_FILE_EXTENSIONS["PS1"]):
                game_path = os.path.join(root, file)
                if os.path.getsize(game_path) >= 300 * 1024 * 1024:
                    games.append(game_path)
    return games

def get_ps2_games():
    """Get a list of all PS2 games that are between 1.3GB and 4.7GB"""
    game_folder = get_game_folder_path("PS2")
    games = []
    for root, dirs, files in os.walk(game_folder):
        for file in files:
            if file.endswith(EMULATOR_FILE_EXTENSIONS["PS2"]):
                game_path = os.path.join(root, file)
                size = os.path.getsize(game_path)
                if size >= 1.1 * 1024 * 1024 * 1024 and size <= 4.7 * 1024 * 1024 * 1024:
                    games.append(game_path)
    return games

def get_game_path(emulator, game):
    """Get the path to the specified game for the specified emulator"""
    if emulator == "Switch":
        game_folder = get_game_folder_path("Switch")
    elif emulator == "PS1":
        game_folder = get_game_folder_path("PS1")
    elif emulator == "PS2":
        game_folder = get_game_folder_path("PS2")
    elif emulator == "Wii U":
        game_folder = get_game_folder_path("Wii U")
    elif emulator == "Nintendo DS":
        game_folder = get_game_folder_path("Nintendo DS")
    elif emulator == "PSP":
        game_folder = get_game_folder_path("PSP")
    game_path = os.path.join(game_folder, game)

    return game_path
    
    
    
# Create gamepath.txt to store the game folder path
if __name__ == "__main__":
    game_folder_path = get_game_folder_path("Switch")
    with open("gamepath.txt", "w") as f:
        f.write
