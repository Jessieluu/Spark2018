
# coding: utf-8

# In[7]:

def Normalization(x):
    min = x.min()
    max = x.max()
    result = x.map(lambda x: (x-min)/(max-min))
    return result


# In[23]:

import csv
global Path
Path = "file:/home/ethan/pythonwork/ipynotebook/hw1/"

# input data
dataset = sc.textFile( Path + "household_power_consumption.txt" )

#split data with ";"
rowData = dataset.map(lambda row : row.split(";")).filter(lambda x : not x[0] == 'Date')

#global_active_power
float_gap = rowData.map(lambda column: column[2]).filter(lambda x: x!='?').map(lambda x: float(x))
min_gap = float_gap.min()
max_gap = float_gap.max()
count_gap = float_gap.count()
mean_gap = float_gap.mean()
std_gap = float_gap.stdev()
gap_normalization = Normalization(float_gap).collect()


#global_reactive_power
float_grp = rowData.map(lambda column: column[3]).filter(lambda x: x!='?').map(lambda x: float(x))
min_grp = float_grp.min()
max_grp = float_grp.max()
count_grp = float_grp.count()
mean_grp = float_grp.mean()
std_grp = float_grp.stdev()
grp_normalization = Normalization(float_grp).collect()

#voltage
float_voltage = rowData.map(lambda column: column[4]).filter(lambda x: x!='?').map(lambda x: float(x))
min_voltage = float_voltage.min()
max_voltage = float_voltage.max()
count_voltage = float_voltage.count()
mean_voltage = float_voltage.mean()
std_voltage = float_voltage.stdev()
voltage_normalization = Normalization(float_voltage).collect()

#global_intensity
float_gi = rowData.map(lambda column: column[4]).filter(lambda x: x!='?').map(lambda x: float(x))
min_gi = float_gi.min()
max_gi = float_gi.max()
count_gi = float_gi.count()
mean_gi = float_gi.mean()
std_gi = float_gi.stdev()
gi_normalization = Normalization(float_gi).collect()

file = open("result.txt", 'a')
write = csv.writer(file)

for i in range(0, len(gap_normalization)):
    tmpArray = []
    tmpArray.append(gap_normalization[i])
    tmpArray.append(grp_normalization[i])
    tmpArray.append(voltage_normalization[i])
    tmpArray.append(gi_normalization[i])
    write.writerow(tmpArray)
    
file.close()


# In[22]:

print("---------Subtask 1---------")
print("Minimum of global active power:", min_gap)
print("Minimum of global reactive power:", min_grp)
print("Minimum of voltage:", min_voltage)
print("Minimum of global_intensity:", min_gi)
print("---------------------------")
print("Maximum of global active power:", max_gap)
print("Maximum of global reactive power:", max_grp)
print("Maximum of voltage:", max_voltage)
print("Maximum of global_intensity:", max_gi)
print("---------------------------")
print("Count of global active power:", count_gap)
print("Count of global reactive power:", count_grp)
print("Count of voltage:", count_voltage)
print("Count of global_intensity:", count_gi)

print("---------Subtask 2---------")
print("Mean of global active power:", mean_gap)
print("Mean of global reactive power:", mean_grp)
print("Mean of voltage:", mean_voltage)
print("Mean of global_intensity:", mean_gi)
print("---------------------------")
print("Standard deviation of global active power:", std_gap)
print("Standard deviation of global reactive power:", std_grp)
print("Standard deviation of voltage:", std_voltage)
print("Standard deviation of global_intensity:", std_gi)


# In[ ]:



