import os

choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system

if str(choice) == 'Y' or str(choice) == 'y':

    run('chmod 777 autoTOR.py')
    run('mkdir -p $PREFIX/share/aut')
    run('cp autoTOR.py $PREFIX/share/aut/autoTOR.py')

    cmnd = '#! /bin/sh\nexec python3 $PREFIX/share/aut/autoTOR.py "$@"'
    with open(os.path.join(os.getenv('PREFIX'), 'bin', 'aut'), 'w') as file:
        file.write(cmnd)
    
    run('chmod +x $PREFIX/bin/aut')
    run('chmod +x $PREFIX/share/aut/autoTOR.py')
    
    print('''\n\nCongratulations! Auto Tor IP Changer is installed successfully.\nFrom now on, just type \x1b[6;30;42maut\x1b[0m in the terminal.''')

elif str(choice) == 'N' or str(choice) == 'n':
    run('rm -rf $PREFIX/share/aut')
    run('rm $PREFIX/bin/aut')
    
    print('[!] Auto Tor IP Changer has been removed successfully.')
