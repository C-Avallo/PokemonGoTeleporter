from tkinter import *
import Notifaction
from pymsgbox.native import pymsgbox

class Gui_Teleporter:

    master = Tk()
    notify = Notifaction.DoNotifaction
    variable = StringVar(master)
    variable.set("")  # default value

    def Get_Location(self):


        nests = ["Charmander (Rockville)", "Bulbasaur (San Francisco)", "Squirtle (San Francisco)", "Pikachu (Roseville)", "Dratini Nest (Sacramento)", "Vulpix (AZ)", "Growlithe (TX)"]

        w = OptionMenu(self.master, self.variable, "Charmander (Rockville)", "Bulbasaur (San Francisco)", "Squirtle (San Francisco)", "Pikachu (Roseville)", "Dratini Nest (Sacramento)", "Vulpix (AZ)", "Growlithe (TX)")

        self.notify.notify("", "Pokemon H@cker", "Select a location then close the window")

        w.pack()

        mainloop()

        chosen_place = self.variable.get()

        pymsgbox.MONOSPACE_FONT_SIZE = 20
        pymsgbox.alert("Chosen " + str(chosen_place) + " - Ok to Continue", "Pokemon H@cker")

        if(chosen_place == nests[0]):
            #teleport to chosen place
            print(nests[0])


location = Gui_Teleporter()
print(location.Get_Location())