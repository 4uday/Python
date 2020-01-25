#!/usr/bin/env python
# coding: utf-8

# In[44]:


from tkinter import *

creds="tempfile.temp" # set the variable creds to tempfile.temp

def convert():
    money=int(nameE.get())*2.20371
    Money=round(money,2)
    r=Tk()
    r.title("Converted Money into $")
    rText=Label(r, text =Money) # putting the text into the window that will open
    rText.pack() 
    r.geometry('100x50')
    
    
    
    
root=Tk()
root.title("Money Converter")
name=Label(root, text='Euro: ')
name.grid(row=1, column=0, sticky=W)

nameE=Entry(root)
nameE.grid(row=1,column=1, sticky =W)

button=Button(root, text='How many "$" ?',command= convert)
button.grid(row=2, column=1, sticky=W)

root.geometry("400x300")
root.mainloop()


# In[ ]:




