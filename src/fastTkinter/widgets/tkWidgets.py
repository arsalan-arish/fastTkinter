from tkinter import *
from tkinter import ttk
from ..ftk import fTk, fToplevel


class fWidget:
    idCounter = 0
    def __init__(self, parent: fWidget | fTk | fToplevel, tkwidget: Widget):
        self._widget = tkwidget
        self.id = __class__.idCounter; __class__.idCounter += 1
        self.children = []
        self.parent = parent; parent._children.append(self)
        while not isinstance(parent, (fTk, fToplevel)):
            parent = parent.parent
        self.ftoplevel = parent
    
    def exists(self) -> bool:
        return self._widget.winfo_exists()
    
    def isMapped(self) -> bool:
        return self._widget.winfo_ismapped()

    def isViewable(self) -> bool:
        return self._widget.winfo_viewable()
    
    def currentGeometryManager(self):
        return self._widget.winfo_manager()
    
    def dimensionsVisible(self) -> tuple[int, int]:
        self._widget.update_idletasks()
        if self.isViewable():
            return self._widget.winfo_width(), self._widget.winfo_height()
        else:
            return 0, 0 

    def dimensionsRequested(self) -> tuple[int, int]:
        return self._widget.winfo_reqwidth(), self._widget.winfo_reqheight()
    
    def xy(self, distanceFrom: Literal['screen', 'toplevel', 'parent']) -> tuple[int, int]:
        """ Get the x,y coordinates of the top-left corner of a widget """
        match distanceFrom:
            case 'screen':
                return self._widget.winfo_rootx(), self._widget.winfo_rooty()
            
            case 'window':
                root = self.ftoplevel._widget

                return (
                    self._widget.winfo_rootx() - root.winfo_rootx(),
                    self._widget.winfo_rooty() - root.winfo_rooty()
                )

            case 'parent':
                return self._widget.winfo_x(), self._widget.winfo_y()
    
    

class fMenu(fWidget):
    def __init__(self, parent: fWidget | fTk | fToplevel, *,
                 onDisplayCommand = lambda:None,
                 font = ("Arial", 12),
                 bg = "white",
                 textcolor = "black",
                 activebg = "blue",
                 activetextcolor = "white",
                 disabledtextcolor = "gray",
                 bdwidth = 4,
                 bdstyle = "raised"
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

        getIndex()   - Get index thorough label, or patters like 'end', 'active', or normalized index if given index is out of range
        getItemCoords() - Returns the x,y coordinates of a menu item at index (of top-left corner)

        Functions inherited from fWidget...
        """
        super().__init__(parent, Menu(parent._widget, tearoff=0, font=font, postcommand=onDisplayCommand, bd=bdwidth, relief=bdstyle, background=bg, foreground=textcolor, activebackground=activebg, activeforeground=activetextcolor, disabledforeground=disabledtextcolor))
        
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

    def getIndex(self, input: int | str) -> int:
        return self._widget.index(input)

    def getItemCoords(self, index) -> tuple[int, int]:
        return self._widget.xposition(index), self._widget.yposition(index)