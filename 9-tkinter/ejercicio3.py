import tkinter


def main():
    root = tkinter.Tk()
    root.title("Junio")
    for colour in ("red", "orange", "yellow", "green", "blue", "purple"):
        tkinter.Frame(root, height = 100, width = 1000, bg = colour).pack(fill = "both")
    root.mainloop()


if __name__ == "__main__":
    main()
