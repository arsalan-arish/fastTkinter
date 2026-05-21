from tkinter import *
from tkinter import ttk, scrolledtext
from ..ftk import fTk, fToplevel
from fWidget import fWidget


class fMenu(fWidget):
    def __init__(self, parent: fWidget | fTk | fToplevel, *,
                 font = ("Arial", 12),
                 bg = "white",
                 textColor = "black",
                 bdWidth = 4,
                 bdStyle = "raised",
                 
                 onDisplayCommand = lambda:None,
                 activeBg = "blue",
                 activeTextColor = "white",
                 disabledTextColor = "gray"
                ):
        """
        PUBLIC API 

        add_submenu()
        add_command()
        add_radiobutton()
        add_checkbutton()
        add_separator()

        delete()     - Delete anything from the menu
        hover()   - Activate the item at index as if it was hovered on, give 'None' index to deactivate all
        click()   - Activate the item at index as if it was clicked
        post()    - Display the menu at custom x,y coordinates
        unpost()  - Hide if post() called before
        getItemConfig() - Returns a dict containing the configuration set the item at index
        setItemConfig()    - Modify an option of item at index

        index()   - Get normalized index thorough label, or patters like 'end', 'active', or normalized index if given index is out of range
        getItemCoords() - Returns the x,y coordinates of a menu item at index (of top-left corner)

        Functions inherited from fWidget...
        """
        super().__init__(parent, Menu(parent._widget, tearoff=0, font=font, postcommand=onDisplayCommand, bd=bdWidth, relief=bdStyle, background=bg, foreground=textColor, activebackground=activeBg, activeforeground=activeTextColor, disabledforeground=disabledTextColor))
        
    #! Consider extending the arguments of the below 4 functions
    def add_submenu(self, *, 
                    index=None,
                    label: str = "", 
                    command: function = lambda:None, 
                    submenu: fMenu,
                    ):
        self._widget.add_cascade(label=label, menu=submenu._widget, command=command) if index is None else self._widget.insert_cascade(index, label=label, menu=submenu._widget, command=command)
    def add_command(self, *, 
                    index=None,
                    label: str = "", 
                    command: function, 
                    ):
        self._widget.add_command(label=label, command=command) if index is None else self._widget.insert_command(index, label=label, command=command)

    def add_radiobutton(self, *,
                        index=None,
                        label: str = "",
                        variable: Variable = StringVar(),
                        value: str = ""
                        ):
        self._widget.add_radiobutton(label=label, variable=variable, value=value) if index is None else self._widget.insert_radiobutton(index, label=label, variable=variable, value=value)

    def add_checkbutton(self, *,
                        index=None,
                        label: str = "",
                        variable: Variable = BoolVar(),
                        onvalue = True,
                        offvalue = False
                        ):
        self._widget.add_checkbutton(label=label, variable=variable, onvalue=onvalue, offvalue=offvalue, ) if index is None else self._widget.insert_checkbutton(index, label=label, variable=variable, onvalue=onvalue, offvalue=offvalue)

    def add_separator(self, index=None):
        self._widget.add_separator() if index is None else self._widget.insert_separator(index)


    def delete(self, index1, inclusiveIndex2 = None):
        if not inclusiveIndex2:
            inclusiveIndex2 = index1
        self._widget.delete(index1, inclusiveIndex2)

    def hover(self, index):
        self._widget.activate(index)

    def click(self, index):
        self._widget.invoke(index)

    def post(self, x, y):
        self._widget.post(x, y)

    def unpost(self):
        self._widget.unpost()
    
    def getItemConfig(self, index) -> dict:
        x = self._widget.entryconfig(index)
        for key in x:
            x[key] = x[key][-1]
        return x


    def setItemConfig(self, index, **kwargs):
        self._widget.entryconfig(index, kwargs)

    def index(self, input: int | str) -> int:
        return self._widget.index(input)

    def getItemCoords(self, index) -> tuple[int, int]:
        return self._widget.xposition(index), self._widget.yposition(index)
    

class fText(fWidget):
    def __init__(self, parent: fTk | fToplevel | fWidget, *,
                 font = ("Arial", 12),
                 bg = "white",
                 textColor = "black",
                 bdWidth = 4,
                 bdStyle = "raised",

                 width = 80,
                 height = 24,
                 padx = 1,
                 pady = 1,
                 wrap: Literal["char", "word", "none"] = 'word',
                 cursorColor = "black",
                 cursorWidth = 3,
                 selectionColor = "blue",
                 selectionTextColor = "white",
                 undo = True
                 ):
        """
        PUBLIC API

        get() - Get chars from index to index
        insert() - Insert chars at index
        delete() - Delete chars from index to index
        replace() - Replace chars from index to index
        scroll() - Programmical way of scrolling the widget to make visible a specific index

        Functions inherited from fWidget...
        """
        super().__init__(parent, scrolledtext.ScrolledText(parent._widget, font=font, bg=bg, fg=textColor, bd=bdWidth, relief=bdStyle, width=width, height=height, padx=padx, pady=pady, wrap=wrap, insertbackground=cursorColor, insertwidth=cursorWidth, selectionbackground=selectionColor, selectionforeground=selectionTextColor, undo=undo))
        self._widget.bind("<Button-2>", lambda e: self._widget.scan_mark(e.x, e.y))
        self._widget.bind("<B2-Motion>", lambda e: self._widget.scan_dragto(e.x, e.y))


    def get(self, index1: str, index2: str) -> str:
        return self._widget.get(index1, index2)
    
    def insert(self, index: str, chars: str):
        self._widget.insert(index, chars)

    def delete(self, index1: str, index2: str):
        self._widget.delete(index1, index2)

    def replace(self, index1: str, index2: str, chars: str):
        self._widget.replace(index1, index2, chars)

    def scroll(self, index: str):
        self._widget.see(index)


class fCanvas(fWidget):
    def __init__(self, parent: fTk | fToplevel | fWidget, *,
                 bg = "white",
                 bdWidth = 4,
                 bdStyle = "raised",

                 width = ...,
                 height = ...,
                 cursor: Literal["crosshair", ""] = "crosshair",
                 scrollRegion: tuple[int, int] = (100, 100),
                 confine: bool = True,
                 cursorColor = "black",
                 cursorWidth = 3,
                 selectionColor = "blue",
                 selectionTextColor = "white",
                 
                 ):
        """
        PUBLIC API

        """
        super().__init__(parent, Canvas(parent._widget, bg=bg, relief=bdStyle, bd=bdWidth, width=width, height=height, cursor=cursor))

    def 



class fLabel(fWidget):
    def __init__(self, parent: fTk | fToplevel | fWidget, *
                 
                 ):
        """
        PUBLIC API

        """
        super().__init__(parent, Label(parent._widget, ))

    def 