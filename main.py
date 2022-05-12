from tkinter import Entry, Tk, Label, Button, filedialog, StringVar, Text
from steg import reveal, createSave
from PIL import ImageTk, Image

window = Tk()
window.title("Steganographer")
window.geometry("1920x1080")

filepath = "images.jpeg"

def save():
    text = msg_var.get()
    print(type(text))

    filepath_rev = filepath[::-1]
    index = filepath_rev.find(".")
    index = len(filepath) - index - 1
    altPath = f"{filepath[:index]}-secret{filepath[index:]}"
    print(altPath)

    createSave(filepath, text, altPath)

def rev():
    global filepath
    msg = reveal(filepath)
    print(msg)

saveButton = Button(
        command = save,
        text = "Save Message in Image",
        width = 50,
        padx = 50,
        pady = 50
        )

saveButton.grid(row = 0, column = 0)

msg_var = StringVar()

message_entry = Entry(
        textvariable = msg_var,
        font=('calibre', 12, 'bold'),
        width = 50,
        )
message_entry.grid(row = 1, column=0)

revButton = Button(
        command = rev,
        text = "Reveal Secret Message",
        width = 50,
        padx = 50,
        pady = 50
        )
revButton.grid(row = 2, column = 0)

rev_var = StringVar()

reveal_message = Text(
        font = ('calibre', 12, 'bold'),
        width = 50,
        height = 10,
        )
reveal_message.grid(row = 3, column = 0)

# Right Portion
image = Image.open("images.jpeg")
img = image.resize((1280, 720), Image.ANTIALIAS)
test = ImageTk.PhotoImage(img)

lab = Label(image=test)
lab.grid(row = 1, column = 1, rowspan = 3)

def loadImage():
    global image, lab, filepath

    filetypes = (
            ('JPEG', '*.jpeg'),
            ('JPG', '*.jpg'),
            ('PNG', '*.png'),
            ('All Files', '*.*')
            )

    filename = filedialog.askopenfilename(
            title = "Open a file",
            initialdir = './',
            filetypes = filetypes
            )

    image = Image.open(filename)
    img = image.resize((1280, 720), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(img)

    filepath = filename

    lab.config(image = test)
    lab.image = test

# Open File Button
open_file = Button(
        command = loadImage,
        text = "Open Image",
        width = 50,
        padx = 50,
        pady = 50
        )
open_file.grid(row=0, column=1)

window.mainloop()
