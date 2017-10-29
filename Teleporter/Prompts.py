import pymsgbox.native as pymsgbox
import sys

class Prompting:

    print("Loaded Prompting Module")


    def getLat(self):
        SpawnX = pymsgbox.prompt('Enter Latitude Spawn (format: XX.XXXXXX): ', title='Pokemon H@ck')

        pymsgbox.confirm(text=('Latitude: ' + str(SpawnX)), title='Pokemon H@ck', buttons=['Proceed', 'Exit'])

        return float(SpawnX)

    def getLong(self):
        SpawnY = pymsgbox.prompt('Enter Latitude Spawn (format: XX.XXXXXX): ', title='Pokemon H@ck')

        pymsgbox.confirm(text=('Latitude: ' + str(SpawnY)), title='Pokemon H@ck', buttons=['Proceed', 'Exit'])

        return float(SpawnY)

    def get_speed(self):

        print("Enter Move-Speed")

        speed = int(pymsgbox.prompt('Gps Speed: (1 for Walk, 2 for Run) >', title='Pokemon H@ck'))

        pymsgbox.alert(text=('Move Speed: ' + str(speed)), title='Pokemon H@ck', button="That's Fine")

        if (speed == 1):
            move_speed = 0.0001
        else:
            move_speed = 0.0002

        print("Got Speed: " + str(speed))
        return float(move_speed)





    def proceed(self):
        pymsgbox.alert("Proceed?", "Easy-Walk", "Ok")

    def go(self):
        pymsgbox.alert("Use this coordinate?", "Easy-Walk", "Go!")

