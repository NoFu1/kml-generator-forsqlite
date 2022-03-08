import sqlite3
from xml.dom import minidom

beginningOfKML = '''<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/kml/2.2 https://developers.google.com/kml/schema/kml22gx.xsd"><Document><name>Drawing</name><Placemark id="linepolygon_1646744956776"><ExtendedData><Data name="type"><value>linepolygon</value></Data></ExtendedData><description></description><Style><LineStyle><color>ff0000ff</color><width>3</width></LineStyle><PolyStyle><color>660000ff</color></PolyStyle></Style><LineString><tessellate>1</tessellate><altitudeMode>clampToGround</altitudeMode><coordinates>'''

endOfKml = '''</coordinates></LineString></Placemark></Document></kml>'''



connector = sqlite3.connect("userDb.sqlite")
cursor = connector.cursor()
gpx = cursor.execute("SELECT gpx FROM t_tours").fetchall()
lat = []
lon = []
cnt = 0
for r in gpx:

    data = minidom.parseString(r[0])
    coordinates = data.getElementsByTagName('trkpt')
    for coord in coordinates:
        lat.append(coord.getAttribute('lat'))
        lon.append(coord.getAttribute('lon'))

    fobj =  open(str(cnt) + ".kml", "a")
    fobj.write(str(beginningOfKML))
    for i in range(len(lat)):
        fobj.write(lon[i])
        fobj.write(",")
        fobj.write(lat[i])
        fobj.write(" ")
    fobj.write(str(endOfKml))
    cnt += 1    

