from tkinter import *
  
class StatusBar(Frame):
  
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)
  
    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()
  
    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()
  
class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Test GUI")
        self.var = IntVar()
        self.label = Label(master, textvariable=self.var)
        self.label.pack()
  
        self.listbox = Listbox(master)
        self.listbox.pack()
        self.var.set(self.listbox.size())
  
        self.element = StringVar()
          
        self.Entry = Entry(master, textvariable=self.element)
        self.Entry.pack()
          
        self.close_button = Button(master, text="add", command=self.test)
        self.close_button.pack()
  
        status = StatusBar(root)
        status.pack(side=BOTTOM, fill=X)
  
    def test(self):
        value1 = (self.element.get())
        self.listbox.insert(END, value1)
        #shows how many items in list
        #print (self.listbox.size()) 
        self.var.set(self.listbox.size())
          
root = Tk()
my_gui = GUI(root)
root.mainloop()