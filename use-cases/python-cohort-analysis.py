import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

df = pd.read_excel('transactions.xlsx')

data = df

# A function that will parse the date Time based cohort: 1 day of month
def get_month(x): return dt.datetime(x.year, x.month, 1)

# Create transaction_date column based on month and store in TransactionMonth
data['TransactionMonth'] = data['TransactionDate'].apply(get_month)

# Grouping by customer_id and select the InvoiceMonth value
grouping = data.groupby('UserId')['TransactionMonth'] 

# Assigning a minimum InvoiceMonth value to the dataset
data['CohortMonth'] = grouping.transform('min')

def get_date_int(df, column):
    year = df[column].dt.year
    month = df[column].dt.month
    day = df[column].dt.day
    return year, month, day

# Getting the integers for date parts
transcation_year, transaction_month, _ = get_date_int(data, 'TransactionMonth')

cohort_year, cohort_month, _ = get_date_int(data, 'CohortMonth')

#Get the  difference in years and months
years_diff = transcation_year - cohort_year

months_diff = transaction_month - cohort_month

""" 
Extract the difference in months from all previous values
"+1" in addeded at the end so that first month is marked as 1 instead of 0 for easier interpretation. 
"""

data['CohortIndex'] = years_diff * 12 + months_diff  + 1

# Counting daily active user from each cohort
grouping = data.groupby(['CohortMonth', 'CohortIndex'])

# Counting number of unique customer Id's falling in each group of CohortMonth and CohortIndex
cohort_data = grouping['UserId'].apply(pd.Series.nunique)
cohort_data = cohort_data.reset_index()

# Assigning column names to the dataframe created above
cohort_counts = cohort_data.pivot(index='CohortMonth',
                                 columns ='CohortIndex',
                                 values = 'UserId')

cohort_sizes = cohort_counts.iloc[:,0]

retention = cohort_counts.divide(cohort_sizes, axis=0)

# Coverting the retention rate into percentage and rounding off
retention = retention.round(3)*100
retention.index = retention.index.strftime('%Y-%m')

plt.figure(figsize=(16, 10))
plt.title('Monthly Cohorts %', fontsize = 14)

# Creating the heatmap
sns.heatmap(retention, annot = True,vmin = 0.0, vmax =30,cmap="RdYlGn", fmt='g')
plt.ylabel('Cohort Month')
plt.xlabel('Cohort Index')
plt.yticks( rotation='360')
plt.show()