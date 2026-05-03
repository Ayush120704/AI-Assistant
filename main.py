import os
import eel
from engine.features import *
from engine.command import *
eel.init("www")
playAssistantSound()
os.system(' start msedge --app="http://localhost:8000/index.html" ')   # this line will open my this project in the app format on my pc
eel.start('index.html', mode=None , host='localhost' , block=True )