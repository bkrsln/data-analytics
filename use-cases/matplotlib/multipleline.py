#Create lists from dataframe
#First list is for x axis
[month,std,std_ter] = [list(kpi_query_result.MONTH_NAME.tail(13).values),
                       list(kpi_query_result.CLOSING_STALONE_CNT.tail(13).values),
                       list(kpi_query_result.CLOSING_TER_AND_STALONE_CNT.tail(13).values)]

fig, ax = plt.subplots(figsize=(12,6))

#Create one line for a list
plt.plot(month, std, linewidth=2, marker="o")

#Create another line for a list and hide 0 values
plt.plot(month[std_ter.count(0):], std_ter[std_ter.count(0):], 
         linewidth=2, marker="o")  

#Create data labels and format texts
for i,j in zip(month,std):
    ax.annotate(str(round(j/1000))+'K', 
        xy=(i,j),
        xytext=(0,-20),
        textcoords="offset points",
        ha='center', va='bottom')
    
for i,j in zip(month,std_ter):
    ax.annotate(str(round(j/1000))+'K',
        xy=(i,j),
        xytext=(0,6),
        textcoords="offset points",
        ha='center', va='bottom')

plt.title("Title", loc='left')
plt.legend(["Legend1","Legend2"], loc='upper left')
plt.xticks(rotation=0)
plt.ylim([min(std)-50000,max(std_ter)+100000])
plt.yticks([])

plt.show()