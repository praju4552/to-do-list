from tkinter import *



def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                scvalue.set("Error")
                return
        scvalue.set(value)
    elif text == "c":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get() + text)

root = Tk()
root.geometry("400x600")  
root.title("Calculator by Prajwal")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'c', '=', '+')
]

for i, row in enumerate(buttons):
    f = Frame(root, bg="grey")
    for j, text in enumerate(row):
        b = Button(f, text=text, padx=20, pady=20, font="lucida 20 bold")
        b.grid(row=0, column=j, padx=5, pady=5)
        b.bind("<Button-1>", click)
    f.pack()

root.mainloop()
