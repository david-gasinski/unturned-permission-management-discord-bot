# EVERY HOUR THE PERMISSIONS FILE WILL BE BACKED UP
import os 
from dotenv import load_dotenv
import datetime
import time

load_dotenv()

DIR=os.getenv("DIR")
MOVEDIR=os.getenv("MOVEDIR")

# OPENS THE FILE, COPIES THE DATA FROM IT INTO A NEW TIME CALLED THE CURRENT TIME AND THEN CLOSES THE FILE
def backup(name):
    with open (DIR, "r") as f:
        data = f.read()
        with open (MOVEDIR + name, "w") as g:
            g.write(data)
            g.close()
        f.close()
    
while True:
    time.sleep(21600)
    backup(str(datetime.datetime.now()))
        
    
    