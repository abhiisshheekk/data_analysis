import numpy as np
import matplotlib.pyplot as la
import pandas as pd

histo = np.random.randint(0,100,1000)
lent = len(histo)
max = np.amax(histo)
interval = 10

size = (max//interval)+1

freq = np.random.randint(0,1,size)

for i in range(lent) :
	n = histo[i]//interval
	freq[n]=freq[n]+1
	
relfreq = freq/lent

density = relfreq/interval

# range = ['[0-<10]','[10-<20]','[20-<30]','[30-<40]','[40-<50]','[50-<60]','[60-<70]','[70-<80]','[80-<90]','[90-<100]']
# data = {'Range':range,'frequency':freq,'Relative frequency':relfreq,'Density':density}
# df = pd.DataFrame(data)
# print(df)

print("  Range\t\tFrequency\tRelativeFrequency\tDensity\n--------------------------------------------------------------------")
for i in range(size):
	print("[",interval*i,"-<",interval*(i+1),"]\t",freq[i],"\t\t",round(relfreq[i],5),"\t\t\t",round(density[i],5))
	
fig = la.figure()
la.hist(histo,bins=10,color="green",edgecolor="black")
la.ylabel('frequency')
la.xlabel('data')
la.title('Simple Histogram')
fig.savefig("hist.png")
