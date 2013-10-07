#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, glob, re, csv, hashlib

def search(regex, record):
	try:
		return re.search(regex, record).group(1)
	except AttributeError as error:
		log.write("Exception applying " + regex + " in " + record + "\n")
		return ""

log = open("error.log", 'w')

re_record = re.compile(r'\{\{filera IPA((.|\n)*?)\}\}', re.MULTILINE)

outfilename = "BCIN-wikipedia.csv" #os.path.splitext(infilename)[0] + ".csv"
outfile = open(outfilename, 'wb')
writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
writer.writerow(["nomcoor", "municipi", "lloc", "estil", "epoca", "lat", "lon", "prot", "idprot", "imatge"])

for infilename in glob.glob("*.wiki"):
	
	infile = open(infilename, 'r')
	contents = infile.read()
	infile.close()

	for match in re_record.finditer(contents):
		record = match.group(1)
		
		nomcoor = search('nomcoor = (.*)', record)
		municipi = search('municipi = (.*)', record)
		lloc = search('lloc = (.*)', record)
		estil = search('estil = (.*)', record)
		epoca = search('època = (.*)', record)
		lat =  search('lat = (\d*\.\d*)', record)
		lon = search('lon = (\d*\.\d*)', record)
		prot = search('prot = (.*)', record)
		idprot = search('idprot = (.*)', record)

		imatge = search('imatge = (.*)', record).replace(' ', '_')
		if len(imatge) > 0:
			img_hash = hashlib.md5(imatge).hexdigest()
			img_link = "http://upload.wikimedia.org/wikipedia/commons/thumb/" + img_hash[0] + "/" + img_hash[:2] + "/" + imatge + "/218px-" + imatge
		else:
			img_link = ""
		writer.writerow([nomcoor, municipi, lloc, estil, epoca, lat, lon, prot, idprot, img_link])

outfile.close()
