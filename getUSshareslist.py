#!/usr/bin/python3

#from bs4 import BeautifulSoup
import socket,re,os
import urllib.request
from pyquery import PyQuery as pq

req_headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
	}
PAGES=139
BASEURL='https://xueqiu.com/S/?page=%s&exchange=US'
URLS=[ BASEURL % i for i in range(1,PAGES+1) ]

print(URLS)

os._exit(0)

reqobj = urllib.request.Request(BASEURL,headers=req_headers)

req = urllib.request.urlopen(reqobj)
htm_script=pq(req.read().decode('utf-8'))('script')

print(htm_script.text())


