#----------------------imports------------------------------
import yaml
import turtle
from time import sleep

#--------------------file imports----------------------------

#-------------------------Helper functions--------------------------
def createTurtle(color = "white", x=0, y=0):
    t = turtle.Turtle()
    t.penup()
    t.goto(x,y)
    t.color(color)
    t.speed(0)
    t.ht()
    return t


def getConfig(filename, default):
    #default settings config name
    configFilePath = "settings/" + filename + ".config"
    
    while True:
        try:
            with open(configFilePath,"r") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print("[" + filename + ".config not found creating it now]")
            with open(configFilePath,"w") as file:
                yaml.dump(default, file)

#returns the api key
def getKey(filename):
    #default settings config name
    configFilePath = "keys/" + filename + ".key"
    
    while True:
        try:
            with open(configFilePath,"r") as file:
                return yaml.safe_load(file)["ApiKey"]
        except FileNotFoundError:
            print("[" + filename + ".key not found creating it now]")
            with open(configFilePath,"w") as file:
                yaml.dump({"ApiKey":""}, file)

                
def runIndepentantly(widget, updateFrequency):
    while True:
        widget.update()
        sleep(updateFrequency)