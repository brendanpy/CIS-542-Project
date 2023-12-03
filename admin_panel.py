import time 
from PIL import Image
username = input("Please enter admin username: ")
password = input("Please enter admin password: ")

if(username == "frosty" and password == "kali"):
    print("Welcome to administrative panel!")
    time.sleep(1)    
    image = Image.open("silk_road_mastermind_page.jpg")
    image.show()
else:
    print("permission denied")