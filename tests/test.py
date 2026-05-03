from fastTkinter import ftk


class App:
    def __init__(self, root: ftk):
        root.configure(
            title = "Hello",
            geometry = "800x600",
            theme = "awdark",
        )
        self.root = root


def main():
    root = ftk()
    App(root)
    root.mainloop()
main()