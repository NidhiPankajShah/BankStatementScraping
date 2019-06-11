import pandas as pd
import io
import base64
import matplotlib.pyplot as plt

def summaryGraph(month):
	data_url = 'C:\\Users\\nidhi\\Desktop\\UCSC_Spring\\WebScraping\\Summary.csv'
	df = pd.read_csv(data_url)
	for r in df['Labels']:
		if r=='Month':
			print("He")
	month = '1.0'	
	labels = []	
	amount=[]
	index = -1
	for i in range(len(df)):
		if df.iloc[i]['Labels']=='Month':
			print(df.iloc[i]['Amount'])
			if df.iloc[i]['Amount'] == month:
				print("I am inside")
				index=i
				break
			else:
				print ("Not found!")
	if index > -1:			
		while df.iloc[index]['Labels'] != 'Ending Balance':
			labels.append(df.iloc[index]['Labels'])
			amount.append(df.iloc[index]['Amount'])
			index = index + 1
			
	labels.append('Ending Balance')
	amount.append(df.iloc[index]['Amount'])
	labels = labels[1:]
	amount=amount[1:]
	print(labels)
	print(amount)	
	img = io.BytesIO()
			#plt.style.use('seaborn-whitegrid')
	plt.bar(labels,amount,label="Example two", color='g')
	plt.xticks(rotation=45)
	plt.savefig(img, format='png')
	img.seek(0)
	graph_url = base64.b64encode(img.getvalue()).decode()
	plt.close()
		
	return 'data:image/png;base64,{}'.format(graph_url)
			
#print(df['Labels'])