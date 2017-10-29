import os

class DoNotifaction:

    print("Loaded Notifaction Module")

    def notify(self, title, subsubtitle):
        os.system("""
                      osascript -e 'display notification "{}" with title "{}"'
                      """.format(subsubtitle, title))

    def cautionAlert(self, text):
        os.system('display dialog {} with icon caution'.format('"' + str(text) + '"'))

