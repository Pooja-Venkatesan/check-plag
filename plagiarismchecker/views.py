#!/usr/bin/python3
from django.shortcuts import render
from django.http import HttpResponse
from plagiarismchecker.algorithm import main
from docx import *
from plagiarismchecker.algorithm import fileSimilarity
import PyPDF2 

# Create your views here.
#home
def home(request):
    return render(request, 'pc/index.html') 


#web search(Text)
def test(request):
    # print("request is welcome test")

    print(request.POST['q'])  
    
    if request.POST['q']: 
        totalPercent, uniquePercent, link, text, tracker= main.findSimilarity(request.POST['q'])
        uniquePercent = (100-totalPercent)
        totalPercent = round(totalPercent,2)
        uniquePercent = round(uniquePercent,2)
    print("Output..!!!",totalPercent, uniquePercent, link, text, tracker)
    return render(request, 'pc/index.html',{'totalPercent': totalPercent,'uniquePercent': uniquePercent,'link': link, 'text' : text, 'tracker':tracker})
    

#web search file(.txt, .docx)
def filetest(request):
    value = ''    
    print(request.FILES['docfile'])
    if str(request.FILES['docfile']).endswith(".txt"):
        value = str(request.FILES['docfile'].read())

    elif str(request.FILES['docfile']).endswith(".docx"):
        document = Document(request.FILES['docfile'])
        for para in document.paragraphs:
            value += para.text

    elif str(request.FILES['docfile']).endswith(".pdf"):
        # creating a pdf file object 
        pdfFileObj = open(request.FILES['docfile'], 'rb')

        # creating a pdf reader object 
        pdfReader = PyPDF2.PdfReader(pdfFileObj)

       # print number of pages in the pdf file
        print("Page Number:", pdfReader.numPages)

        # creating a page object 
        pageObj = pdfReader.getPage(0) 

        # extract text from page
        value = pageObj.extractText()
        value = str(request.FILES['docfile'].read())
        # print(pageObj.extractText()) 
        print(value)

        # closing the pdf file object 
        pdfFileObj.close() 


    totalPercent, uniquePercent, link, text, tracker= main.findSimilarity(value)
    print("Output..!!! \n",totalPercent, uniquePercent, link, text, tracker )
    return render(request, 'pc/index.html',{'link': link, 'totalPercent': totalPercent,'uniquePercent':uniquePercent, 'text' : text, 'tracker':tracker})


# def report(request):
#     return render(request, 'pc/report.html')
# .........Extrinsic.................
#text compare
def fileCompare(request):
    return render(request, 'pc/doc_compare.html') 

#two text compare(Text)
def twofiletest1(request):
    print("Submiited text for 1st and 2nd")
    print(request.POST['q1'])
    print(request.POST['q2'])

    if request.POST['q1'] != '' and request.POST['q2'] != '': 
        print("Got both the texts")
        result = fileSimilarity.findFileSimilarity(request.POST['q1'],request.POST['q2'])
    result = round(result,2)    
    print("Output>>>!!!!",result)
    return render(request, 'pc/doc_compare.html',{'result': result})
    

#two text compare(.txt, .docx)
def twofilecompare1(request):
    value1 = ''
    value2 = ''
    if (str(request.FILES['docfile1'])).endswith(".txt") and (str(request.FILES['docfile2'])).endswith(".txt"):
        value1 = str(request.FILES['docfile1'].read())
        value2 = str(request.FILES['docfile2'].read())

    elif (str(request.FILES['docfile1'])).endswith(".docx") and (str(request.FILES['docfile2'])).endswith(".docx"):
        document = Document(request.FILES['docfile1'])
        for para in document.paragraphs:
            value1 += para.text
        document = Document(request.FILES['docfile2'])
        for para in document.paragraphs:
            value2 += para.text

    result = fileSimilarity.findFileSimilarity(value1,value2)
    
    print("Output! \n",result)
    return render(request, 'pc/doc_compare.html',{'result': result})
# .................
