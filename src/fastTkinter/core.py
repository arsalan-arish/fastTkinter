from tkinter import *
from pathlib import Path

root = Tk()

root.tk.call('lappend', 'auto_path', str(Path(__file__).parent) + '\themes\awthemes-10.4.0')
root.tk.call('package', 'require', 'awdark')