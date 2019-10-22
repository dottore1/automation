import PyPDF2
import sys
import time
import os
import tkinter
from tkinter import filedialog

def search_dir():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir


print("Welcome to the pdf searcher! \nI can search in x pdf files given in a specific folder :-)")
root = tkinter.Tk()
root.withdraw()
chosen_path = search_dir()

search_term = input(str("Type in the keyword you want to search for: "))


file2 = open("result.txt", "w+")
file2.write("You are now searching for "+search_term)
print("You are now searching for "+search_term)


def searcher(path, keyword):
    pdf_file_obj = open(str(path) , 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj, strict=True)
    search_word = keyword
    search_word_count = 0

    for pageNum in range(1, pdf_reader.numPages):
        pageObj = pdf_reader.getPage(pageNum)
        text = pageObj.extractText().encode('utf-8')
        search_text = text.lower().split()
        for word in search_text:
            if search_word in word.decode("utf-8"):
                search_word_count += 1
                print("Keyword: " + search_word + " is found on " + "page number: " + str(pdf_reader.getPageNumber(pageObj)+1))
                file2.write("\nKeyword: " + '"' + search_word + '"' + " is found on " + "page number: " + str(pdf_reader.getPageNumber(pageObj)+1))

    print("The keyword {} was found {} times".format(search_word, search_word_count) + " in " + str(pdf_file_obj.name))
    file2.write("\nThe keyword {} was found {} times".format(search_word, search_word_count) + "\n in " + str(pdf_file_obj.name))


pdf_found = 0

for file in os.listdir(chosen_path):
    if file.endswith(".pdf"):
        pdf_found += 1
        path =  os.path.join("C:/Users/Nichlas/Documents/Noter_OOP/search_area", file)
        print("------------------------------------------")
        file2.write("\n------------------------------------------")
        print("Now searching: " + path)
        file2.write("\nNow searching: " + path)
        searcher(path, search_term)
        print("-------------------------------------------")
        file2.write("\n-------------------------------------------")

print("We found: " + str(pdf_found) + "pdfs")
file2.write("\n*********We found: " + str(pdf_found) + "pdfs*********")
file2.close()
time.sleep(100)





