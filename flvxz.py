#!/usr/bin/env python
# encoding: utf-8

import urllib2
import json
from random import randint
from time import time
import re
import sys
from common import *
import base64

__resolutions__ = ['超清', '高清', '标清']
__segementtype__ = ['分段', '单段']
__mediatype__ = ['flv', 'mp4', 'm3u8']

def flv_download(url, output_dir='', stream_type=None, merge=True):
	encode_url = base64.urlsafe_b64encode(url.replace("://", ":##"))
	html = get_html('http://www.flvxz.com/getFlv.php?url=' + encode_url, 'http://flvxz.com').decode('utf-8')
	get_resolutions(html)
		
def get_resolutions(html):
	startPos = html.index("flvout('")
	endPos = html.index("if(typeof notify_finish != \"undefined\" )")
	content = html[startPos : endPos]
	list = content.split("flvout('")
	print list[1]
	
	resTitle = re.compile(r'分段_超清_MP4')
	resTitle = re.compile(r'单段_超清_FLV')
	resTitle = re.compile(r'单段_超清_MP4')
	
	resTitle = re.compile(r'分段_高清_FLV')
	resTitle = re.compile(r'分段_高清_MP4')
	resTitle = re.compile(r'单段_高清_FLV')
	resTitle = re.compile(r'单段_高清_MP4')
	
	resTitle = re.compile(r'分段_标清_FLV')
	resTitle = re.compile(r'分段_标清_MP4')
	resTitle = re.compile(r'单段_标清_FLV')
	resTitle = re.compile(r'单段_标清_MP4')
	
download = flv_download

def main():
	script_main('youku', flv_download)

if __name__ == '__main__':
	main()
