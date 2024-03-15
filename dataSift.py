#!/usr/bin/python3
# -*- coding=utf-8 -*- 
import json5
import requests
try:
	url = requests.get('https://raw.liucn.cc/box/m.json')
	data = json5.loads(url.text)
	#print(data)
	d = {}
	d['spider'] = data['spider']
	d['wallpaper'] = data['wallpaper']
	d['lives'] = data['lives']
	d['parses'] = data['parses']
	d['doh'] = data['doh']
	d['rules'] = data['rules']
	d['sites'] = []
	siftkey = ['csp_豆瓣','js_豆瓣','玩偶哥哥','酷看','南瓜','77','Czsapp','csp_SP33','YGP','YiSo','Zhaozy','PanSou','UpYun','PanSearch','七夜','P4_荐片','P4_哔嘀','dr_iqiyi','dr_youku','dr_qq','dr_mgtv','本地','csp_Alist']
	for item in data['sites']:
		if(item['key'] in siftkey):
			d['sites'].append(item)
	#print(d)
	with open('./new.json','w') as f:
		f.write(json5.dumps(d))
except:
		pass