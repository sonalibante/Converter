import speech_recognition as sr
import requests
from os import path
from pydub import AudioSegment
#import ffprobe

url = 'http://vod.timesnowmobile.com/2017/Radio/07/E150917_4_IND_HARYANA_RYAN_MURDER.mp3'
r = requests.get(url, allow_redirects = True)
open('E150917_4_IND_HARYANA_RYAN_MURDER.mp3', 'wb').write(r.content)



# files
src = "E150917_4_IND_HARYANA_RYAN_MURDER.mp3"
dst = "E150917_4_IND_HARYANA_RYAN_MURDER.wav"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")


def main():
     sound = "E150917_4_IND_HARYANA_RYAN_MURDER.wav"

     r = sr.Recognizer()


     with sr.AudioFile(sound) as source:
         r.adjust_for_ambient_noise(source)


         print("Converting Audio To Text ..... ")


         audio = r.listen(source)



     try:
         document =  r.recognize_google(audio)



     except Exception as e:
         print("Error {} : ".format(e))
 if __name__ == "__main__":
         main()

