#Create list from query result
terminal = terminal_query_result[["CLOSING_FREE_STD_CNT","CLOSING_PAID_STD_CNT"]].tail(13)
terminal_month = terminal_query_result["MONTH_NAME"].tail(13).values

fig, ax = plt.subplots(figsize=(12,6))

bottom = np.zeros(len(terminal))

#Create stacked bar
for i, col in enumerate(terminal.columns):
    ax.bar(terminal.index, terminal[col], bottom=bottom, label=col)
    bottom += np.array(terminal[col])
    
totals = terminal.sum(axis=1)


#Create data label for total result
for i, total in enumerate(totals):
    ax.text(totals.index[i], total * 1.02, str(round(total/1000))+'K', 
            ha='center',
            weight='normal',
            size=10)

#Create data labels for bars
for bar in ax.patches:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() / 2 + bar.get_y(), 
            str(round(bar.get_height()/1000))+'K',
            ha='center',
            va='center',
            color='white',
            weight='normal',
            size=10)

ax.set_title('Title', loc='left')
axend = max(totals)+80000
ax.set_ylim(0,axend)
ax.legend(["Legend1","Legend2"], loc='upper left')
ax.set_yticks([])
ax.set_xticks(np.arange(len(terminal_month)))
ax.set_xticklabels(terminal_month)

plt.show()