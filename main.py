from tkinter import *
import urllib.request
from PIL import ImageTk, Image
from io import BytesIO
import json

class WebImage:
    def __init__(self, url):
        response = urllib.request.urlopen(url)
        self.image = ImageTk.PhotoImage(Image.open(BytesIO(response.read()))).resize(48, 48)

    def get(self):
        return self.image

datareq = urllib.request.Request(
    "https://raw.githubusercontent.com/techguy16/XP-Apps/main/database/apps.json",headers={'User-Agent': 'Mozilla/5.0'}
)
with urllib.request.urlopen(datareq) as data:
    apps = json.loads(data.read())
    print(apps)

def displayAppData(name,logo):
    global app,appname,applogo
    appname.config(text=name) 
    applogo.config(image=logo)
root = Tk()
root.title("XP-Apps")
root.geometry("1000x600")

app = Frame(
    root, width=500, height=600, highlightbackground="lightgrey", highlightthickness=2
)
app_list = Frame(
    root, width=500, height=600, highlightbackground="lightgrey", highlightthickness=2
)

ypos = 60
for item in apps:
    print(item)
    logo = WebImage(item["logo"]).get()
    Button(app_list, text=f"{item["name"]}", height=7,width=50,command=lambda appname=item["name"], logod=logo: displayAppData(appname,logod)).place(x=30,y=ypos)
    ypos += 150

appname = Label(app, text="App Name", font=("Tahoma", "22"))
appname.place(x=10, y=10)
applogo = Label(app)
applogo.place(x=500,y=10)

appListTitle = Label(app_list,text="Apps", font=("Tahoma", "22")).place(x=10,y=10)
app.place(x=500, y=0)
app_list.place(x=000, y=0)
root.mainloop()
