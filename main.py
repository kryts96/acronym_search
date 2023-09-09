import PyPDF2
import pdfplumber
# creating an object
acronym_list = []

def acronym_search(text):
    aux=""
    in_list = False
    for character in text:
        if character>='A' and character<='Z':
            aux+=character
        else:
            if len(aux)>1:
                for entry in acronym_list:
                    if aux in entry:
                        in_list = True
                        break
                if not in_list:
                #if (aux + " Page " + str(page+1)) not in acronym_list:
                    acronym_list.append(aux + " Page " + str(page+1))
                else:
                    in_list = False
            aux=""

# with pdfplumber.open(r'45463_tese.pdf') as pdf:
#     for page in range (29, 106):
#         print("searching in page: " + str(page))
#         print(str(106 - page) + " pages left.")
#         pageObj = pdf.pages[page]
#         if len(pageObj.chars):
#             page_contents = pageObj.extract_text()
#             if len(page_contents):
#                 acronym_search(page_contents)
#         else:
#             print("Page" + str(page) + "is empty")
#             continue
file = open('45463_tese.pdf', 'rb')

#creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)


for page in range (28, 106):
    print("searching in page: " + str(page))
    print(str(fileReader.numPages-18-page) + " pages left.")
    pageObj = fileReader.getPage(page)
    page_contents = pageObj.extractText()
    if len(page_contents):
        acronym_search(page_contents)

if len(acronym_list):
    with open('acronym_list.txt', 'w') as f:
        for item in acronym_list:
            f.write("%s\n" % item)
    #print(acronym_list)
# print the number of pages in pdf file
#print(fileReader.numPages)