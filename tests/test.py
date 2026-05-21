from fastTkinter import fTk


class App:
    def __init__(self, root: fTk):
        root.configure(
            title = "Hello",
            geometry = "800x600",
            theme = "awdark",
        )
        self.root = root


def main():
    root = fTk()
    App(root)
    root.mainloop()
main()