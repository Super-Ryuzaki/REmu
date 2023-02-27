import os
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog
import wget
import zipfile
import subprocess

EMUPATHS_FILE = 'C:/REmu/emupaths.txt'
RYUJINX_DEFAULT_PATH = 'C:/REmu/Switch/Ryujinx.exe'
EPSXE_DEFAULT_PATH = 'C:/REmu/Playstation1/ePSXe.exe'
PCSX2_DEFAULT_PATH = 'C:/REmu/Playstation2/PCSX2 1.6.0/pcsx2.exe'
CEMU_DEFAULT_PATH = 'C:/REmu/WiiU/cemu/Cemu.exe'
DS_DEFAULT_PATH = 'C:/REmu/Nintendo DS/DeSmuME_0.9.11_x86.exe'
PSP_DEFAULT_PATH = 'C:/REmu/PSP/'

def get_psp_path():
    emu_paths = {}
    if os.path.exists(EMUPATHS_FILE):
        with open(EMUPATHS_FILE, 'r') as f:
            for line in f:
                if ':' not in line:
                    continue
                name, path = line.strip().split(':', 1)
                emu_paths[name] = path

        psp_path = emu_paths.get('PSP', None)
        if psp_path and os.path.exists(psp_path):
            return psp_path

    # Ask the user if they have PSP emulator
    response = QMessageBox.question(None, "PSP emulator not found", "Do you have PSP emulator?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    if response == QMessageBox.Yes:
        # Open a window to let the user navigate to the folder where the emulator is located
        root = QMainWindow()
        root.show()
        root.setGeometry(100, 100, 300, 200)
        psp_path, _ = QFileDialog.getOpenFileName(root, 'Open file', PSP_DEFAULT_PATH, 'Executable Files (*.exe)')

        if psp_path and os.path.exists(psp_path):
            emu_paths['PSP'] = psp_path
            with open(EMUPATHS_FILE, 'w') as f:
                for name, path in emu_paths.items():
                    f.write(f"{name}:{path}\n")
            return psp_path

    else:
        print("Downloading PSP emulator...")
        url = "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212594&authkey=ACrwpvQsJXzI5as"
        output_path = os.path.join(PSP_DEFAULT_PATH, "PSP.zip")
        wget.download(url, out=output_path)

        # Extract PSP emulator to the C:/REmu/PSP folder
        with zipfile.ZipFile(output_path, 'r') as zip_ref:
            zip_ref.extractall(PSP_DEFAULT_PATH)

        # Delete the downloaded zip file
        os.remove(output_path)

        # Check if the PSP emulator was extracted
        psp_path = os.path.join(PSP_DEFAULT_PATH, "PPSSPPWindows.exe")
        if not os.path.exists(psp_path):
            print("Error: PSP emulator not found in C:/REmu/PSP Folder.")
        else:
            emu_paths['PSP'] = psp_path
            with open(EMUPATHS_FILE, 'w') as f:
                for name, path in emu_paths.items():
                    f.write(f"{name}:{path}\n")
            print("\n PSP emulator download and extraction completed")
            return psp_path
                
def get_cemu_path():
    emu_paths = {}
    if os.path.exists(EMUPATHS_FILE):
        with open(EMUPATHS_FILE, 'r') as f:
            for line in f:
                if ':' not in line:
                    continue
                name, path = line.strip().split(':', 1)
                emu_paths[name] = path

        cemu_path = emu_paths.get('Cemu', None)
        if cemu_path and os.path.exists(cemu_path):
            return cemu_path

    # Ask the user if they have Cemu
    response = QMessageBox.question(None, "Cemu not found", "Do you have Cemu emulator?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    if response == QMessageBox.Yes:
        # Open a window to let the user navigate to the folder where Cemu is located
        root = QMainWindow()
        root.show()
        root.setGeometry(100, 100, 300, 200)
        cemu_path, _ = QFileDialog.getOpenFileName(root, 'Open file', CEMU_DEFAULT_PATH, 'Executable Files (*.exe)')

        if cemu_path and os.path.exists(cemu_path):
            emu_paths['Cemu'] = cemu_path
            with open(EMUPATHS_FILE, 'w') as f:
                for name, path in emu_paths.items():
                    f.write(f"{name}:{path}\n")
            return cemu_path

    print("Downloading Cemu...")
    url = "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212577&authkey=AE7aHCL5fXkvPfQ"
    output_path = os.path.join("C:/REmu/WiiU", "Cemu.zip")
    wget.download(url, out=output_path)

    # Extract Cemu to the C:/REmu/WiiU folder
    with zipfile.ZipFile(output_path, 'r') as zip_ref:
        zip_ref.extractall("C:/REmu/WiiU")

    # Delete the downloaded zip file
    os.remove(output_path)

    # Check if Cemu was extracted
    cemu_path = os.path.join("C:/REmu/WiiU/cemu", "Cemu.exe")
    if not os.path.exists(cemu_path):
        print("Error: Cemu not found in C:/REmu/WiiU/cemu Folder.")
    else:
        emu_paths['Cemu'] = cemu_path
        with open(EMUPATHS_FILE, 'w') as f:
            for name, path in emu_paths.items():
                f.write(f"{name}:{path}\n")
        print("\n Cemu download and extraction completed")
        return cemu_path

def get_desmume_path():
    emu_paths = {}
    if not os.path.exists(EMUPATHS_FILE):
        with open(EMUPATHS_FILE, 'w'):
            pass
    else:
        with open(EMUPATHS_FILE, 'r') as f:
            for line in f:
                if ':' not in line:
                    continue
                name, path = line.strip().split(':', 1)
                emu_paths[name] = path
        if 'DeSmuME' in emu_paths:
            desmume_path = emu_paths.get('DeSmuME')
            if os.path.exists(desmume_path):
                return desmume_path

        # Ask the user if they have DeSmuME
        response = QMessageBox.question(None, "DeSmuME not found", "Do you have DeSmuME emulator?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if response == QMessageBox.Yes:
            # Open a window to let the user navigate to the folder where DeSmuME is located
            root = QMainWindow()
            root.show()
            root.setGeometry(100, 100, 300, 200)
            desmume_path = QFileDialog.getOpenFileName(root, 'Open file', DS_DEFAULT_PATH, 'Executable Files (*.exe)')[0]
            if desmume_path:
                emu_paths['DeSmuME'] = desmume_path
                with open(EMUPATHS_FILE, 'w') as f:
                    for name, path in emu_paths.items():
                        f.write(f"{name}:{path}\n")
                return desmume_path

        print("Downloading DeSmuME...")
        url = "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212578&authkey=AMGBwhQBg1LWGhA"
        output_path = os.path.join("C:/REmu/Nintendo DS", "DeSmuME.zip")
        wget.download(url, out=output_path)
        # Extract DeSmuME to the C:/REmu/Nintendo DS folder
        with zipfile.ZipFile(output_path, 'r') as zip_ref:
            zip_ref.extractall("C:/REmu/Nintendo DS")
        # Delete the downloaded zip file
        os.remove(output_path)
        # Check if DeSmuME was extracted
        desmume_path = os.path.join("C:/REmu/Nintendo DS", "DeSmuME_0.9.11_x86.exe")
        if not os.path.exists(desmume_path):
            print("Error: DeSmuME not found in C:/REmu/Nintendo DS folder.")
        else:
            emu_paths['DeSmuME'] = desmume_path
            with open(EMUPATHS_FILE, 'w') as f:
                for name, path in emu_paths.items():
                    f.write(f"{name}:{path}\n")
                print("\n DeSmuME download and extraction completed")
                return desmume_path
  
def get_pcsx2_path():
    emu_paths = {}
    if not os.path.exists(EMUPATHS_FILE):
        with open(EMUPATHS_FILE, 'w'):
            pass
    else:
        with open(EMUPATHS_FILE, 'r') as f:
            for line in f:
                if ':' not in line:
                    continue
                name, path = line.strip().split(':', 1)
                emu_paths[name] = path
        if 'PCSX2' in emu_paths:
            pcsx2_path = emu_paths.get('PCSX2')
            if os.path.exists(pcsx2_path):
                return pcsx2_path

        # Ask the user if they have pcsx2.exe
        response = QMessageBox.question(None, "PCSX2 not found", "Do you have pcsx2.exe?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if response == QMessageBox.Yes:
            # Open a window to let the user navigate to the folder where pcsx2.exe is located
            root = QMainWindow()
            root.show()
            root.setGeometry(100, 100, 300, 200)
            pcsx2_path = QFileDialog.getOpenFileName(root, 'Open file', PCSX2_DEFAULT_PATH, 'Executable Files (*.exe)')[0]
            if pcsx2_path:
                emu_paths['PCSX2'] = pcsx2_path
                with open(EMUPATHS_FILE, 'w') as f:
                    for name, path in emu_paths.items():
                        f.write(f"{name}:{path}\n")
                return pcsx2_path

        print("Downloading PCSX2...")
        url = "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212568&authkey=ACImlvBLKR4ToZw"
        output_path = os.path.join("C:/REmu/Playstation2", "PCSX2.zip")
        wget.download(url, out=output_path)
        # Extract PCSX2 to the C:/REmu/Playstation2 folder
        with zipfile.ZipFile(output_path, 'r') as zip_ref:
            zip_ref.extractall("C:/REmu/Playstation2")
        # Delete the downloaded zip file
        os.remove(output_path)
        # Check if PCSX2 was extracted
        pcsx2_path = os.path.join("C:/REmu/Playstation2/PCSX2 1.6.0", "PCSX2.exe")
        if not os.path.exists(pcsx2_path):
            print("Error: PCSX2 not found in C:/REmu/Playstation2/PCSX2 1.6.0 folder.")
        else:
            emu_paths['PCSX2'] = pcsx2_path
            with open(EMUPATHS_FILE, 'w') as f:
                for name, path in emu_paths.items():
                    f.write(f"{name}:{path}\n")
                print("\n PCSX2 download and extraction completed")
                
            # Download the PCSX2 bios
            if not os.path.exists("C:/REmu/Playstation2/PCSX2 1.6.0/bios"):
                os.makedirs("C:/REmu/Playstation2/PCSX2 1.6.0/bios")
            print("Downloading Bios...")
            bios_url ="https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212575&authkey=AD-GecUpU4YWztA"
            bios_output_path = os.path.join("C:/REmu/Playstation2/PCSX2 1.6.0/bios", "bios.zip")
            wget.download(bios_url, out=bios_output_path)
            with zipfile.ZipFile(bios_output_path, 'r') as bios_zip_ref:
                bios_zip_ref.extractall("C:/REmu/Playstation2/PCSX2 1.6.0/bios")
            os.remove(bios_output_path)

def get_epsxe_path():
    emu_paths = {}
    if not os.path.exists(EMUPATHS_FILE):
        with open(EMUPATHS_FILE, 'w') as f:
            f.write('')
    else:
        with open(EMUPATHS_FILE, 'r') as f:
            for line in f:
                if ':' not in line:
                    continue
                name, path = line.strip().split(':', 1)
                emu_paths[name] = path

    if 'ePSXe' in emu_paths:
        epsxe_path = emu_paths.get('ePSXe')
        if os.path.exists(epsxe_path):
            return epsxe_path

    # Ask the user if they have ePSXe.exe
    response = QMessageBox.question(None, "ePSXe not found", "Do you have ePSXe.exe?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    if response == QMessageBox.Yes:
        # Open a window to let the user navigate to the folder where ePSXe.exe is located
        root = QMainWindow()
        root.show()
        root.setGeometry(100, 100, 300, 200)
        epsxe_path = QFileDialog.getOpenFileName(root, 'Open file', EPSXE_DEFAULT_PATH, 'Executable Files (*.exe)')[0]
        if epsxe_path:
            emu_paths['ePSXe'] = epsxe_path
            with open(EMUPATHS_FILE, 'w') as f:
                for name, path in emu_paths.items():
                    f.write(f"{name}:{path}\n")
            return epsxe_path

    # Download ePSXe if it is not found
    if not os.path.exists("C:/REmu/Playstation1"):
        os.makedirs("C:/REmu/Playstation1")
    print("Downloading ePSXe...")
    url = "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212574&authkey=AKiAxMza8LBGV6g"
    output_path = os.path.join("C:/REmu/Playstation1", "ePSXe.zip")
    wget.download(url, out=output_path)
    # Extract ePSXe to the C:/REmu/Playstation1 folder
    with zipfile.ZipFile(output_path, 'r') as zip_ref:
        zip_ref.extractall("C:/REmu/Playstation1")
    # Delete the downloaded zip file
    os.remove(output_path)
    # Check if ePSXe was extracted
    epsxe_path = os.path.join("C:/REmu/Playstation1", "ePSXe.exe")
    if not os.path.exists(epsxe_path):
        print("Error: ePSXe not found in C:/REmu/Playstation1 folder.")
    else:
        emu_paths['ePSXe'] = epsxe_path
        with open(EMUPATHS_FILE, 'w') as f:
            for name, path in emu_paths.items():
                f.write(f"{name}:{path}\n")
            # Download the ePSXe bios
            if not os.path.exists("C:/REmu/Playstation1/bios"):
                os.makedirs("C:/REmu/Playstation1/bios")
            print("Downloading Bios...")
            bios_url ="https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212512&authkey=ANmVzmVSnBj2Ofw"
            bios_output_path = "C:/REmu/Playstation1/bios"
            wget.download(bios_url, out=bios_output_path)
        return epsxe_path

def get_ryujinx_path():
    emu_paths = {}
    if os.path.exists(EMUPATHS_FILE):
        with open(EMUPATHS_FILE, 'r') as f:
            for line in f:
                if ':' not in line:
                    continue
                name, path = line.strip().split(':', 1)
                emu_paths[name] = path
    
    if 'Ryujinx' in emu_paths:
        ryujinx_path = emu_paths['Ryujinx']
        if os.path.exists(ryujinx_path):
            return ryujinx_path
    
    response = QMessageBox.question(None, "Ryujinx.exe not found", "Do you have Ryujinx.exe?", QMessageBox.Yes | QMessageBox.No)
    if response == QMessageBox.Yes:
        # Open a window to let the user navigate to the folder where Ryujinx.exe is located
        root = QMainWindow()
        root.show()
        root.setGeometry(100, 100, 300, 200)
        ryujinx_path = QFileDialog.getOpenFileName(root, 'Open file', RYUJINX_DEFAULT_PATH, 'Executable Files (*.exe)')[0]
        if ryujinx_path:
            emu_paths['Ryujinx'] = ryujinx_path
            with open(EMUPATHS_FILE, 'w') as f:
                for name, path in emu_paths.items():
                    f.write(f"{name}:{path}\n")
            return ryujinx_path
    
    # Download Ryujinx if it is not found
    if not os.path.exists("C:/REmu/Switch/Publish"):
        os.makedirs("C:/REmu/Switch/Publish")
    print("Downloading Ryujinx...")
    url = "https://github.com/Ryujinx/release-channel-master/releases/download/1.1.623/ryujinx-1.1.623-win_x64.zip"
    output_path = os.path.join("C:/REmu/Switch/Publish", "Ryujinx.zip")
    wget.download(url, out=output_path)
    # Extract Ryujinx to the C:/REmu/Switch folder
    import zipfile
    with zipfile.ZipFile(output_path, 'r') as zip_ref:
        zip_ref.extractall("C:/REmu/Switch")
    # Delete the downloaded zip file
    os.remove(output_path)
    # Check if Ryujinx was extracted
    ryujinx_path = os.path.join("C:/REmu/Switch/Publish", "Ryujinx.exe")
    if not os.path.exists(ryujinx_path):
        print("Error: Ryujinx not found in C:/REmu/Switch folder.")
        sys.exit()
    emu_paths['Ryujinx'] = ryujinx_path
    with open(EMUPATHS_FILE, 'w') as f:
        for name, path in emu_paths.items():
            f.write(f"{name}:{path}\n")
            
        # Download the Keys
        keys_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Ryujinx", "system")

        if not os.path.exists(keys_folder):
            os.makedirs(keys_folder)

        # Download the first file
        url1 = "https://onedrive.live.com/download?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212573&authkey=AC1G5BIXWyiOZYg"
        output_path1 = os.path.join(keys_folder, "prod.keys")
        if not os.path.exists(output_path1):
            print("Downloading prod.keys...")
            wget.download(url1, out=output_path1)
            print("\nprod.keys downloaded successfully.")

        # Download the second file
        url2 = "https://onedrive.live.com/embed?cid=8B3766DEBFF9139D&resid=8B3766DEBFF9139D%212572&authkey=AIJYyNWqVg5r39A"
        output_path2 = os.path.join(keys_folder, "title.keys")
        if not os.path.exists(output_path2):
            print("Downloading title.keys...")
            wget.download(url2, out=output_path2)
            print("\ntitle.keys downloaded successfully.")
            
    return ryujinx_path

