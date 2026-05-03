from playsound import playsound
import eel

@eel.expose
#  assistant sound playing function
def playAssistantSound() :
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)