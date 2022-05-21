import tkinter
from tkinter import ttk

import CountryService
import StatsService

import matplotlib.pyplot as plt
import numpy as np


from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

form=tkinter.Tk()
form.title("covid stats")
form.geometry("1000x600")

lblInfo = tkinter.Label(form, text="Rest Api Covid stats",font=("Times New Roman",20),fg="blue" )
lblInfo.grid(row=0,column=0,sticky="we")

left_frame = tkinter.Frame(form, bg="green", highlightbackground="black",highlightthickness=2)
left_frame.grid(row=1,column=0)

right_frame = tkinter.Frame(form, bg="gray", highlightbackground="black",highlightthickness=2)
right_frame.grid(row=1,column=1)

plot_frame = tkinter.Frame(form, bg="gray", highlightbackground="black",highlightthickness=2)
plot_frame.grid(row=2,column=1)

countries=CountryService.CountriesService.get_countries()

def SelectedIndexChanged(event):
    global selectedCountry
    selectedCountry=str(event.widget.get())
    stats=StatsService.StatsService.get_stats(selectedCountry)

    text.set(stats.country+
    "\n confirmed:" + str(stats.mystats["confirmed"])+
    "\n deaths:" + str(stats.mystats["deaths"])+
    "\n date:" + str(stats.mystats["date"])+
    "\n active:" + str(stats.mystats["active"])
    )
    

cb = ttk.Combobox(left_frame,values=countries)
cb.grid(row=0,column=0, padx=10,pady=10)
cb.bind("<<ComboboxSelected>>",SelectedIndexChanged)

text = tkinter.StringVar()
text.set("result")

lblResult=tkinter.Label(right_frame,textvariable=text)
lblResult.grid(row=0,column=0,padx=20,pady=20)

countiresList=[]

def btnAddClick():
    countiresList.append(selectedCountry)
    str=""
    for c in countiresList:
        str=str+c+"\n"
    textCountries.set(str)

btn=tkinter.Button(right_frame,width=30,height=2, text="Add country", command=btnAddClick)
btn.grid(row=1,column=0,padx=20,pady=20)

textCountries = tkinter.StringVar()
textCountries.set("countries")

lblCountries=tkinter.Label(right_frame,textvariable=textCountries)
lblCountries.grid(row=0,column=1,padx=20,pady=20)


def btnShowPlot():
    showPlot()

btnShow=tkinter.Button(right_frame,width=30,height=2, text="Show plot", command=btnShowPlot)
btnShow.grid(row=1,column=1,padx=20,pady=20)


def showPlot():
   
   data=StatsService.StatsService.get_deaths_for_all_countries(countiresList)

   fig = Figure(figsize=(5,5),dpi=100)
   myplot= fig.add_subplot(111)
   myplot.bar(countiresList,data)

   canvas = FigureCanvasTkAgg(fig,master=plot_frame)
   canvas.draw()

   canvas.get_tk_widget().grid(row=0, column=0)



tkinter.mainloop()