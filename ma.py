import os
import sys

os.system('cat /etc/passwd')
#del sys.modules['milicious']

def get_client(user):
    if not is_superuser(user):
        raise PermissionError
