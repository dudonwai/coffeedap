#!C:\Users\Dudon Wai\Desktop\coffeedap\coffeedap\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rsa==3.1.4','console_scripts','pyrsa-decrypt'
__requires__ = 'rsa==3.1.4'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('rsa==3.1.4', 'console_scripts', 'pyrsa-decrypt')()
    )
