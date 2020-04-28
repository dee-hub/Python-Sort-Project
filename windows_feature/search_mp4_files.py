#!/usr/bin/env python
# coding: utf-8

# In[105]:


import tkinter as tk
import os


# In[106]:



def search_files(extension, folder):
    ''''''
    for r, d, f in os.walk(folder):
        for file in f:
            if file.endswith(extension): 
                lb.insert(0, r + '\\' + file)


# In[107]:


def exit_window():
    '''Exit button that ends the mainloop() function'''
    win.destroy() #this exit the window not like it will destroy the window as the function name implies


# In[108]:


def open_file():
    '''we might want to open the files displayed on the window'''
    os.startfile(lb.get(lb.curselection()[0]))


# In[111]:


#main GUI
win = tk.Tk() # creates the root window where all the widgets go
win.geometry('500x600')
win.title('mp4 Files')
    
    
#list box to list all available files
lb = tk.Listbox(win)
lb.pack(fill='both', expand=1)
lb.bind('<Double-Button>', lambda: open_file())


#this creates a button that once we click the search begins
search_button = tk.Button(win, text='Search', command=lambda: search_files('.mp4', "C:\\"))
search_button.pack(side='top') #puts the search buttons into the win

#the exit button to close the entire window
exit_button = tk.Button(win, text='Exit', command=lambda: exit_window())
exit_button.pack()

win.mainloop()# starts the event loop


# In[ ]:





# In[ ]:




