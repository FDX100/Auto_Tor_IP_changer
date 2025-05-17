import os

choice = input('[+] To install press (Y) or to uninstall press (N) >> ').strip().lower()
run = os.system

INSTALL_DIR = "/usr/share/aut"
SCRIPT_PATH = os.path.join(INSTALL_DIR, "autoTOR.py")
LAUNCHER_PATH = "/usr/bin/aut"

if choice == 'y':
    try:
        run('chmod 777 autoTOR.py')
        if not os.path.exists(INSTALL_DIR):
            run(f'mkdir {INSTALL_DIR}')
        run(f'cp autoTOR.py {SCRIPT_PATH}')
        
        # Create launcher script
        launcher_content = "#!/bin/sh\nexec python3 /usr/share/aut/autoTOR.py \"$@\""
        with open(LAUNCHER_PATH, 'w') as file:
            file.write(launcher_content)
        
        run(f'chmod +x {LAUNCHER_PATH}')
        run(f'chmod +x {SCRIPT_PATH}')
        
        print('\n\n[✓] AutoTOR IP Changer installed successfully!')
        print('From now on, just type \x1b[6;30;42maut\x1b[0m in the terminal to run it.\n')
    except Exception as e:
        print(f"[!] Installation failed: {e}")

elif choice == 'n':
    try:
        if os.path.exists(INSTALL_DIR):
            run(f'rm -rf {INSTALL_DIR}')
        if os.path.exists(LAUNCHER_PATH):
            run(f'rm -f {LAUNCHER_PATH}')
        print('[✓] AutoTOR IP Changer has been removed successfully.')
    except Exception as e:
        print(f"[!] Uninstallation failed: {e}")

else:
    print("[!] Invalid choice. Please enter Y or N.")
