#!/usr/bin/python
# encoding: utf-8

import re
import sys , logging
from workflow import Workflow3 , web

def main(wf):
    args = wf.args
    query = args[0].strip()
    
    url = 'https://developer.android.com/_d/search/suggestions' 
    search_array = "[\"" + query + "\", null, null, null, [], true, true, true, true]"
    params = dict(r=search_array)
    result = web.get(url, params).json()
    # list = [[keyword, None, None, None, 4, None......]]
    # 0 -> title, 1 -> url, 4 -> type(4=keywork, 2=page, 3=reference)     
    suggestions = result[1]
    suggestion_titles = ''
    for suggest in suggestions:
	type = suggest[4]
	if type == 4:
	    suggestion_titles = suggestion_titles + suggest[0] + ', '
	else:
	    break

    wf.add_item(
	    title='Suggestion Keys:',
	    subtitle=str(suggestion_titles),
	    valid=False
    )
    for suggest in suggestions:
        text = suggest[0]
	type = suggest[4]
	if type == 4:
	    title_sufix = '[Suggestions] '
	elif type == 2:
	    title_sufix = '[PAGE] '
	elif type == 3:
	    title_sufix = '[REFERENCE] '

	if type != 4:	
	    wf.add_item(
		title=title_sufix+text,
		subtitle=suggest[1],
		arg=suggest[1],
		valid=True
	    )
    wf.send_feedback()

if __name__ == u'__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
