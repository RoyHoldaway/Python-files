from tkinter import *
from pypdf import PdfReader

#variables
current_word = ""
current_word_index = 0

#this will establish the window for the program to display
root = Tk()
root.geometry("700x100")
root.title("Speed Reading Program")
root.resizable(False, False)
frame = Frame(root)
frame.pack(padx=10, pady=10)

#this will parse the pdf to go onto the speed reading program
def parse_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

book = parse_pdf("C:\\Users\\crazy\\Desktop\\ereaderbooks\\fahrenheit451Part1.pdf")  # Replace with your PDF file path

#get the words from the book and store them in a list
words = book.split()
current_word = words[current_word_index]

#break the word into 3 parts, beginning, middle, and end. Then make the middle letter red to help with speed reading
def word_split(words, current_word_index):
    current_word = words[current_word_index]
    for i in range(len(current_word)):
        if i == len(current_word) // 2:
            middle_index = i
            first = current_word[:middle_index]
            middle = current_word[middle_index]
            last = current_word[middle_index + 1:]
            Label(frame, text=first, font=("Helvetica", 36)).pack(side=LEFT)
            Label(frame, text=middle, fg="red", font=("Helvetica", 36)).pack(side=LEFT)
            Label(frame, text=last, font=("Helvetica", 36)).pack(side=LEFT)

def update_word(current_word_index):
    for widget in frame.winfo_children():
        widget.destroy()
    current_word_index += 1
    word_split(words, current_word_index)
    root.after(200, update_word, current_word_index)  # Update the word every 200ms
    if len(words) == current_word_index:
        print("End of book reached.")


update_word(0)  # Start updating from the first word
#program runs wihtin the main loop so we keep this here to ensure it runs within the loop
root.mainloop()