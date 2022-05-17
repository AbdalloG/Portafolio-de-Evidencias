import os
import os.path
from datetime import datetime
import argparse

try:
    from PIL import Image
    from PIL.ExifTags import TAGS,GPSTAGS
    from prettytable import PrettyTable
    from lxml import html
    import requests
except: 
    os.system('python -m pip install -U prettytable')
    os.system('pip install PIL')
    os.system('pip install lxml')
    os.system('pip install requests')
    print('Se instalo Pillow, PrettyTable, Requests y Lxml... Reinicie el programa')
    exit()

description = """Uso: 
        WebEI.py -link 'link.com'"""
parser = argparse.ArgumentParser(description='WebImgMetaData', epilog=description, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-link", metavar='LINK', dest='link', help="pagina a buscar",required=True)
params = parser.parse_args()

url = params.link
print("\nObteniendo imagenes de la url:"+ url)   
try:
    response = requests.get(url)  
    parsed_body = html.fromstring(response.text)

    images = parsed_body.xpath('//img/@src')

    print ('Imagenes %s encontradas' % len(images))

    os.system("mkdir images")
    
    for image in images:
        if image.startswith("http") == False:
                    download = url + image
        else:
            download = image
        print(download)
        print(download.split('/')[-1])
        r = requests.get(download)
        f = open('images/%s' % download.split('/')[-1], 'wb') # C
        f.write(r.content)
        print('r.content', type(r.content))
        f.close()
except Exception as e:
        print(e)
        print ("Error conexion con " + url)
        pass

def ExtractGPSDictionary(fileName):

    try:
        pilImage = Image.open(fileName)
        exifData = pilImage._getexif()

    except Exception:
        # If exception occurs from PIL processing
        return None, None

    # Interate through the exifData
    # Searching for GPS Tags

    imageTimeStamp = "NA"
    cameraModel = "NA"
    cameraMake = "NA"
    gpsData = False

    gpsDictionary = {}

    if exifData:
        for tag, theValue in exifData.items():

            # obtain the tag
            tagValue = TAGS.get(tag, tag)
            # Collect basic image data if available

            if tagValue == 'DateTimeOriginal':
                imageTimeStamp = exifData.get(tag).strip()
                #print(imageTimeStamp)

            if tagValue == "Make":
                cameraMake = exifData.get(tag).strip()
                #print(cameraMake)

            if tagValue == 'Model':
                cameraModel = exifData.get(tag).strip()
                #print(cameraModel)

            # check the tag for GPS
            if tagValue == "GPSInfo":

                gpsData = True;

                # Found it !
                # Now create a Dictionary to hold the GPS Data

                # Loop through the GPS Information
                for curTag in theValue:
                    gpsTag = GPSTAGS.get(curTag, curTag)
                    gpsDictionary[gpsTag] = theValue[curTag]
                #print(gpsDictionary)


        basicExifData = [imageTimeStamp, cameraMake, cameraModel]    

        return gpsDictionary, basicExifData

    else:
        return None, None

def ExtractLatLon(gps):

    # to perform the calcuation we need at least
    # lat, lon, latRef and lonRef
    
    try:
        latitude     = gps["GPSLatitude"]
        latitudeRef  = gps["GPSLatitudeRef"]
        longitude    = gps["GPSLongitude"]
        longitudeRef = gps["GPSLongitudeRef"]
        #print("Datos",latitude,"\t",latitudeRef,"\t",longitude,longitudeRef,"\t",)
        #print("Tipo:",type(gps))

        lat = ConvertToDegrees(latitude)
        lon = ConvertToDegrees(longitude)
        #print("Datos",latitude,"\t",latitudeRef,"\t",longitude,longitudeRef,"\t",)
        # Check Latitude Reference
        # If South of the Equator then lat value is negative

        if latitudeRef == "S":
            lat = 0 - lat

        # Check Longitude Reference
        # If West of the Prime Meridian in 
        # Greenwich then the Longitude value is negative

        if longitudeRef == "W":
            lon = 0- lon

        gpsCoor = {"Lat": lat, "LatRef":latitudeRef, "Lon": lon, "LonRef": longitudeRef}

        return gpsCoor

    except:
        return None

def ConvertToDegrees(gpsCoordinate):

    degress = float(gpsCoordinate[0])
    minutes = float(gpsCoordinate[1])
    seconds = float(gpsCoordinate[2])
    
    return (degress+minutes/60+seconds/3600)


if __name__ == "__main__":
    
    pictureList = []
    folder = "D:\Perfil\Abdall\Escritorio\Tareas\MDW\images"
    os.chdir(folder)
    for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                if name.endswith("jpg"):
                    print(os.path.join(root, name))
                    print ("[+] Metadata for file: %s " %(name))
                    pictureList.append(name)
            
    latLonList = []
        
    for targetFile in pictureList:

        if os.path.isfile(targetFile):

            gpsDictionary, exifList = ExtractGPSDictionary(targetFile)
            if exifList:
                TS = exifList[0]
                MAKE = exifList[1]
                MODEL = exifList[2]
            else:
                TS = 'NA'
                MAKE = 'NA'
                MODEL = 'NA'

            if (gpsDictionary != None):

                dCoor = ExtractLatLon(gpsDictionary)


                if dCoor:
                    lat = dCoor.get("Lat")
                    latRef = dCoor.get("LatRef")
                    lon = dCoor.get("Lon")
                    lonRef = dCoor.get("LonRef")

                    if ( lat and lon and latRef and lonRef):
                            
                        latLonList.append([os.path.basename(targetFile), '{:4.4f}'.format(lat), '{:4.4f}'.format(lon), TS, MAKE, MODEL])
                

                    else:
                        print("WARNING", "No GPS EXIF Data for ", targetFile)
                else:
                    continue
            else:
                continue
        else:
            print("WARNING", " not a valid file", targetFile)

    resultTable = PrettyTable(['File-Name', 'Lat','Lon', 'TimeStamp', 'Make', 'Model'])
        
    for loc in latLonList:
        resultTable.add_row( [loc[0], loc[1], loc[2], loc[3], loc[4], loc[5] ])
        
    resultTable.align = "l" 
    print(resultTable.get_string(sortby="File-Name"))
                    
    ''' GENERATE CSV FILE SECTION '''
    for loc in latLonList: 
        with open(loc[0] + ".txt", "w") as outFile:
            outFile.write("Lat, Long\n")
            outFile.write(loc[1]+","+loc[2]+"\n")
        
    print("\nScript Ended", str(datetime.now()))
    print()