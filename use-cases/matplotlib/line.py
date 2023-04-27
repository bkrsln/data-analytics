#Create lists from dataframe
[month,churn_rate] = [list(kpi_query_result.MONTH_NAME.tail(13).values),
                      list(kpi_query_result.CHURN_RATE.tail(13).values)]

fig, ax = plt.subplots(figsize=(12,6))

plt.plot(month, churn_rate, linewidth=2, marker="o") 

for i,j in zip(month,churn_rate):
    ax.annotate(str(round(j,2))+'%',
                xy=(i,j),
                xytext=(0,10),
                textcoords="offset points",
                rotation=0,
                ha='center', va='bottom',)

plt.title("Title", loc='left')
plt.legend(["Legend1"], loc='upper left')
plt.xticks(rotation=0)
plt.ylim([min(churn_rate)-2,max(churn_rate)+2])
plt.yticks([])

plt.show()