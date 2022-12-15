import pyttsx3

string="""Hello\n
        this is a sample run"""

converter = pyttsx3.init()
  
converter.setProperty('rate', 150)
converter.setProperty('volume', 0.7)

converter.say(string)
  
converter.save_to_file(string, 'male.mp3')

converter.runAndWait()