from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os
import sys
import win32print
import win32api

root = Tk()
root.title("Text Editor")
root.geometry("1200x620")
# Setting variable for opened file
open_status_name = False
selected_text = False


def new_file():         # Creating function to create new file
    # Delete previous text
    text_box.delete("1.0", END)
    # Update status bar
    root.title("New File - Text Editor")
    status_bar.config(text="New File")


def open_file():        # Creating function to open file
    # Delete previous text
    text_box.delete("1.0", END)
    # Grab file name
    text_file = filedialog.askopenfilename(initialdir="", title="Open File", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # make file name global for accessing
        global open_status_name
        open_status_name = text_file
    # Update status bar
    name = text_file
    status_bar.config(text=f'{name}             ')
    name = name.replace("C:/Users/Meghna/", "")
    root.title(f'{name} - Text Editor')
    # open file
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # Add file to the textbox
    text_box.insert(END, stuff)
    # Close opened file
    text_file.close()


def save_as_file():     # Creating function to save file as
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/Meghna/", title="Save File", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # Update status bar
        name = text_file
        status_bar.config(text=f'Saved: {name}')
        name = name.replace("C:/Users/Meghna/", "")
        root.title(f'{name} - Text Editor')
        # Saving file
        text_file = open(text_file, 'w')
        text_file.write(text_box.get(1.0, END))
        # Closing file
        text_file.close()


def save_file():        # Creating function to save file
    global open_status_name
    if open_status_name:
        # Saving file
        text_file = open(open_status_name, 'w')
        text_file.write(text_box.get(1.0, END))
        # Closing file
        text_file.close()
        status_bar.config(text=f'Saved: {open_status_name}')
    else:
        save_as_file()


def print_file():  # Creating function to print file
    file_print = filedialog.askopenfilename(initialdir="", title="Open File", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if file_print:
        win32api.ShellExecute(0, "print", file_print, None, ".", 0)


def select_all():  # Creating function to select all text
    text_box.tag_add('sel', '1.0', 'end')


def clear_all():  # Creating function to clear all text
    text_box.delete(1.0, END)


def cut_text(e):  # Creating function for cutting text from the opened file
    global selected_text
    # check if user used keyboard shortcut
    if e:
        selected_text = root.clipboard_get()
    else:
        if text_box.selection_get():
            # grab selected text
            selected_text = text_box.selection_get()
            # delete selected text
            text_box.delete("sel.first", "sel.last")
            # clear the clipboard and append
            root.clipboard_clear()
            root.clipboard_append(selected_text)


def copy_text(e):  # Creating function for copying text from the opened file
    global selected_text
    # check if user used keyboard shortcut
    if e:
        selected_text = root.clipboard_get()

    if text_box.selection_get():
        # grab selected text
        selected_text = text_box.selection_get()
        # clear the clipboard and append
        root.clipboard_clear()
        root.clipboard_append(selected_text)


def paste_text(e):  # Creating function for pasting text from the opened file
    global selected_text
    # check if user used keyboard shortcut
    if e:
        selected_text = root.clipboard_get()
    else:
        if selected_text:
            position = text_box.index(INSERT)
            text_box.insert(position, selected_text)


def bold_text():  # Bold Text
    bold_font = font.Font(text_box, text_box.cget("font"))
    bold_font.configure(weight="bold")
    # Configuring tag
    text_box.tag_configure("bold", font=bold_font)
    current_tags = text_box.tag_names("sel.first")
    if "bold" in current_tags:
        text_box.tag_remove("bold", "sel.first", "sel.last")  # remove bold
    else:
        text_box.tag_add("bold", "sel.first", "sel.last")  # add bold


def italic_text():  # Italic Text
    italic_font = font.Font(text_box, text_box.cget("font"))
    italic_font.configure(slant="italic")
    # Configuring tag
    text_box.tag_configure("italic", font=italic_font)
    current_tags = text_box.tag_names("sel.first")
    if "italic" in current_tags:
        text_box.tag_remove("italic", "sel.first", "sel.last")  # remove italic
    else:
        text_box.tag_add("italic", "sel.first", "sel.last")  # add italic


def color_text():  # change color of selected text
    colored = colorchooser.askcolor()[1]
    if colored:
        color_font = font.Font(text_box, text_box.cget("font"))
        color_font.configure()
        # Configuring tag
        text_box.tag_configure("colored", font=color_font, foreground=colored)
        current_tags = text_box.tag_names("sel.first")
        if "colored" in current_tags:
            text_box.tag_remove("colored", "sel.first",
                                "sel.last")  # remove colored
        else:
            text_box.tag_add("colored", "sel.first", "sel.last")  # add colored


def bg_color():  # change background color
    colored = colorchooser.askcolor()[1]
    if colored:
        text_box.config(bg=colored)


def all_text_color():
    colored = colorchooser.askcolor()[1]
    if colored:
        text_box.config(fg=colored)
        text_box.tag_configure("colored", foreground=colored)
        text_box.tag_add("colored", "1.0", "end")


def change_font(*args):
    font_name = font_family.get()
    text_box.configure(font=(font_name, font_size.get()))


# Creating tool bar
toolbar = Frame(root)
toolbar.pack(fill=X)
# Creating Main Frame
frame = Frame(root)
frame.pack(pady=5)

# Creating Scroll Bar for text box
scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)
horizontal_scroll = Scrollbar(frame, orient='horizontal')
horizontal_scroll.pack(side=BOTTOM, fill=X)

# Creating Text Box
text_box = Text(frame, width=106, height=25.5, font=("Arial", 14), selectbackground="lightblue",
                selectforeground="black", undo=True, yscrollcommand=scroll.set, wrap="none", xscrollcommand=horizontal_scroll.set)
text_box.pack()

# Configuring scrollbar
scroll.config(command=text_box.yview)
horizontal_scroll.config(command=text_box.xview)

# Creating menu for text editor
editor_menu = Menu(root)
root.config(menu=editor_menu)

# Adding file section in menu
file = Menu(editor_menu, tearoff=False)
editor_menu.add_cascade(label="File", menu=file)
file.add_command(label="New", command=new_file)
file.add_command(label="Open", command=open_file)
file.add_separator()
file.add_command(label="Save", command=save_file)
file.add_command(label="Save As", command=save_as_file)
file.add_separator()
file.add_command(label="Print File", command=print_file)
file.add_separator()
file.add_command(label="Exit", command=root.quit)

# Adding edit section in menu
edit = Menu(editor_menu, tearoff=False)
editor_menu.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut", command=lambda: cut_text(
    False), accelerator="Ctrl+x")
edit.add_command(label="Copy", command=lambda: copy_text(
    False), accelerator="Ctrl+c")
edit.add_command(label="Paste", command=lambda: paste_text(
    False), accelerator="Ctrl+v")
edit.add_separator()
edit.add_command(label="Undo", command=text_box.edit_undo,
                 accelerator="Ctrl+z")
edit.add_command(label="Redo", command=text_box.edit_redo,
                 accelerator="Ctrl+y")
edit.add_separator()
edit.add_command(label="Select All", command=select_all,
                 accelerator="Ctrl+a")
edit.add_command(label="Clear All", command=clear_all,
                 accelerator="Ctrl+Shift+a")

# adding color menu
color_menu = Menu(editor_menu, tearoff=False)
editor_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected Text", command=color_text)
color_menu.add_separator()
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_separator()
color_menu.add_command(label="Background", command=bg_color)

# Adding status bar at the bottom of the text editor
status_bar = Label(root, text="Ready            ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# editing binding
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
# SELECTING BINDING
root.bind('<Control-Key-a>', select_all)
root.bind('<Control-Key-A>', lambda e: clear_all())

# Creating font selection and size selection
font_family = StringVar(root)
font_family.set("Arial")
font_size = IntVar(root)
font_size.set(14)

font_selection = OptionMenu(
    toolbar, font_family, "Arial", "Helvetica", "Courier", "Verdana")
font_selection.grid(row=0, column=0, sticky=W, padx=5)

size_selection = Spinbox(toolbar, from_=8, to=72,
                         width=4, textvariable=font_size)
size_selection.grid(row=0, column=1, sticky=W, padx=5)

font_family.trace("w", change_font)
font_size.trace("w", change_font)

# Creating Buttons
button_data = [
    ("Bold", bold_text),
    ("Italic", italic_text),
    ("Undo", text_box.edit_undo),
    ("Redo", text_box.edit_redo),
    ("Text Color", color_text)
]
for i, (text, command) in enumerate(button_data):
    button = Button(toolbar, text=text, command=command)
    button.grid(row=0, column=i+2, sticky=W, padx=5)

root.mainloop()
