import random
import matplotlib.pyplot as lala
import pandas as pd
import numpy as freak
from scipy import stats
	
series = pd.Series(freak.random.randint(0,101,1000000))
print('1,000,000 Data-\n****************\nMean: ',series.mean(),'\nMedian: ',series.median(),'\nMode: ',stats.mode(series))
fig = lala.figure()
lala.hist(series)
fig.savefig('hist_full')

sample1 = series.sample(n = 10000)
print('\n10,000 Data-\n****************\nMean: ',sample1.mean(),'\nMedian: ',sample1.median(),'\nMode: ',stats.mode(sample1))
fig2 = lala.figure()
lala.hist(sample1)
fig2.savefig('hist_sample1')

count=0
i=0
halla=[]
while count<10000 :
	halla.append(series[i])
	count+=1
	i=i+5	

sample2 = pd.Series(halla)
print('\n10,000 step-sized Data-\n****************\nMean: ',sample2.mean(),'\nMedian: ',sample2.median(),'\nMode: ',stats.mode(sample2))
fig3 = lala.figure()
lala.hist(sample2)
fig3.savefig('hist_sample2')

ser = series.tolist()
values = [ser,sample1,sample2]
fig1 = lala.figure()
lala.boxplot(values)
fig1.savefig('box')