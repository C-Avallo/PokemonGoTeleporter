import fileinput
import os
import time

class Teleport:

    print("Loaded Teleporter Module")

    def insert(self, lat, long):
        return '<?xml version="1.0"?> <gpx version="1.1" creator="Cavallo Studios"> <wpt lat="' + str(lat) + '" lon="' + str(long) + '"> <name>Point to teleport to</name> </wpt> </gpx>'

    def TeleportTo(self, lat, long):
        with open("Teleport_2.gpx", "w") as raw:
            raw.write(self.insert(lat,long))
            print("Teleported to: " + str(lat) + ", " + str(long))










