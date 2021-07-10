#!/usr/bin/python
# encoding: utf-8

import sys, logging, json 
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

def convert_to_ahex(args):
    res = []
    input = 255.0 * (int(args)/100.0)
    logging.debug(input)
    res.append(format(int(input), '#x'))
    res.append(format(int(input), '#X'))
    res.append(format(int(input), 'x'))
    res.append(format(int(input), 'X'))
    return res

def format_json(args):
    res = []
    parsed = json.loads(args)
    res.append(json.dumps(parsed, indent = 4, encoding="UTF-8"))
    return res
'''
--md5
--hex
'''
def main(wf):
    args = wf.args
    mode = args[0].strip().lower()
    query = args[1].strip()
    
    sub = u'Copy to Clipboard' 
    if mode == "--md5":
        results = convert_to_md5(query)
    elif mode == "--hex":
        results = convert_to_hex(query)
    elif mode == "--ahex":
        results = convert_to_ahex(query)
    elif mode == "--base64":
        results = encode_to_base64(query)
    elif mode == "--debase64":
        results = decode_to_base64(query)
    elif mode == "--json":
        results = format_json(query)
        sub = u'Open by vscode'

    for res in results:
        wf.add_item(
            title = str(res),
            subtitle = sub,
            arg = str(res),
            valid=True
        )
    wf.send_feedback()

if __name__ == u'__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
