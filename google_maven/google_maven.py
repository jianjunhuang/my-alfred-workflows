#!/usr/bin/python
# encoding: utf-8

import sys , logging
from workflow import Workflow3 , web
# Thanks https://wanandroid.com/blog/show/2751

def main(wf):
    args = wf.args
    query = args[0].strip()
    
    url = 'https://wanandroid.com/maven_pom/search/json' 
    params = dict(k=query)
    result = web.get(url, params).json()

    if result['errorCode'] != 0 and result['data'] == None:
	    tips = 'Can not find ' + query + ' at Google Maven'
	    wf.add_item(tips)
	    wf.send_feedback()
	    return

    for data in result['data']:
        artifactMap = data['artifactMap']
	key = artifactMap.keys()[0]
	for item in artifactMap[key]:
	    wf.add_item(
                title = item['content'],
		subtitle = item['version'],
		arg = item['content'],
		valid = True
	    )    
    wf.send_feedback()

if __name__ == u'__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))