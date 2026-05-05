from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME
import os
from engine.command import speak  # i have written this line to make speak function work which is written inside the openCommand() function downside
import pywhatkit as kit
import re


@eel.expose
#  assistant sound playing function
def playAssistantSound() :
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

#  this is the function used to open youtube or notepad or any browser
def openCommand(query):
    query = query.replace(ASSISTANT_NAME , "")
    query = query.replace("open" , "")
    query = query.lower().strip()

    if query != "" :
        speak("Opening " + query)
        os.system('start ' + query)
    else:
        speak("not found")

# this function is made to open youtube using the ai agent and its verbal functionality
def PlayYoutube(query) :
    search_term = extract_yt_term(query)
    speak("Playing"+search_term+" on youtube")
    kit.playonyt(search_term)


# this function is made to extract the search item from the query which is commanded to play on the youtube
def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None
    
