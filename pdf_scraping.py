
from tabula import wrapper
import re
import math
import os
import matplotlib.pyplot as plt

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os 
import PyPDF2
import pandas as pd

def convert_pdf_to_txt(path, pages=None):
		if not pages:
			pagenums = set()
		else:
			
			pagenums = set(pages)
			print(pagenums)
		output = StringIO()
		manager = PDFResourceManager()
		converter = TextConverter(manager, output, laparams=LAParams())
		interpreter = PDFPageInterpreter(manager, converter)

		infile = open(path, 'rb')
		for page in PDFPage.get_pages(infile, pagenums):
			interpreter.process_page(page)
		infile.close()
		converter.close()
		text = output.getvalue()
		output.close()
		return text
		
		
def cleanAmountAndBalance(money):
	cleanedList = [x for x in money if str(x) != 'nan']
	cleanedList = [s.replace(',','') for s in cleanedList]
	for i in range(len(cleanedList)):
   
		if(cleanedList[i][0] == '$'):
      
			cleanedList[i] = cleanedList[i][1:]
			print(cleanedList[i])
	return cleanedList
	  
def cleanDates(trans_details):
	n_date =[]
	for date in trans_details:
		isMatch = re.match('^\d{2}\/\d{2}',date)
		if isMatch and len(date)==5:
		  #print(date)
		  n_date.append(date)
	return n_date

def getMonths(dates):
	months=[]
	for month in dates:
		months.append(month[0:2])
	return months
def cleanDescription(description):
	cleanedDescription=[]
	for desc in description:
		des = desc.split()
		#print(des[0])
		if(re.match("^\d{2}\/\d{2}",str(des[0]))):
		  #print(desc[5:])
		  cleanedDescription.append(desc[5:])
	return cleanedDescription


def scrap(filename):
	
	# pdf file object
	# you can find find the pdf file with complete code in below
	pdfFileObj = open(filename, 'rb')
	#print(filepath)
	# pdf reader object
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	# number of pages in pdf
	print(pdfReader.numPages)
	no_of_pages = pdfReader.numPages



	#This scrapes the PDF
	

	text = convert_pdf_to_txt(filename, pages=range(no_of_pages))
	arr = text.split('\n') #We split by new line
	print(arr)
	trans_details = arr
	#We will retrieve the labels by finding the index of  Beginning and Ending balance.
	st_index_labels = arr.index('Beginning Balance')
	end_index_labels = arr.index('Ending Balance')
	labels = arr[st_index_labels:end_index_labels+1]
	print(labels)
	
	#find start index
	index = end_index_labels
	st='Ending Balance'
	while index<(len(arr)-1):
		if arr[index] != '': 
			if arr[index][0] == '$':
				st=arr[index]
		  
				break
		index=index+1
  

	st
	print(index)

	st_index = index
	print(st_index)
	print(len(labels))
	summary = (arr[st_index:st_index+len(labels)])

	summary[len(summary)-1] = summary[len(summary)-1][1:]
	#Wrangle Strings to remove dollar sign and commas. Convert them to float to plot them
	summary[0] = summary[0][1:] # This removes dollar sign in the front, so we can use for plotting.
	summary = [s.replace(',','') for s in summary] # This removes commas from the amount

	print(summary)
	
	
	
	

	#This scrapes data from 
	

	dates = cleanDates(trans_details)
	print(len(dates))

	months =  getMonths(dates)
	months
	labels.insert(0,'Month')
	summary.insert(0,months[0])
	summary = [float(i) for i in summary] # converts the whole list into flots
	summary_dataframe = pd.DataFrame({
								  'Labels': labels,
								  'Amount': summary
	})
	summary_dataframe.to_csv('C:\\Users\\nidhi\\Desktop\\UCSC_Spring\\WebScraping\\Summary.csv', sep=',',mode='a',index=False)
	#Adjust the page number.
	#Test which is the start page where the transaction details are
	#If you give a page which does not have table then tabula will throw an exception
	print(summary_dataframe.info())
	print(summary_dataframe.head(10))

	startpage=0
	for page in range(no_of_pages):
		try:
			text = convert_pdf_to_txt(filename, pages=[page])
			arr = text.split('\n')
			index = arr.index('*start*transaction detail')
			if(index>=0):
				break
		except ValueError:
			startpage = startpage + 1
    


	print(startpage)
	print("Nit")


	#from tabula import wrapper


	#for page in range(startpage,)
	#tables = wrapper.read_pdf("C:\\Users\\nidhi\\Desktop\\UCSC_Spring\\WebScraping\\s2.pdf",multiple_tables=True, pages=0)

	#print(len(tables[0][2]))
	#for table in tables:
	 # for tab in range(len(table[0][2])):
	  #  print(tables[0][2][tab])

	
	#os.path.abspath("E:/Documents/myPy/")
	#Strange observation: 1) Though pages all means iterating all the pages and multi tables true should help to accumulate multiple table. But it has only one
	# 2) All the first page where the transaction starts like s4,s6 does fine  or has 0,1 as amounts otherwise it is on 0,2 
	
	balance=[]
	amount=[]
	description=[]
	  #print(len(tables[0][1]))

	

		#print(tables[0][2][tab])
	#for tab in range(len(tables[0][1])):
	# print(tables[0][1][tab])

	for page in range(startpage,no_of_pages):
		print(page)
		try:
			tables = wrapper.read_pdf(filename,multiple_tables=True, pages=page+1)
			print(tables[0][2])
			if((page)==startpage):
				try:
					for tab in range(len(tables[0][1])):
						amount.append(tables[0][1][tab])

				except:
					print("Amount Hi")
			else:
				try:
					for tab in range(len(tables[0][2])):
						amount.append(tables[0][2][tab])
				except:
					print("Amount Hi")
			try:
				for tab in range(len(tables[0][0])):
					description.append(tables[0][0][tab])
			except:
				print(" Description Hi")
			if((page)==startpage):
				try:

					for tab in range(len(tables[0][2])):
						balance.append(tables[0][2][tab])
				except:
					print("Balance Hi")
			else:
				try:

					for tab in range(len(tables[0][3])):
						balance.append(tables[0][3][tab])
				except:
					print("Balance Hi")

			#balance
			#cleanedList = [x for x in balance if str(x) != 'nan']
			#cleanedlist = [x for x in balance if x != 'nan']
			#cleanedList

			#amount
			print(amount)
			print(balance)
		except:
			print("table error")
		  
	
	print(amount)
	cleanedAmount = cleanAmountAndBalance(amount)
	cleanedAmount = [float(i) for i in cleanedAmount]
	cleanedAmount
	len(cleanedAmount)

	cleanedBalance = cleanAmountAndBalance(balance)
	cleanedBalance = [float(i) for i in cleanedBalance]
	cleanedBalance = cleanedBalance[1:]
	print((cleanedBalance))
	if len(cleanedBalance)>len(cleanedAmount):
		cleanedBalance = cleanedBalance[:len(cleanedBalance)-1]

	len(cleanedBalance)




	cleanedDescription = cleanDescription(description)
	cleanedDescription
	len(cleanedDescription)


	bankStatementInfo = pd.DataFrame({
								  'Dates': dates,
								  'Months': months,
								  'Description':cleanedDescription,
								  'Amount': cleanedAmount,
								  'Balance': cleanedBalance
	})
	print(bankStatementInfo.info())
	print(bankStatementInfo.head(10))
	from pathlib import Path

	my_file = Path("bankStatements.csv")
	if my_file.is_file():
		bankStatementInfo.to_csv('bankStatements.csv',index=False,header=False,sep=',',mode='a')
	else:

    # file exists
		bankStatementInfo.to_csv('bankStatements.csv',index=False,sep=',',mode='a')

	ism = re.match("^\d{2}\/\d{2}",'01/22')
	if ism:
	  print("Hi")
	  
	  
	return "Hello Nits!!"
	
	

