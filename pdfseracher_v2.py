import PyPDF2
import sys
import time
import os

print("Welcome to the pdf searcher! \nI can search in x pdf files given in a specific folder :-)")
search_term = input(str("Type in the keyword you want to search for: "))


def searcher(path, keyword):
    pdfFileObj = open(str(path) , 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=True)
    search_word = keyword
    search_word_count = 0

    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        text = pageObj.extractText().encode('utf-8')
        search_text = text.lower().split()
        for word in search_text:
            if search_word in word.decode("utf-8"):
                search_word_count += 1
                print("Keyword: " + search_word + " is found on " + "page number: " + str(pdfReader.getPageNumber(pageObj)+1))

    print("The keyword {} was found {} times".format(search_word, search_word_count) + " in " + str(pdfFileObj.name))
    time.sleep(1)


for file in os.listdir("C:/Users/Nichlas/Documents/Noter_OOP/search_area"):
    if file.endswith(".pdf"):
        path =  os.path.join("C:/Users/Nichlas/Documents/Noter_OOP/search_area", file)
        print("------------------------------------------")
        print("Now searching: " + path)
        searcher(path, search_term)
        print("-------------------------------------------")
