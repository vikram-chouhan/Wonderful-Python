import matplotlib.pyplot as plt
y=[1980,1984,1989,1991,1996,1998,1999,2004,2009,2014]
n=[35,40,49,51,59,60,61,67,71,83]
plt.plot(y,n, linestyle="dashdot")
plt.xlabel('year of election')
plt.ylabel('no of electors')
plt.title('voter turnout b/w 1980 to 2014')
plt.show()
