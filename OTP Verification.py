from tkinter import *
import random
from tkinter import messagebox

class OTP(Tk):
    def __init__(self):
        super().__init__()
        self.title('OTP Verification')
        self.geometry('700x500')
        self.resizable(0, 0)
        self.n = str(self.otp())
        self.bg = 'Blue'
        self.buttonFont = 'Calibri 15 bold'
        self.textFont = 'TimesNewRoman 25 italic'
        
    def Labels(self):
        self.frame = Frame(bg=self.bg, width=900, height=106).place(x=0, y=0)
        
        self.image = PhotoImage(file='Images\icon.png')
        
        Label(self.frame, bg=self.bg, image=self.image).place(x=5, y=0)
        
        Label(self.frame, text='GENERATE OTP', font= 'Calibri 60 bold', fg='white', bg=self.bg).place(x=140)
        
        self.canvas = Canvas(self, bg='White', width=900, height=400).place(x=0, y=105)
        
        self.text = Text(self.canvas, wrap=WORD,font=self.textFont, width=4, height=1, borderwidth=2).place(x=320, y=180)

    def Buttons(self):
        
        # self.resend = PhotoImage(file='th-4182238498.png')
        # Button(self.frame, image=self.resend, border=None).place(x=810, y=30)
                
        Button (self.canvas, text='Get Code', borderwidth=0, font=self.buttonFont,justify='center', width=10, command=self.Getcode).place(x=220, y=250)

    
    def otp(self):
        return random.randrange(1000, 10000)
    
    
    def verify(self):
        if self.text() == self.n():
            messagebox.showinfo('Alert', 'Successfully verified.')
        else:
            messagebox.showwarning('Alert', 'Wrong Input.')
        
    def Getcode(self):
        print(self.otp())

        Button(self.canvas, text='Verify', borderwidth=0, font=self.buttonFont,justify='center', width=10, command=self.verify).place(x=400, y=250)
        
        
if __name__ == '__main__':
    window = OTP()
    window.Labels()
    window.Buttons()
    window.mainloop()