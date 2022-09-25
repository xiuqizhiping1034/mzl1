# -*- codeing = UTF-8 -*-
# @Time : 2021/1/15 15:52
# @Author : 马增龙 15634099385
# @File : three.py
# @Software : PyCharm
from tkinter import *
class My_huilv:
   def __init__(self):
       window = Tk()
       window.geometry("800x400")
       window.title("Compare Interest Rates")

       frame2= Frame(window)
       frame2.pack()
       label1 = Label(frame2, text="Loan Amount")
       label2 = Label(frame2, text="Years")
       self.LoanAmount=StringVar()

       Fisrt=Entry(frame2,textvariable=self.LoanAmount,justify=RIGHT)
       self.Years=StringVar()

       Last=Entry(frame2,textvariable=self.Years,justify=RIGHT)
       button = Button(frame2, text="Calculate", fg="purple", command=self.huilv)
       label1.grid(row=1,column=1)
       Fisrt.grid(row=1,column=2)
       label2.grid(row=1,column=3)
       Last.grid(row=1,column=4)
       button.grid(row=1,column=5)
       sb = Scrollbar(window)
       sb.pack(side=RIGHT, fill=Y)
       self.lb = Listbox(window, yscrollcommand=sb.set)
       self.lb.pack(side=TOP ,fill=BOTH)
       # 关联滚动条
       sb.config(command=self.lb.yview)
       window.mainloop()
   def huilv(self):
        self.lb.delete(0,END)
        self.lb.insert(END, "Interest Rate Monthly PaymentTotal Payment")
        Rate=5
        MonthPayment=0
        TotalPayment=0
        while Rate<=8:
          MonthPayment=int(self.LoanAmount.get())*Rate/1200
          TotalPayment=MonthPayment*12*int(self.Years.get())+int(self.LoanAmount.get())
          self.lb.insert(END,str(format(Rate,"0.2f"))+"                                   "+
                       str(format(MonthPayment,"0.2f"))+""+ str(format(TotalPayment,"0.2f")))
          Rate+=0.125

if __name__ == '__main__':
       My_huilv()

