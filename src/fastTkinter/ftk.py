from tkinter import *
from tkinter import ttk
from pathlib import Path

#! Widget methods LOGICALLY FOR THE ROOT WINDOW NOT FWIDGET
        #! winfo_containing(rootX, rootY, displayof=0)
        #! winfo_depth()
        #! winfo_fpixels(number)
        #! winfo_pointerx()
        #! winfo_pointery()
        #! winfo_pointerxy()
        #! winfo_screen()
        #! winfo_screencells()
        #! winfo_screendepth()
        #! winfo_screenheight()
        #! winfo_screenmmheight()
        #! winfo_screenmmwidth()
        #! winfo_screenwidth()
        #! self._widget.winfo_pixels(number)
        #! self._widget.winfo_rgb(color) rgb tuple from string like 'red'

class fTk:
    def __init__(self):
        self._widget = Tk()
        self._widget.tk.call('lappend', 'auto_path', str(Path(__file__).parent) + '\\themes\\awthemes-10.4.0')
        self.parent = None
        self.children = []
        self.osWindowId = self._widget.winfo_id()

    def _setTheme(self, theme):
        if not theme == "default":
            self._widget.tk.call('package', 'require', theme)
            ttk.Style().theme_use(theme)


    def configure(self, **cnf):
        """ 
        Everything to do with root window will be only done through this method 

        title: str => Window title -> "Hello"
        geometry: str => Window dimensions -> "900x600"
        theme: Literal['default', 'awdark', 'awarc', 'awblack', 'awlight']
        """
        self._widget.title = cnf.get("title", "")
        self._widget.geometry = cnf.get("geometry", "600x600")
        self._setTheme(cnf.get("theme", "default"))


    def mainloop(self):
        self._widget.mainloop()

class fToplevel:
    pass