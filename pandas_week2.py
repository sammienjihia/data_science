import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

pd_patientRecords = pd.read_csv('RegistrationData.csv')
pd_patientVisits = pd.read_csv('PatientPaidVisit.csv')

# Check number of rows
print(pd_patientRecords.iloc[0:,0].count())

#check for duplicates
print(pd_patientRecords.iloc[0:,0].duplicated())

print("***"*25)

print(pd_patientRecords.duplicated('Patient Code'))

# Drop duplicate rows in the Patient Code column
pd_patientRecords = pd_patientRecords.drop_duplicates('Patient Code', keep='first')

# Removing the unwanted strings in the patient code column

"""
Strip the spaces from the data set in the Patient Code column
lstrip() strips from the left, rstrip() strips from the right
The slice gets the first 8 characters in the patient's code
"""
print(pd_patientRecords['Patient Code'].map(lambda x: x.lstrip(' ').rstrip(' ')[:8]))
pd_patientRecords['Patient Code'] = pd_patientRecords['Patient Code'].map(lambda x: x.lstrip(' ').rstrip(' ')[:8])

print(pd_patientRecords['Patient Code'].head(100))
print(pd_patientRecords.tail(100))

print(pd_patientVisits.tail(100))



# Clean the PAtient's paid visit dataframe
# 1. Check for duplicate visitations
print(pd_patientVisits.duplicated('Visit Code'))
pd_patientVisits = pd_patientVisits.drop_duplicates('Visit Code', keep='first')
print(pd_patientVisits['Visit Code'])

# 2 Clean the patients visit's Patient code
print(pd_patientVisits['Patient Code'].map(lambda x: x.lstrip(' ').rstrip(' ')[:8]))

# Rename the columns replacing spaces and / with underscore
pd_patientVisits.rename(columns=lambda x:x.replace(' ', '_').lower().replace('/','_'), inplace=True)

# Clean the patient code column
pd_patientVisits.patient_code = pd_patientVisits.patient_code.map(lambda x: x.lstrip(' ').rstrip(' ')[:8])

print(pd_patientVisits)

# Check if there's any duplicated data
print(pd_patientVisits.duplicated('visit_code').sum())


print(pd_patientVisits.groupby('visit_location').diagnosis.count())
print(pd_patientVisits.iloc[:,7])
print(pd_patientVisits.diagnosis)

print(pd_patientVisits.info())

print("****"*15)
# Contains will check if the column contains the given string as argument
print(pd_patientVisits.diagnosis.str.contains('typhoid', regex=True, case=False).sum())
print(pd_patientVisits.diagnosis.str.contains('tyfoid', regex=True, case=False).sum())


#pd_patientVisits.diagnosis.replace(to_replace='tyfoid', value='typhoid', inplace=True)
#pd_patientVisits['typhoid'] = pd_patientVisits.diagnosis.str.contains('typhoid' , regex=True, case=False)
#pd_patientVisits['typhoid'] = pd_patientVisits.diagnosis.str.contains('tyfoid', regex=True, case=False)

#pd_patientVisits[pd_patientVisits.diagnosis.str.contains('tyfoid' , regex=True, case=False)=='True']
#print(pd_patientVisits[pd_patientVisits.diagnosis.str.contains('tyfoid' , regex=True, case=False)==True])
print(pd_patientVisits[ pd_patientVisits.diagnosis.str.contains('tyfoid', regex=True, case=False)==True])

dataframe1 = pd_patientVisits[ pd_patientVisits.diagnosis.str.contains('tyfoid', regex=True, case=False)==True] 
dataframe2 = pd_patientVisits[ pd_patientVisits.diagnosis.str.contains('typhoid', regex=True, case=False)==True]


print("***"*15)
print(dataframe1)



# Used the pandas apply function to use a custom function to search the diagnosis column entries for any string in my searchword list 
searchword =['tyfoid', 'typhoid']

def finder(x):
    for i in searchword:
        if str(i).lower() in str(x).lower():
            return True
    else:
        return np.nan

pd_patientVisits['is_typhoid'] = pd_patientVisits.diagnosis.apply(finder)

print(pd_patientVisits[pd_patientVisits['is_typhoid']==True])


pd_patientVisits.visit_date = pd.to_datetime(pd_patientVisits.visit_date)

pd_grouped = pd_patientVisits.groupby( [pd_patientVisits.visit_location,pd_patientVisits.visit_date.dt.strftime('%B')] ).is_typhoid.count()


print("*****"*15)

# Using concat function to combine two data frames together. Remember the fucntions agurment should be a list of simillar items to be concactenated
print(pd.concat([dataframe1,dataframe2]))


print(pd_grouped)
# pd_grouped.plot(kind='bar')

# plt.show()

print('hello world')


