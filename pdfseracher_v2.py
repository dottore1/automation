import PyPDF2
import sys
import time
import os

print("Welcome to the pdf searcher! \nI can search in x pdf files given in a specific folder :-)")
search_term = input(str("Type in the keyword you want to search for: "))

file2 = open("result.txt", "w+")


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
                file2.write("\nKeyword: " + '"' + search_word + '"' + " is found on " + "page number: " + str(pdfReader.getPageNumber(pageObj)+1))

    print("The keyword {} was found {} times".format(search_word, search_word_count) + " in " + str(pdfFileObj.name))
    file2.write("\nThe keyword {} was found {} times".format(search_word, search_word_count) + "\n in " + str(pdfFileObj.name))



pdf_found = 0

for file in os.listdir("C:/Users/Nichlas/Documents/Noter_OOP/search_area"):
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





