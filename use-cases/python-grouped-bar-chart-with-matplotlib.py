#Create lists from dataframe
[labels,month,acq,churn,netadd] = [list(kpi_query_result.tail(13).index),
                                   list(kpi_query_result.MONTH_NAME.tail(13).values),
                                   list(kpi_query_result.ACQ_STALONE_CNT.tail(13).values),
                                   list(kpi_query_result.CHURN_STALONE_CNT.tail(13).values),
                                   list(kpi_query_result.NETADD_STALONE_CNT.tail(13).values)]

x = np.arange(len(labels))
width = 0.3

fig, ax = plt.subplots(figsize=(12, 6))

#Create and locate bars
rects1 = ax.bar(x - width, acq, width, label='Acq')
rects2 = ax.bar(x , churn, width, label='Churn')
rects3 = ax.bar(x + width, netadd, width, label='NetAdd')

#Create data labels in bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            str(round(height/1000))+'K',
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(1, 5),
            textcoords="offset points",
            rotation=90,
            ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

ax.set_title('Title', loc='left')
ax.set_xticks(x)
ax.set_yticks([])
ax.set_xticklabels(month)
ax.legend(["Legend1","Legend2", "Legend3"], loc='upper left', ncol=3)

axstart = round((min(acq+churn+netadd))*1.5/1000)*1000
axend = round((max(acq+churn+netadd))*1.5/1000)*1000
ax.set_ylim(axstart,axend)

plt.show()