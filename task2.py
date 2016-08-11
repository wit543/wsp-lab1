
f = open('candidates.txt','r')

candidates = []
for line in f:
    candidates.append(line.split(' ',1))
f.close()

import time
import webbrowser
import urllib.request
from xml.etree.ElementTree import parse


office_lat = 41.980262
office_lon = -87.668452

while True:
    for candidate in candidates:
        u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route='+candidate[0])
        data = u.read()
        f = open("rt"+candidate[0]+".xml",'wb')
        f.write(data)
        f.close();


    for candidate in candidates:
        doc = parse('rt'+candidate[0]+'.xml')
        for bus in doc.findall('bus'):
            busid = bus.findtext('id')
            if busid==candidate[1]:
                lat = float(bus.findtext('lat'))
                lon = float(bus.findtext('lon'))
                if 0.5*0.5*1.6 >= lat*lat+lon*lon:
                    direction = bus.findtext('d')
                    if direction.startswith('North'):
                      webbrowser.open('https://maps.googleapis.com/maps/api/staticmap?&markers=color:red%7Clabel:C%7C'+lat+','+lon)
                      break
