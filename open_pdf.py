#!/usr/bin/env python3

import pdftotext


pdf_path='pdfs/CI20200119.pdf'

def printPdfToText(path): #return dic with the format: {product1:[unit price, quantity, total price], product2:[unit price, quantity, total price], ...}
    pdfFileObj = open(path, 'rb')
    pdftext=pdftotext.PDF(pdfFileObj)
    pdftextsplit=pdftext[0].split('\n')
    listNoFiltered=[]
    for e in pdftextsplit:
        if e!='':
            listNoFiltered.append(e.strip())
    start_index=listNoFiltered.index('Total')
    end_index=listNoFiltered.index('Resumen de operaciones de venta y descuentos')
    clean_list=joinPricesProducts(listNoFiltered, start_index, end_index)
    final_dic=createDic(clean_list)
    return final_dic

def joinPricesProducts(listNoFiltered, start_index, end_index):
    final_list=[]
    auxString=''
    for x in range(start_index+1, end_index):
        if '€' not in listNoFiltered[x]:
            auxString=auxString + listNoFiltered[x]
        else:
            auxString=auxString + listNoFiltered[x]
            final_list.append(auxString)
            auxString=''
    return final_list

def createDic(clean_list): #dic={product:[unit price, quantity, total price]}
    dic={}
    for product in clean_list:
        productName = getProductName(product)
        unitPrice = getUnitPrice(product)
        quantity = getQuantity(product)
        totalPrice = getTotalPrice(product)
        dic[productName]=[unitPrice, quantity, totalPrice]
    return dic

def getProductName(product): #search first € and search where the value begins, then get the full name
    firstEuro=product.index('€')
    count=0
    while (not product[firstEuro+count].isalpha()):
        count-=1
    return product[:firstEuro+count+1]  

def getUnitPrice(product): #search first € and search where the value begins
    firstEuro=product.index('€')
    count=0
    countSpaces=0
    while (not product[firstEuro+count].isalpha() and countSpaces<3):
        if product[firstEuro+count]==' ':
            countSpaces+=1
        count-=1
    return product[firstEuro+count+1:firstEuro+1]

def getQuantity(product): #search last letter to know where quantity ends
    firstEuro=product.index('€')
    endCount=len(product)
    while (not product[endCount-1].isalpha()):
        endCount-=1
    return product[firstEuro+1:endCount+1].strip()

def getTotalPrice(product): #search where the last number starts
    endCount=len(product)
    while (not product[endCount-1].isalpha()):
        endCount-=1
    return product[endCount+1:].strip()

if __name__=='__main__':
    printPdfToText(pdf_path)