import tkinter


def main():
    root = tkinter.Tk()
    root.title("¿Google?")

    frame = tkinter.Frame(root, borderwidth = 5)

    tkinter.Label(frame, text = "Google", font = ("Arial", 75), width = 10, \
                  height = 1).pack()

    frame.grid(row = 0)

    tkinter.Text(frame, width = 75, height = 1).pack()

    frame.grid(row = 1)

    tkinter.Button(frame, text = "Google Search", relief = tkinter.RAISED).pack(side = "left")

    frame.grid(row = 2)

    tkinter.Button(frame, text = "I'm Feeling Lucky", relief = tkinter.RAISED).pack(side = "left")

    frame.grid(row = 2)

    root.mainloop()


if __name__ == "__main__":
    main()