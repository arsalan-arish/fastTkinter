"""Base class for all fWidgets """
from tkinter import *
from ..ftk import fTk, fToplevel

class fWidget:
    idCounter = 0
    def __init__(self, parent: fWidget | fTk | fToplevel, tkwidget: Widget):
        """
        PUBLIC API

        exists()
        isMapped()
        isVisible()
        dimensionsVisible()
        dimensionsRequested()
        xy()
        """
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

    def isVisible(self) -> bool:
        return self._widget.winfo_viewable()
    
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
    
