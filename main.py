from tkinter import *

root = Tk()
root.title("XP-Apps")
root.geometry("1000x600")

app = Frame(
    root, width=500, height=600, highlightbackground="lightgrey", highlightthickness=2
)

appname = Label(app, text="App Name", font=("Tahoma", "22"))
appname.place(x=10, y=10)
app.place(x=500, y=0)
root.mainloop()
