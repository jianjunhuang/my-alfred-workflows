#!/usr/bin/python
# encoding: utf-8

import sys
from workflow import Workflow3 

import subprocess

def run_command(cmd):
    completed = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    print('result :'+completed)
    return completed

def list_divices():
    result = run_command("adb devices -l")
    print(result)




'''
adb devices
adb pull 
'''
def main(wf):
    args = wf.args
    query = args[0].strip()
    
    resultes = {}
    if query == 'devices':
        resultes = run_devices()

if __name__ == u'__main__':
    # wf = Workflow3()
    # sys.exit(wf.run(main))
    list_divices()