import pandas as pd


def keywordExpenses(keyword):
	#keyword = "Safeway"
	keywordArr = keyword.split()
	data_url = 'C:\\Users\\nidhi\\Desktop\\UCSC_Spring\\WebScraping\\bankStatements.csv'
	df = pd.read_csv(data_url)
	amount =0
	#common = keyword
	for i in range(len(df)):
		desc = df.iloc[i]['Description'].split()
		common = set(keywordArr).intersection( set(desc) )
		if len(common) > 0:
			amount= amount+df.iloc[i]['Amount']
			  
			
	print(amount)
	return amount
