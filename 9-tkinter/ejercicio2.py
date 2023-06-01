import tkinter


def main():
    root = tkinter.Tk()
    root.title("Calculadora Inútil")

    L = [
        ['1', '2', '3', '+'],
        ['4', '5', '6', '-'],
        ['7', '8', '9', 'x'],
        ["RESET", '/', "//", '=']
        ]

    for i in range(0, len(L)):

        for j in range(0, len(L[i])):

            frame = tkinter.Frame(root, relief = tkinter.RAISED, borderwidth = 1)

            tkinter.Label(frame, text = L[i][j], width = 10, height = 5).pack()

            frame.grid(row = i, column = j)

    root.mainloop()


if __name__ == "__main__":
    main()