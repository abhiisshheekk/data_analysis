import numpy as np
import matplotlib.pyplot as la
from scipy import stats

# function to calculate mode
def get_mode(list) :
	count = 0
	num = list[0]
	for i in list :
		freq = list.count(i)
		if freq>count :
			count = freq
			num = i
	return num,count

# array definition and its boxplot
set = np.random.randint(0,101,1000)
# set = np.append(set,[156,-65])
fig = la.figure()
la.boxplot(set)
fig.savefig("box.png")

# sorting array
sorted_data = np.sort(set).tolist()

# stats using predefined functions
mean_set = np.mean(set)
median_set = np.median(set)
mode_set = stats.mode(set)
quantile1_set = np.percentile(set,25)
quantile2_set = np.percentile(set,50)
quantile3_set = np.percentile(set,75)
iqr_set = stats.iqr(set)


# printing data of predefined functions
print("Predefined function\n--------------------\nMean: ",mean_set," ; Median: ",median_set," ; Mode: ",mode_set," ; 1st Quartile: ",quantile1_set," ; 2nd Quartile: ",quantile2_set," ; 3rd Quartile: ",quantile3_set," ; InterQuartileRange: ",iqr_set,'\n')

# calculating mean
lent = len(set)
sum = np.sum(set)
mean = sum/lent

# calculating mediant
median = 0
if (lent%2 == 0) :
	median = (sorted_data[(lent//2)-1] + sorted_data[lent//2])/2
else :
	median = sorted_data[(lent-1)//2]*1.0

# calculating quartiles
quantile1 = 0
if (lent+1)%4 == 0 :
	quantile1 = sorted_data[((lent+1)//4)-1]*1.0
else :
	quantile1 = (sorted_data[((lent+1)//4)-1] + sorted_data[(lent+1)//4])/2

quantile2 = median

quantile3 = 0
if (3*(lent+1))%4 == 0 :
	quantile3 = sorted_data[((3*(lent+1))//4)-1]*1.0
else :
	quantile3 = (sorted_data[((3*(lent+1))//4)-1] + sorted_data[(3*(lent+1))//4])/2
	

# outliers
iqr = quantile3 - quantile1
ub = quantile3 + 1.5*iqr
lb = quantile1 - 1.5*iqr
outliers = []

for i in sorted_data :
	if i<lb or i>ub :
		outliers.append(i)
	else :
		continue

# calculating mode
mode,count = get_mode(sorted_data)

# printing calculated data
print("Calculated\n--------------------\nMean: ",mean," ; Median: ",median," ; Mode: ",mode,",count: ",count," ; 1st Quartile: ",quantile1," ; 2nd Quartile: ",quantile2," ; 3rd Quartile: ",quantile3," ; InterQuartileRange: ",iqr)

print("Outliers: ",outliers)