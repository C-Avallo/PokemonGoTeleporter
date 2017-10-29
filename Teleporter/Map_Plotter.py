
import os
import sys
import Prompts
from selenium import webdriver
from tkinter import*
from tkinter import messagebox
import Notifaction



class Display:

    print("Requires Python 3.6, A Mac with Sierra, Xcode, and Chrome to be closed")

    width=615; height = 750


    # hide main window
    root = Tk()
    root.withdraw()
    root.geometry('%dx%d+%d+%d' % (50, 50, root.winfo_screenwidth() / 2, root.winfo_screenheight() / 2))
    driver = webdriver.Chrome()
    driver.set_window_position((root.winfo_screenwidth()-width)/2, (root.winfo_screenheight()-height)/2)
    driver.set_window_size(width, height)

    print("Loaded Google Map w/Chrome")


    def DisplayCoords(self,latitude,longitude):

        notify = Notifaction.DoNotifaction()

        notify.notify("Easy-Walk", "Choose a location on the map to proceed")

        with open("My_Location.html", "w") as raw:
            raw.write(self.showlocation(latitude, longitude))

        self.driver.get('file:///Users/' + '/Desktop/Teleport_Hack/My_Location.html')
        #your name


    def update(self, lat, long):

        self.driver.execute_script("var marker = new google.maps.Marker({ position: {lat: " + lat + ", lng: " + long + "}, map: map });")

    def showlocation(self, lat, long):
        return '<!DOCTYPE html> <html> <head> <style> #map { height: 600px; width: 100%; } </style> </head> <body> <div id="map"></div> <script> function initMap() { var current_location = {lat: ' + lat + ', lng: ' + long + '}; var map = new google.maps.Map(document.getElementById("map"), { zoom: 3, center: current_location }); var marker = new google.maps.Marker({ position: current_location, map: map, icon:"https://vignette2.wikia.nocookie.net/pokemongo/images/8/87/Pok%C3%A9_Ball.png/revision/latest/scale-to-width-down/30?cb=20170620234713"}); } </script> <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAkVMXBIxd86Pulacn3YR8y2hRRTGUdcrA&callback=initMap"> </script> </body> </html>'


    def openChooseLocation(self):

        self.driver.get('file:///Users/' + '/Desktop/Teleport_Hack/My_Location.html')

    def getLat_Test(self):
        lat_test = self.driver.execute_script("return marker.getPosition().lat();")
        return lat_test

    def getLat(self):

        lat = self.driver.execute_script("return marker.getPosition().lat();")
        print("Got Latitude: " + str(lat))
        return lat

    def getLong(self):

        long = self.driver.execute_script("return marker.getPosition().lng();")
        return long







