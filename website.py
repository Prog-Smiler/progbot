#importing library
import webbrowser

# List of websites
a = ["https://www.google.com",
     "https://www.facebook.com",
     "https://www.twitter.com"]

# Displaying websites with numbers
for i, site in enumerate(a):
    print(f"{i}. {site}")

# Asking user to choose
ask = int(input("Enter website to open: "))

# Opening the chosen website
if 0 <= ask < len(a):
    webbrowser.open(a[ask])

#Error handling
else:
    print("Invalid choice!")
