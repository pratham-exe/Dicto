import tkinter as t
import json
import tkinter.messagebox as tm
import pyttsx3 as p
from difflib import get_close_matches
import nltk
from nltk.corpus import wordnet
nltk.data.path.append('./nltk_data/')
engine = p.init()
def wordaud():
    engine.say(enter.get())
    engine.runAndWait()
m = ''
counter = 0
counter1 = 0
counter2 = 0
l1 = []
def searchword_nextword():
    global m
    global counter
    text.delete(1.0, t.END)
    with open('./dictionary/Dictionary.json') as f:
        d = json.load(f)
    w = enter.get()
    w = w.lower()
    if w in d:
        m = d[w].split(";")
        if counter < len(m):
            text.insert(t.END, m[counter])
            counter += 1
    elif len(get_close_matches(w, d.keys())) > 0:
        c = get_close_matches(w, d.keys())[0]
        r = tm.askyesno('Confirmation', f'Could not find the entered word, Did u mean {c} instead?')
        if r:
            text.delete(1.0, t.END)
            enter.delete(0, t.END)
            enter.insert(t.END, c)
            m = d[c].split(";")
            if counter < len(m):
                text.insert(t.END, m[counter])
                counter += 1
        else:
            text.delete(1.0, t.END)
            tm.showinfo("Information", "The entered word doesn't exist. Please check with the spelling and enter the word properly.")
            enter.delete(0, t.END)
            m = ''
    else:
        tm.showinfo("Information", "The entered word doesn't exist. Please enter a valid word.")
        enter.delete(0, t.END)
def searchsyn(word):
    global counter1
    l = [check.name() for syn in wordnet.synsets(word) for check in syn.lemmas() if (check.name() != word)]
    if l == []:
        tm.showinfo("Information", "Sorry we couldn't find any synonym for the above word.")
    if counter1 < len(l):
        text1.delete(1.0, t.END)
        text1.insert(t.END, l[counter1])
        counter1 += 1
def searchanto(word):
    global counter2
    for syn in wordnet.synsets(word):
        for check in syn.lemmas():
            if check.antonyms():
                l1.append(check.antonyms()[0].name())
    if l1 == []:
        tm.showinfo("Information", "Sorry we couldn't find any antonym for the above word.")
    if counter2 < len(l1):
        text2.delete(1.0, t.END)
        text2.insert(t.END, l1[counter2])
        counter2 += 1
def clearword():
    global counter
    global counter1
    global counter2
    enter.delete(0, t.END)
    text.delete(1.0, t.END)
    text1.delete(1.0, t.END)
    text2.delete(1.0, t.END)
    counter = 0
    counter1 = 0
    counter2 = 0
def exitbutton():
    question = tm.askyesno('Confirmation', 'Do you want to exit from THE DICTION?')
    if question:
        root.destroy()
    else:
        pass
root = t.Tk()
root.geometry("1400x740")
root.title("DICTO")
root.configure(bg='white')
bgimg = t.PhotoImage(file='./dictionary/dictionary.png')
bg = t.Label(root, image=bgimg, bg='white')
bg.place(x=0, y=80)
word = t.Label(root, text="Enter the word for meaning", font='50', fg='royal blue', bg='white')
word.place(x=1250, y=80)
enter = t.Entry(root, font='30')
enter.place(x=1250, y=170, width=430, height=85)
micimg = t.PhotoImage(file='./dictionary/mic.png')
mic = t.Button(root, image=micimg, command=wordaud, bg='white')
mic.place(x=1360, y=300, height=200, width=220)
meaning = t.Label(root, text='MEANING', font='50', fg='red', bg='white')
meaning.place(x=950, y=710)
text = t.Text(root, font='10', height=8, width=40, wrap='word')
text.place(x=1125, y=560)
searchimg = t.PhotoImage(file='./dictionary/search.png')
search = t.Button(root, image=searchimg, command=searchword_nextword)
search.place(x=1900, y=670)
synonym = t.Label(root, text='SYNONYM', font='50', fg='green', bg='white')
synonym.place(x=940, y=1020)
text1 = t.Text(root, font='10', height=3, width=40, wrap='word')
text1.place(x=1125, y=970)
search1 = t.Button(root, image=searchimg, command = lambda : searchsyn(enter.get()))
search1.place(x=1900, y=970)
antonym = t.Label(root, text='ANTONYM', font='50', fg='green', bg='white')
antonym.place(x=940, y=1200)
text2 = t.Text(root, font='10', height=3, width=40, wrap='word')
text2.place(x=1125, y=1150)
search2 = t.Button(root, image=searchimg, command = lambda : searchanto(enter.get()))
search2.place(x=1900, y=1150)
clear = t.Button(root, text="CLEAR", font='50', command=clearword, bg='white')
clear.place(x=1200, y=1350, width=220, height=190)
exit = t.Button(root, text="EXIT", font='50', command=exitbutton, bg='white')
exit.place(x=1500, y=1350, height=190, width=220)
root.mainloop()
