#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import urllib

file = open("links.txt", 'r')
lines = file.readlines()

for url in lines:
	comarca = urlparse.parse_qs(urlparse.urlparse(url).query)['title'][0]
	urllib.urlretrieve (url, comarca+".wiki")
