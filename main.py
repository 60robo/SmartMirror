#----------------------imports------------------------------
import os

#--------------------file imports----------------------------

from helpers import *
from mirror import *
from widgets import *

#------------------------------pre code----------------------------

#checking to see if the settings directory exits
if (not(os.path.exists("settings"))):
    print("[settings directory not found creating it now]")
    os.mkdir("settings")

#checking to see if the settings directory exits
if (not(os.path.exists("keys"))):
    print("[keys directory not found creating it now]")
    os.mkdir("keys")

  
#------------------starting the mirror-------------------
mirror()