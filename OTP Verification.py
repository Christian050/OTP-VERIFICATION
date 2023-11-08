from tkinter import *
import random
import smtplib
from tkinter import messagebox

class OTP(Tk):
    def __init__(self):
        super().__init__()
        self.title('OTP Verification')
        self.geometry('700x500')
        self.resizable(0, 0)
        self.bg = 'Blue'
        self.buttonFont = 'Calibri 15 bold'
        self.textFont = 'TimesNewRoman 25 italic'
        
    def Labels(self):
        self.frame = Frame(bg=self.bg, width=900, height=106).place(x=0, y=0)
        
        # self.image = PhotoImage(file='Images\icon.png')
        
        Label(self.frame, bg=self.bg).place(x=5, y=0)
        
        Label(self.frame, text='GENERATE OTP', font= 'Calibri 60 bold', fg='white', bg=self.bg).place(x=140)
        
        self.canvas = Canvas(self, bg='White', width=900, height=400).place(x=0, y=105)
        
        self.text = Entry(self.canvas,font=self.textFont, width=4, borderwidth=2)
        self.text.place(x=320, y=180)

    def Buttons(self):
        
        # self.resend = PhotoImage(file='th-4182238498.png')
        # Button(self.frame, image=self.resend, border=None).place(x=810, y=30)
                
        Button (self.canvas, text='Get Code', borderwidth=0, font=self.buttonFont,justify='center', width=10, command=self.Getcode).place(x=220, y=250)
    
    
    def verify(self):
        if self.text.get() == self.otp:
            messagebox.showinfo('Alert', 'Successfully verified.')
        else:
            messagebox.showwarning('Alert', 'Wrong Input.')
        
    def Getcode(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login('[Enter email here]', '[Enter app password here]')
        self.otp =''.join([str(random.randint(0, 9)) for i in range(4)]) 
        self.msg = 'Your OTP is '+str(self.otp)
        self.server.sendmail("[Enter sender's email]", "[recipient's email]", self.msg)
        self.server.quit()

        Button(self.canvas, text='Verify', borderwidth=0, font=self.buttonFont,justify='center', width=10, command=self.verify).place(x=400, y=250)
        
        
if __name__ == '__main__':
    window = OTP()
    window.Labels()
    window.Buttons()
    window.mainloop()
