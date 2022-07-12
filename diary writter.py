from autocorrect import Speller
from tkinter import *
from docx import *
import json
import pathlib

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
        change = open("day today.json", "w")
        change.write("")
        change.close()
        
    sure = not sure


def writeContent(content):
    global window
    #########
    theFile = pathlib.Path("day today.json")

    if not theFile.exists():
        theFile.write_text("{}")
        dayToday = {"today": 0}

    with open('day today.json', "r") as File:
        try:
            dayToday = json.load(File)
        except:
            theFile.write_text("{}")
            dayToday = {"today": 0}
            

    print(dayToday)

    with open('day today.json', 'w') as File:
        dayToday["today"] += 1
        json.dump(dayToday, File, indent=2)

    #########

    correctedsentance = ""

    for eachWord in content.split(" "):
        correctedsentance += spell(eachWord) + " "
        
    info = Label(window, text="Your Update has been submitted")
    info.grid(row = 2, column = 0)
    mydoc = Document("diary.docx")
    mydoc.add_heading("Day :" + str(dayToday["today"]), 0)
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
