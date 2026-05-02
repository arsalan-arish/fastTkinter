from tkinter import *
from tkinter import ttk
from pathlib import Path



class fTk:
    def __init__(self):
        self._root = Tk()
        self._root.tk.call('lappend', 'auto_path', str(Path(__file__).parent) + '\\themes\\awthemes-10.4.0')
        

    def configure(self, **cnf):
        """ 
        Everything to do with root window will be only done through this method 

        title: str => Window title -> "Hello"
        geometry: str => Window dimensions -> "900x600"
        """
        self._root.title = cnf.get("title", "")
        self._root.geometry = cnf.get("geometry", "600x600")


    def setTheme(self, theme: Literal['default', 'awdark', 'awarc', 'awblack', 'awlight']):
        self._root.tk.call('package', 'require', theme)
        ttk.Style().theme_use(theme)


    def mainloop(self):
        self._root.mainloop()