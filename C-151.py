month=("JAN","FEB","MAR","APR","MAY","JUNE","JULY","AUG","SEP","OCT","NOV","DEC")
Profit=(5,183,298,32,938,928,398,298,392,1,349,349)
max_profit=max(Profit)
max_profit_index=Profit.index(max_profit)
max_profit_month=month[max_profit_index]
print("The maximum profit of "+str(max_profit)+" was recorded in the month of "+str(max_profit_month))
min_profit=min(Profit)
min_profit_index=Profit.index(min_profit)
min_profit_month=month[min_profit_index]
print("The minimum profit of "+str(min_profit)+" was recorded in the month of "+str(min_profit_month)
      )

