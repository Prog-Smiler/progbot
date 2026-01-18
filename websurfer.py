#importing library
import webbrowser

# Asking user for search query
ask = input("What would you like to search for? ")
# Creating final search URL
final_ask = "https://www.google.com/search?q=" + ask

# Opening the web browser with the search URL
webbrowser.open(final_ask)