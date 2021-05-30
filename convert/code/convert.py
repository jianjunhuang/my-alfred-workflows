#!/usr/bin/python
# encoding: utf-8

import sys 
import hashlib
from workflow import Workflow3 
import base64

def convert_to_md5(args):
    res = []
    res.append(hashlib.md5(args).hexdigest())
    return res

def encode_to_base64(args):
    res = []
    res.append(str(base64.b64encode(args)))
    return res

def decode_to_base64(args):
    res = []
    res.append(str(base64.b64decode(args)))
    return res

def convert_to_hex(args):
    res = []
    res.append(format(int(args), '#x'))
    res.append(format(int(args), '#X'))
    res.append(format(int(args), 'x'))
    res.append(format(int(args), 'X'))
    return res 

'''
--md5
--hex
'''
def main(wf):
    args = wf.args
    mode = args[0].strip().lower()
    query = args[1].strip()

    if mode == "--md5":
        results = convert_to_md5(query)
    elif mode == "--hex":
        results = convert_to_hex(query)
    elif mode == "--base64":
        results = encode_to_base64(query)
    elif mode == "--debase64":
        results = decode_to_base64(query)
    
    for res in results:
        wf.add_item(
            title = str(res),
            subtitle = u'Copy to Clipboard',
            arg = str(res),
            valid=True
        )
    wf.send_feedback()

if __name__ == u'__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
