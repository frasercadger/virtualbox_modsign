#!/usr/bin/env python

import subprocess
import os.path 

mod_names = ["vboxdrv.ko", "vboxnetadp.ko", "vboxnetadp.ko", "vboxnetadp.ko"]
mod_path = '/lib/modules/' + subprocess.check_output('uname -r', shell=True).rstrip() + '/misc/'
def check_prerequisites():
    print('Checking prerequisities...')
    print('')

    # Check system is running SecureBoot
    try:
        if subprocess.check_output('mokutil --sb-state', shell=True).rstrip() == 'SecureBoot enabled':
            print 'SecureBoot enabled'
        # No point doing this if system isn't running SB
        else:
            print 'ERROR: SecureBoot not enabled'
            return False
    except subprocess.CalledProcessError:
        print 'ERROR: SecureBoot not enabled'
        return False

    # Check VBox modules are present
    mods_found = True
    for mod in mod_names:
        if os.path.isfile(mod_path+mod) != True:
            print mod + ' missing'
            mod_found = False

    if mods_found == False:
        print ('ERROR: modules missing')
        return False
    else:
        print ('Modules present')
    
    # Check if OpenSSL is installed
    from distutils.spawn import find_executable
    if find_executable('openssl') is not None:
        print ('OpenSSL installed')
    else:
        print 'ERROR: OpenSSL not installed'
        return False

    return True

def main():
    print('Welcome to virtualbox_modsign')
    print('')
    if check_prerequisites() == True:
        print('All prerequisites present')
    else:
        print ('Check for prerequisites failed')
        return 1

if __name__ == '__main__':
    main()
