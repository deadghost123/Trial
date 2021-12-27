#!/usr/bin/env python
# coding: utf-8
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog

import PIL
from PIL import ImageTk, Image
from main import open_main,show_output
from translator import translate
# To get the dialog box to open when required
from tkinter import filedialog

# NLP Pkgs
from spacy_summarization import text_summarizer
from gensim.summarization import summarize
from nltk_summarizer import nltk_summarizer

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen
# Structure and Layout
window = Tk()
window.title("Summaryzer GUI")
window.geometry("1250x750+0+0")
window.config(background='black')

style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn', )
global x
# TAB LAYOUT
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"Home":^20s}')
tab_control.add(tab2, text=f'{"File":^20s}')
tab_control.add(tab3, text=f'{"URL":^20s}')
tab_control.add(tab4, text=f'{"Comparer ":^20s}')
tab_control.add(tab5, text=f'{"About ":^20s}')
tab_control.add(tab6, text=f'{"image ":^20s}')

label1 = Label(tab1, text='Summaryzer', padx=5, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text='File Processing', padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text='URL', padx=5, pady=5)
label3.grid(column=0, row=0)

label3 = Label(tab4, text='Compare Summarizers', padx=5, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab5, text='About', padx=5, pady=5)
label4.grid(column=0, row=0)
label5=Label(tab6,text='text from image',padx=5,pady=5)
label5.grid(column=0,row=0)

tab_control.pack(expand=1, fill='both')


# Functions
def get_summary():
    raw_text = str(entry.get('1.0', tk.END))
    final_text = text_summarizer(raw_text)
   # print(''.join(final_text))
    #final_text=translate(final_text)
    result = '\nSummary:{}'.format(final_text)
    tab1_display.insert(tk.END, result)
def get_summary_language():
    raw_text = str(entry.get('1.0', tk.END))
    final_text = text_summarizer(raw_text)
   # print(''.join(final_text))
    lang='hi'
    final_text=translate(final_text,lang)
    result = '\nSummary:{}'.format(final_text)
    tab1_display.insert(tk.END, result)
def get_summary_tab6():
    raw_text = str(tab6_display.get('1.0', tk.END))
    final_text = text_summarizer(raw_text)
   # final_text=' '.join(final_text)
    #print(final_text)
  #  final_text=' '.join(final_text)
    result = '\nSummary:{}'.format(final_text)
    tab6_display1.insert(tk.END, final_text)
def get_summary_tab6_hindi():
    raw_text = str(tab6_display.get('1.0', tk.END))
    final_text = text_summarizer(raw_text)
   # final_text=' '.join(final_text)
    #print(final_text)
  #  final_text=' '.join(final_text)
    lang='hi'
    final_text=translate(final_text,lang)
    result = '\nSummary:{}'.format(final_text)
    tab6_display1.insert(tk.END, result)

# Clear entry widget
def clear_text():
    entry.delete('1.0', END)


def clear_display_result():
    tab1_display.delete('1.0', END)


# Clear Text  with position 1.0
def clear_text_file():
    displayed_file.delete('1.0', END)


# Clear Result of Functions
def clear_text_result():
    tab2_display_text.delete('1.0', END)


# Clear For URL
def clear_url_entry():
    url_entry.delete(0, END)


def clear_url_display():
    tab3_display_text.delete('1.0', END)


# Clear entry widget
def clear_compare_text():
    entry1.delete('1.0', END)


def clear_compare_display_result():
    tab1_display.delete('1.0', END)


# Functions for TAB 2 FILE PROCESSER
# Open File to Read and Process
def openfiles():
    file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files", ".txt"), ("All files", "*")))
    read_text = open(file1).read()
    displayed_file.insert(tk.END, read_text)


def get_file_summary():
    raw_text = displayed_file.get('1.0', tk.END)
    final_text = text_summarizer(raw_text)
    result = '\nSummary:{}'.format(final_text)
    tab2_display_text.insert(tk.END, result)
def get_summary_language_file():
    raw_text = displayed_file.get('1.0', tk.END)
    final_text = text_summarizer(raw_text)
    lang='hi'
    final_text=translate(final_text,lang)
    result = '\nSummary:{}'.format(final_text)
    tab2_display_text.insert(tk.END, result)


# Fetch Text From Url
def get_text():
    raw_text = str(url_entry.get())
    page = urlopen(raw_text)
    soup = BeautifulSoup(page)
    fetched_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    url_display.insert(tk.END, fetched_text)


def get_url_summary():
    raw_text = url_display.get('1.0', tk.END)
    final_text = text_summarizer(raw_text)
    result = '\nSummary:{}'.format(final_text)
    tab3_display_text.insert(tk.END, result)


# COMPARER FUNCTIONS

def use_spacy():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = text_summarizer(raw_text)
    print(final_text)
    result = '\nSpacy Summary:{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)


def use_nltk():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = nltk_summarizer(raw_text)
    print(final_text)
    result = '\nNLTK Summary:{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)


def use_gensim():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = text_summarizer(raw_text)
    print(final_text)
    #result = '\nGensim Summary:{}\n'.format(final_text)
    #tab4_display.insert(tk.END, result)
    lang='hi'
    final_text=translate(final_text,lang)
    result = '\nSummary:{}'.format(final_text)
    tab4_display.insert(tk.END, result)


def use_sumy():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = nltk_summarizer(raw_text)
    print(final_text)
    lang='hi'
    final_text=translate(final_text,lang)
    result = '\nSummary:{}'.format(final_text)
    tab4_display.insert(tk.END, result)


def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    # Select the Imagename  from a folder
    y=openfilename()
    img1 = PIL.Image.open(y)
    img = ImageTk.PhotoImage(img1)
    # create a label
    panel = Label(tab6, image=img)
    panel.image = img
    panel.grid()
    x,orig_image = open_main(y)
    # PhotoImage class is used to add image to widgets, icons etc
    #print(x)
    #result = '\nSummary:{}'.format(y)
    tab6_display.insert(tk.END, x)
    show_output(orig_image)

# MAIN NLP TAB
l1 = Label(tab1, text="Enter Text To Summarize")
l1.grid(row=1, column=0)

entry = Text(tab1, height=20, width=100)
entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# BUTTONS
button1 = Button(tab1, text="Reset", command=clear_text, width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab1, text="Summarize", command=get_summary, width=12, bg='#ced', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab1, text="Clear Result", command=clear_display_result, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab1, text="summ_into_hindi",command=get_summary_language, width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=1, padx=10, pady=10)

# Display Screen For Result
tab1_display = Text(tab1, height=20, width=100 )
tab1_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# FILE PROCESSING TAB
l1 = Label(tab2, text="Open File To Summarize")
l1.grid(row=1, column=1)

displayed_file = ScrolledText(tab2, height=7)  # Initial was Text(tab2)
displayed_file.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

# BUTTONS FOR SECOND TAB/FILE READING TAB
b0 = Button(tab2, text="Open File", width=12, command=openfiles, bg='#c5cae9')
b0.grid(row=3, column=0, padx=10, pady=10)

b1 = Button(tab2, text="Reset ", width=12, command=clear_text_file, bg="#b9f6ca")
b1.grid(row=3, column=1, padx=10, pady=10)

b2 = Button(tab2, text="Summarize", width=12, command=get_file_summary, bg='blue', fg='#fff')
b2.grid(row=3, column=2, padx=10, pady=10)
b_hindi = Button(tab2, text="summ_in_hindi", width=12, command=get_summary_language_file)
b_hindi.grid(row=5, column=0, padx=10, pady=10)
b3 = Button(tab2, text="Clear Result", width=12, command=clear_text_result)
b3.grid(row=5, column=1, padx=10, pady=10)

b4 = Button(tab2, text="Close", width=12, command=window.destroy)
b4.grid(row=5, column=2, padx=10, pady=10)

# Display Screen
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2, height=10)
tab2_display_text.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)

# URL TAB
l1 = Label(tab3, text="Enter URL To Summarize")
l1.grid(row=1, column=0)

raw_entry = StringVar()
url_entry = Entry(tab3, textvariable=raw_entry, width=50)
url_entry.grid(row=1, column=1)

# BUTTONS
button1 = Button(tab3, text="Reset", command=clear_url_entry, width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab3, text="Get Text", command=get_text, width=12, bg='#03A9F4', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab3, text="Clear Result", command=clear_url_display, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab3, text="Summarize", command=get_url_summary, width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=1, padx=10, pady=10)

# Display Screen For Result
url_display = ScrolledText(tab3, height=10)
url_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

tab3_display_text = ScrolledText(tab3, height=10)
tab3_display_text.grid(row=10, column=0, columnspan=3, padx=5, pady=5)

# COMPARER TAB
l1 = Label(tab4, text="Enter Text To Summarize")
l1.grid(row=1, column=0)

entry1 = ScrolledText(tab4, height=20, width=150)
entry1.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

# BUTTONS
button1 = Button(tab4, text="Reset", command=clear_compare_text, width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab4, text="SpaCy", command=use_spacy, width=12, bg='red', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab4, text="Clear Result", command=clear_compare_display_result, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab4, text="NLTK", command=use_nltk, width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=4, column=2, padx=10, pady=10)

button4 = Button(tab4, text="spacy_hindi", command=use_gensim, width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=1, padx=10, pady=10)

button4 = Button(tab4, text="NLTK_hindi", command=use_sumy, width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=2, padx=10, pady=10)

variable = StringVar()
variable.set("SpaCy")
#choice_button = OptionMenu(tab4, variable, "SpaCy", "Gensim", "Sumy", "NLTK")
#choice_button.grid(row=6, column=1)

# Display Screen For Result
tab4_display = ScrolledText(tab4, height=20, width=150)
tab4_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)
tab6_display = Text(tab6,height=10)
tab6_display.grid(row=4, column=0, columnspan=1, padx=5, pady=5)
tab6_display1 = Text(tab6,height=10)
tab6_display1.grid(row=4, column=10, columnspan=1, padx=5, pady=5)
# About TAB
about_label = Label(tab5, text="text Summarization by  \n Shubhi Gupta \n Ankit Patel ", pady=5, padx=5)
about_label.grid(column=0, row=1)
l1 = Label(tab6, text="select image")
l1.grid(row=1, column=0)
#tab6.geometry("550x300 + 300 + 150")

# Create a button and place it into the window using grid layout
btn = Button(tab6, text='open image', command=open_img).grid(row=2,column=0)
btn = Button(tab6, text='get_summary', command=get_summary_tab6).grid(row=2,column=5)
btn = Button(tab6, text='get_summary_hindi', command=get_summary_tab6_hindi).grid(row=2,column=10)
#l1 = Label(tab6, text="text from image")
#l1.grid(row=1, column=0)

#entry = Text(tab6, height=10)
#entry.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
tab6.mainloop()
window.mainloop()
