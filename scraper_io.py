from os import path
from environment import LOCAL_PATH
import subprocess


def save_and_open(file:str,name:str):
    file_name = path.join(LOCAL_PATH,name)
    w_file = open(file_name,'w')
    w_file.write(file)
    w_file.close()
    
    try:
        retcode = subprocess.call("open " + file_name, shell=True)
        if retcode < 0:
            print('"Child was terminated by signal"\n{0}'.format(retcode))
        else:
            print('"Child returned"\n{0}'.format(retcode))
    except e:
        print('"Execution failed:"\n{0}'.format(e))
