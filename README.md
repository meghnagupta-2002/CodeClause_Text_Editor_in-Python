# Text Editor
This is a simple text editor implemented using the Tkinter library in Python. The text editor provides basic functionalities such as creating new files, opening existing files, saving files, printing files, and editing text.


## Features
The text editor includes the following features:

- **New File**: Creates a new file by clearing the text area.
- **Open File**: Opens an existing file and displays its content in the text area.
- **Save**: Saves the currently opened file.
- **Save As**: Saves the file with a new name or in a different location.
- **Print File**: Prints the contents of the file.
- **Cut, Copy, Paste**: Provides options for cutting, copying, and pasting selected text.
- **Undo, Redo**: Allows undo and redo operations for text changes.
- **Select All, Clear All**: Selects all the text or clears the entire text area.
- **Text Formatting**: Provides options to make text bold, italic, and change its color.
- **Change Font**: Allows selecting different font styles and sizes.
- **Background Color**: Changes the background color of the text area.


## Usage
To run the text editor, execute the Python script. The graphical user interface (GUI) of the text editor will be displayed. You can perform various operations using the menu options and toolbar buttons.

- To create a new file, click on **File** > **New**.
- To open an existing file, click on **File** > **Open** and select a file.
- To save the current file, click on **File** > **Save**.
- To save the file with a new name or location, click on **File** > **Save As**.
- To print the file, click on **File** > **Print File**.
- To cut, copy, or paste text, use the respective buttons or keyboard shortcuts (Ctrl+x, Ctrl+c, Ctrl+v).
- To undo or redo text changes, use the respective buttons or keyboard shortcuts (Ctrl+z, Ctrl+y).
- To select all the text, use the **Edit** > **Select All** option or press Ctrl+a.
- To clear the text area, use the **Edit** > **Clear All** option or press Ctrl+Shift+a.
- To format the text, use the buttons provided in the toolbar. You can make the text bold, italic, or change its color.
- To change the font style and size, select the desired options from the drop-down menus in the toolbar.
- To change the background color of the text area, click on **Colors** > **Background** and select a color.


## Dependencies
The text editor requires the following dependencies:

- Python 3.x
- Tkinter library
- win32print and win32api libraries (for printing functionality on Windows)

You can install the required dependencies using pip:

```
pip install pywin32
```


## Limitations
- The text editor currently supports only plain text files (with .txt extension), HTML files (with .html extension), and Python files (with .py extension).
- The text editor's functionalities may vary depending on the operating system and the availability of specific libraries.

Feel free to explore and modify the code to enhance the functionality of the text editor according to your requirements.
