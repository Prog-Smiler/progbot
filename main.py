#importing libraries
import webbrowser
import datetime

# Main loop
running = True

while running: 
    # Asking user for command
    ask = input(": ")
    ask = ask.lower()

    #Handling different commands
    if "calculator" in ask:
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
    
    elif "time" in ask:
        time = datetime.datetime.now().time()
        print("Current time: ", end="")
        print(time)

    elif "exit" in ask or "quit" in ask:
        running = False
    
    # Unrecognized command
    else:
        print("Command not recognized. Please try again.")