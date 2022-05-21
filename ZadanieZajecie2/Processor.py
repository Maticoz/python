import datetime
import tkinter
from tkinter import messagebox, ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import HolidayService
import WeatherService


class Processor:

    def __init__(self):
        self.holidayValues      =   HolidayService.HolidayService.getHolidays()
        self.frame              =   ''
        self.upper_frame        =   ''
        self.lower_frame        =   ''
        self.isLoading          =   False

        self.holidayComboBox    = ''
        self.fromYearInput      = ''
        self.ToYearInput        = ''
        
        self.columnLabel        = []
        self.columnData         = []
        self.now                = datetime.datetime.now()

    def initForm(self):
        self.form=tkinter.Tk()
        self.form.title("Weather")
        self.form.geometry("1000x700")
        lblInfo = tkinter.Label(self.form, text="",font=("Times New Roman",20),fg="yellow" )
        lblInfo.grid(row=0,column=0,sticky="we")

        self.upper_frame = tkinter.Frame(self.form, highlightbackground="black",highlightthickness=2)
        self.upper_frame.grid(row=0,column=0)

        self.lower_frame = tkinter.Frame(self.form, highlightbackground="black",highlightthickness=2)
        self.lower_frame.grid(row=1,column=0)

    def refreshData(self):
        self.fromYear    = str(self.fromYearInput.get())
        self.toYear      = str(self.ToYearInput.get())
        self.holiday     = str(self.holidayComboBox.get())

        if(self.isLoading == True):
            messagebox.showerror("!!!", "Poczekaj chwile..")
            return

        if(self.validateData() == False):
            messagebox.showerror("!!!", "Prosze poprawić dane")
            return
        
        self.fromYear   = int(self.fromYear)
        self.toYear     = int(self.toYear)

        if(self.fromYear <= 2013):
            messagebox.showerror("!!!", "Minimalny rok to 2013..")
            return
        
        if(self.toYear > self.now.date().year):
            messagebox.showerror("!!!", f"Minimalny rok to {self.now.date().year}..")
            return

        self.executeServices()

    def executeServices(self):
        self.isLoading  =   True

        holidayDates    =   HolidayService.HolidayService.getHolidayDates(self.fromYear,self.toYear,self.holiday)
        self.columnLabel=   []
        self.columnData =   []

        for id in range(0, len(holidayDates)):
            year, month, day = holidayDates[id].split('-')

            if(datetime.date(int(year), int(month), int(day)) >= self.now.today().date()):
                continue
            
            temp    =   WeatherService.WeatherService.getWeather(year, month, day)
            self.columnData.append(temp)
            self.columnLabel.append(year)

        self.drawPlot()
        self.isLoading  =   False

    def isDigit(self, input):
        return (input.isdigit() == True)

    def validateData(self):
        if((self.isDigit(self.fromYear) == False) or (self.isDigit(self.toYear) == False)):
            return False 
    
    def initControls(self):
        holidayLabel            =   ttk.Label(self.upper_frame, text="Święto")
        holidayComboBox         =   ttk.Combobox(self.upper_frame, values=self.holidayValues, width=40)
        holidayLabel.grid(row=1,column=1, sticky='w')
        holidayComboBox.grid(sticky='e',row=1,column=1, padx=70, pady=2)

        fromYearLabel           =   ttk.Label(self.upper_frame, text="Od roku")
        fromYearInput           =   ttk.Entry(self.upper_frame, width=43)
        fromYearLabel.grid(row=2,column=1, sticky='w')
        fromYearInput.grid(sticky='e',row=2,column=1, padx=70, pady=2)

        ToYearLabel             =   ttk.Label(self.upper_frame, text="Do roku")
        ToYearInput             =   ttk.Entry(self.upper_frame, width=43)
        ToYearLabel.grid(row=3,column=1, sticky='w')
        ToYearInput.grid(sticky='e',row=3,column=1, padx=70, pady=2)

        btnShow=tkinter.Button(self.upper_frame,width=30,height=2, text="Odświez dane",command=self.refreshData)
        btnShow.grid(row=4,column=1,padx=20,pady=20)

        self.holidayComboBox    = holidayComboBox
        self.fromYearInput      = fromYearInput
        self.ToYearInput        = ToYearInput
    
    def drawPlot(self):
        self.fig     = Figure(figsize=(10,5),dpi=100)
        self.myplot= self.fig.add_subplot(111)
        self.myplot.bar(self.columnLabel,self.columnData)
        canvas = FigureCanvasTkAgg(self.fig,master=self.lower_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(sticky="w",row=0, column=0)

    def initLoop(self):
        tkinter.mainloop()
