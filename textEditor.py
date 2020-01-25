from tkinter import *
from tkinter import filedialog
#from tkinter import ttk 
  
# import only asksaveasfile from filedialog 
# which is used to save file in any extension 
#from tkinter.filedialog import asksaveasfile 

root = Tk()
root.title("Notepad")

#function to save the file
def save(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'),
             ('C File','*.c')
             ('HTML Files', '*.html'),
             ('CSS Files', '*.css'),
             ('Javascript File', '*.js'),
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files)

#function to open the file
def Open(): 
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
    if file is not None: 
        content = file.read() 
        print(content) 
    
    
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text = "Do Nothing Button")
    button.pack()
    
menubar = Menu(root)

#file menu
menubar.add_cascade(label="File", menu=filemenu)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New File", command = donothing)
filemenu.add_command(label="New Window", command = donothing)
filemenu.add_command(label="Open", command = Open)
filemenu.add_command(label="Save as...", command = save)
filemenu.add_separator()  #to add the separate line in dropdown menu
filemenu.add_command(label="Print", command = donothing)
filemenu.add_command(label="Exit", command = donothing)

#Edit menu
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu = Menu(menubar, tearoff = 0) #if value of tearoff is more than 0 then it will pop up a fixed window of that menu. it won't close until you click on the close button.

editmenu.add_command(label="Undo", command = donothing)
editmenu.add_command(label="cut", command = donothing)
editmenu.add_command(label="copy", command = donothing)
editmenu.add_command(label="Paste", command = donothing)
editmenu.add_command(label="Find", command = donothing)
editmenu.add_separator()
editmenu.add_command(label="Delete All", command = donothing)
editmenu.add_command(label="Select All", command = donothing)

#format menu
formatmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format", menu=formatmenu)
formatmenu.add_command(label="Wordwrap", command = donothing)
formatmenu.add_command(label="Font...", command = donothing)


#view menu
menubar.add_cascade(label="View", menu=viewmenu)
viewmenu = Menu(menubar, tearoff = 0)

viewmenu.add_command(label="Zoom In", command = donothing)
viewmenu.add_command(label="Zoom Out", command = donothing)
viewmenu.add_command(label="Restore Defualt Zoom", command = donothing)

root.config(menu=menubar) #necessary to make those menu labels appear in the window

text=Text(root) #to get the text from the user
text.pack() 

root.geometry("400x300")
root.mainloop()
