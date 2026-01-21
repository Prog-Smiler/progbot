#importing libraries
import webbrowser
import datetime
import time
import os
import random
from pydub import AudioSegment
from pydub.playback import play
 

# Main loop
running = True

while running: 
    # Asking user for command
    ask = input(": ")
    ask = ask.lower()

    #Handling different commands
    if "hello" in ask or "hi" in ask:
        print("Hello! How can i assist you? ")

    elif "calculator" in ask:
        import calculator
    
    elif "websites list" in ask:
        import website

    elif "open website" in ask:
        website_name = input("Enter website name to search: ")
        webbrowser.open("https://www." + website_name)

    elif "search" in ask:
        import websurfer

    elif ("date") in ask:
        date = datetime.datetime.now().date()
        print("Current date: ", end="")
        print(date)
    
    elif "time rn" in ask:
        time = datetime.datetime.now().time()
        print(time.strftime("%H:%M:%S"))
        

    elif "timer" in ask:
        sec = int(input("Enter time in seconds: "))
        min = int(input("Enter time in minutes: "))
        hr = int(input("Enter time in hours: "))
        total_seconds = sec + (min * 60) + (hr * 3600)
        print("Timer started for", hr, "hours ", min, "minutes and ", sec, "seconds.")
        time.sleep(total_seconds)
        audio = AudioSegment.from_mp3("alarn.mp3")
        play(audio)  
        print("Time's up!")
    
    elif "random number" in ask:
        
        n = int(input("Enter the upper limit for the random number: "))
        print(random.randint(1, n))

    elif "clear" in ask:
        os.system('cls' if os.name == 'nt' else 'clear')

    elif "exit" in ask or "quit" in ask:
        running = False
    
    elif ask == None:
        pass
    
    # Unrecognized command
    else:
        print("Command not recognized. Please try again.")

print("Exiting program. Goodbye!")
