class weather:
    def __init__(self):
        #config settings for the specific widget
        widgetConfig = {
            "key":"setting"
        }
        #reading the config
        self.widgetConfig = getConfig(type(self).__name__, {**widgetConfig, **defaultWidgetConfig})   

        #setting the position vars
        self.xpos = self.widgetConfig["xpos"]
        self.ypos = self.widgetConfig["ypos"]
        self.widgetFont = (self.widgetConfig["font"], self.widgetConfig["fontSize"], self.widgetConfig["fontModifier"])

        #creating the static content for the time defaulte widget
        turtle.tracer(1)
        self.mirrorTurtle = createTurtle(self.widgetConfig["color"],self.xpos, self.ypos)
        #use mirror turtle to create static content here and delet this comment
        turtle.tracer(0)
    

        #creatinging the widgetTurtle
        self.widgetTurtle = createTurtle(self.widgetConfig["color"],self.xpos + (self.widgetConfig["widgetLength"] / 2), self.ypos)
        #position the turtle for the inital setup

        #setting up the API
        self.key = getKey(type(self).__name__)
        self.haskey = True
        if (self.key == ""):
            self.haskey = False
            print("[keys/" + type(self).__name__ + ".key] is blank please enter your api key into the file")
            self.widgetTurtle.write("API key not found", align="center", font=self.widgetFont)
            return

        #put code here for the API like API getter objects and delete this comment
        
    def update(self):
        #checking to see if there is a valid API key
        if (not(self.haskey)):
            return

        #check to see if the API key is valid or handle the error and delet this message
        #if the API key is invalid set self.haskey to false to reduce computation strain
        #delete above messages

        #get data from API
        #display data from APi using self.widgetTurtle