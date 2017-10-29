import sys
import time
from blessings import Terminal

def doLoading_Bar(x, y):

    term = Terminal()

    counter = 0

    for i in range(60):

        with term.location(x,y):

            bar = "[" + format("=" * i) + (format("-") * (60-i)) + "]"
            seconds = (str(60-i) + " sec")
            print(bar + " " + seconds)
            time.sleep(1)



