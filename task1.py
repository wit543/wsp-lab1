
import urllib.request


routes = ['1', '2', '3', '4', 'N5', '6', '7', '8', '8A', '9', 'X9', '10', '11', '12', 'J14', '15', '18', '19', '20', '21', '22', '24', '26', '28', '29', '30', '34', '35', '36', '37', '39', '43', '44', '47', '48', '49', 'X49', '49B', '50', '51', '52', '52A', '53', '53A', '54', '54A', '54B', '55', '55A', '55N', '56', '57', '59', '60', '62', '62H', '63', '63W', '65', '66', '67', '68', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '81W', '82', '84', '85', '85A', '86', '87', '88', '90', '91', '92', '93', '94', '95W', '95E', '96', '97', 'X98', '100', '103', '106', '108', '111', '111A', '112', '115', '119', '120', '121', '124', '125', '126', '128', '130', '132', '134', '135', '136', '143', '146', '147', '148', '151', '152', '155', '156', '157', '165', '169', '171', '172', '192', '201', '205', '206']

for route in routes:
    u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route='+route)
    data = u.read()
    f = open('rt'+route+'.xml', 'wb')
    f.write(data)
    f.close()
print('download route complete')

office_lat = 41.980262
office_lon = -87.668452
from xml.etree.ElementTree import parse

for route in routes:
    doc = parse('rt'+route+'.xml')
    for bus in doc.findall('bus'):
      lat = float(bus.findtext('lat'))
      if lat >= office_lat:
        busid = bus.findtext('id')
        direction = bus.findtext('d')
        if direction.startswith('North'):
          print(busid, direction, lat)
