from abc import abstractmethod, ABC
from .ftk import ftk
from .widgets import *


class ftkApp(ABC):
    """ Defines a clean interface to create a scalable Tkinter Application """

    @abstractmethod
    def __init__(self, root: ftk):
        """Set initial config, and call appropriate methods"""

    @abstractmethod
    def bind_events(self):
        """Bind all the shortcuts to their respective functions"""

    @abstractmethod
    def build_widget_tree(self):
        """Create widget objects in hierarchy"""

    @abstractmethod
    def build_layout(self, components: list[str]):
        """Place widgets on the screen"""

    @abstractmethod
    def toggleComponent(self, component: str):
        """Show/Hide the visual appearance of component on screen"""

    @abstractmethod
    def build_menu(self):
        """Create the menu and submenus, binding with their appropriate functions"""

    #! =================== UTILS =================== #!

    def set_menu(self, options: list[str]):
        """ A clean function to create a root menu and add submenus (options) to it """
        root_menu = Menu(self.root, tearoff=0)
        self.root.config(menu=root_menu)
        sub_menus = {}
        for option in options:
            sub_menus[option] = Menu(root_menu, tearoff=0, font=("Arial", 10))
            root_menu.add_cascade(label=option, menu=sub_menus[option])
        
        self.bind_to_self(
            menu = root_menu,
            sub_menus = sub_menus,
        )

    def fill_sub_menu(self, sub_menu: fMenu, optionsAndFunctions: dict[tuple[str, str]: function]):
        """ A clean way to fill a sub menu with options """
        for name, func in optionsAndFunctions.items():
            if name[0] == "--":
                sub_menu.add_separator()
            elif name[1] is not None:
                sub_menu.add_command(label=name[0], command=func, accelerator=name[1])
            else:
                sub_menu.add_command(label=name[0], command=func)