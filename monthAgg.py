import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def monthExpense(month): 
	data_url = 'C:\\Users\\nidhi\\Desktop\\UCSC_Spring\\WebScraping\\bankStatements.csv'
	df = pd.read_csv(data_url)
	#print("Hello")

	df_rank = df.groupby('Months')
	print(df_rank.head(10))
	#month=3
	dates = []
	amount = []
	print("hi")
	print(month)
	for i in range(len(df)):
		if df.iloc[i]['Months'] == int(month):
			dates.append(df.iloc[i]['Dates'])
			amount.append(df.iloc[i]['Amount'])
			
	print(dates)
	grouped_dates=[]
	dayExpense=[]
	prevDate = dates[0].split('/')[1]
	sum=0
	print(prevDate)
	for d,a in zip(dates,amount):
		if d.split('/')[1] == prevDate:
			sum=sum+a
		else:
			grouped_dates.append(prevDate)
			dayExpense.append(sum)
			sum = a
			prevDate = d.split('/')[1]
	grouped_dates.append(prevDate)	
	dayExpense.append(sum)	
	print(grouped_dates)
	print(dayExpense)
	dayExpense = [int(i) for i in dayExpense]
	temp1=[]
	temp2=[]
	temp3=[]
	temp4=[]
	count=0
	for i in dayExpense:
		if i>0:
			temp1.append(i)
			temp3.append(grouped_dates[count])
		else:
			temp2.append(i)
			temp4.append(grouped_dates[count])
		count=count+1
			
	img = io.BytesIO()
		#plt.style.use('seaborn-whitegrid')
	plt.bar(temp3,temp1,label="Example two", color='g')
	plt.bar(temp4,temp2,label="Example two", color='r')
	for a,b in zip(x, y):
		plt.text(a, b, str(b))
	plt.show()
	plt.xticks(rotation=45)
	plt.savefig(img, format='png')
	img.seek(0)
	graph_url = base64.b64encode(img.getvalue()).decode()
	plt.close()
	return 'data:image/png;base64,{}'.format(graph_url)



	 
