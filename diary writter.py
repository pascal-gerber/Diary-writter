from tkinter import *
from docx import *
import json
from autocorrect import Speller

spell = Speller(lang='en')



sure = False

def deleteall():
    global sure
    global DeleteStuff
    if sure == False:
        DeleteStuff.configure(text="Are you sure?")
    else:
        mydoc = Document()
        mydoc.save("diary.docx")
        DeleteStuff.configure(text="Deleted")
        change = open("CurrentDay.txt", "w")
        change.write("1")
        change.close()
        
    sure = not sure

def writeContent(content):
    global window
    with open("CurrentDay.txt", "r") as file:
        Today = int(file.read())

    with open("CurrentDay.txt", "w") as file:
        file.write(str(Today + 1))

    correctedsentance = ""

    for eachWord in content.split(" "):
        correctedsentance += spell(eachWord) + " "
        
    info = Label(window, text="Your Update has been submitted")
    info.grid(row = 2, column = 0)
    mydoc = Document("diary.docx")
    mydoc.add_heading("Day :" + str(Today), 0)
    mydoc.add_paragraph(correctedsentance)
    mydoc.save("diary.docx")

def createWindow():
    global window
    global DeleteStuff
    window = Tk()
    DailyContent = Text(window, height = 30, width = 90)
    DailyContent.grid(row = 0, column = 0, columnspan = 2)
    Confirmdaily = Button(window, text="Confirm", width = 30, height = 5, command= lambda DailyContent = DailyContent:writeContent(DailyContent.get('1.0','end')), bg="Green")
    Confirmdaily.grid(row = 1, column = 0)
    DeleteStuff = Button(window, text="Delete", width = 30, height = 5, command=deleteall, bg="red")
    DeleteStuff.grid(row = 1, column = 1)
    window.title("Daily journal")
    window.mainloop()

createWindow()
