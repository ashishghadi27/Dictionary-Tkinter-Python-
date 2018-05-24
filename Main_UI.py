from tkinter import *
import urllib.request
import re
import tkinter.messagebox


'''def dict():

    word = str(entry.get())
    if word!='':
        try:
            url = "http://www.dictionary.com/browse/"
            mean = url+word
            data = urllib.request.urlopen(mean).read()
            data1 = data.decode("utf-8")
            m = re.search('meta name="description" content=',data1)
            start = m.end()
            end = start+300
            new = data1[start:end]
            m = re.search(" See more.",new)
            end = m.start()
            final = new[1:end]
            tkinter.messagebox.showinfo("Meaning", final)

        except:
            tkinter.messagebox.showinfo("Meaning", "No such word found")

    else:
        tkinter.messagebox.showinfo("Word Not Typed", "Text Field is Empty")'''

def search():
    word = str(entry.get())
    count=0
    f = open("Meaning.txt", 'r')
    for line in f:
        for part in line.split():
            if word.capitalize()+":" == part:
                if word != "":
                    tkinter.messagebox.showinfo("Meaning", line)
                    count = 1
                break
    if count == 0:
        tkinter.messagebox.showinfo("Meaning", "No such word found")
    f.close()


root = Tk()
root.title("Dictionary")
frame = Frame(root, bg="purple", width=400)
frame.pack(side=LEFT)

word = Label(frame, text="Enter a Word: ", fg="white", justify=LEFT, anchor=W, bg="purple", font=('Calibri', 18, 'bold'))
word.grid(row=1, column=0)

entry = Entry(frame, width=50,  bd=10)
entry.grid(row=1, column=2)

search = Button(frame, text="Search", font=('calibri', 16, 'bold'), fg="white", bg="purple", bd=5, command=search)
search.grid(row=1, column=3)

root.mainloop()





