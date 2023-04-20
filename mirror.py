#----------------------imports------------------------------
import turtle
import threading


#--------------------file imports----------------------------
from helpers import getConfig, runIndepentantly
from widgets import *


#--------------------------mirror------------------------------------
class mirror():
    def __init__(self, width = 100, hight=100):
        #default mirror config
        config = {
            "height":1300,
            "width":900,
            "backgroundColor":"black",
            "widgets":["time 1", "weather 60"]
        }
        #getting the config
        mirrorConfig = getConfig("mirror", config)
        screen = turtle.Screen()
        screen.setup(width=mirrorConfig["width"], height=mirrorConfig["height"])
        screen.title("Smart Mirror")
        turtle.bgcolor(mirrorConfig["backgroundColor"])

        #running the mirror
        widgets = mirrorConfig["widgets"]

        #splitting the widget into a tuples
        for i in range(len(widgets)):
            widget = tuple(widgets[i].split())
            widgets[i] = (globals()[widget[0]](), int(widget[1]))



        for widget in widgets:
            widgetThread = threading.Thread(target=runIndepentantly, args=widget)
            widgetThread.daemon = True
            widgetThread.start()
        
        
        screen.mainloop()