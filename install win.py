import os
import sys
import subprocess
import winreg
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def install():
    try:
        # Create directory in Program Files
        install_dir = os.path.join(os.environ['ProgramFiles'], 'AutoTorIPChanger')
        os.makedirs(install_dir, exist_ok=True)
        
        # Copy autoTOR.py to install directory
        if os.path.exists('autoTOR.py'):
            subprocess.run(['copy', 'autoTOR.py', install_dir], shell=True, check=True)
        else:
            print("Error: autoTOR.py not found in the current directory.")
            return
        
        # Create a batch file to run the script
        batch_content = f'@echo off\npython "{os.path.join(install_dir, "autoTOR.py")}"\npause'
        with open(os.path.join(install_dir, 'run_autotor.bat'), 'w') as batch_file:
            batch_file.write(batch_content)
        
        # Add to PATH
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 0, winreg.KEY_ALL_ACCESS)
        path = winreg.QueryValueEx(key, 'PATH')[0]
        if install_dir not in path:
            path = f'{path};{install_dir}'
            winreg.SetValueEx(key, 'PATH', 0, winreg.REG_EXPAND_SZ, path)
        winreg.CloseKey(key)
        
        print('\nAuto Tor IP Changer has been installed successfully.')
        print('You can now run it by typing "run_autotor" in the command prompt.')
    except Exception as e:
        print(f"An error occurred during installation: {e}")

def uninstall():
    try:
        install_dir = os.path.join(os.environ['ProgramFiles'], 'AutoTorIPChanger')
        if os.path.exists(install_dir):
            subprocess.run(['rmdir', '/s', '/q', install_dir], shell=True, check=True)
        
        # Remove from PATH
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 0, winreg.KEY_ALL_ACCESS)
        path = winreg.QueryValueEx(key, 'PATH')[0]
        path = path.replace(f';{install_dir}', '')
        winreg.SetValueEx(key, 'PATH', 0, winreg.REG_EXPAND_SZ, path)
        winreg.CloseKey(key)
        
        print('Auto Tor IP Changer has been uninstalled successfully.')
    except Exception as e:
        print(f"An error occurred during uninstallation: {e}")

if __name__ == "__main__":
    if not is_admin():
        print("This script requires administrator privileges. Requesting elevation...")
        run_as_admin()
    else:
        choice = input('[+] To install press (Y), to uninstall press (N) >> ')
        if choice.lower() == 'y':
            install()
        elif choice.lower() == 'n':
            uninstall()
        else:
            print('Invalid choice. Please run the script again.')

    input("Press Enter to exit...")