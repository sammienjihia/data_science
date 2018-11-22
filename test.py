import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

pd_patientRecords = pd.read_csv('RegistrationData.csv')
pd_patientVisits = pd.read_csv('PatientPaidVisit.csv')

# Rename columns
pd_patientVisits.rename(columns=lambda x:x.replace(' ', '_').lower().replace('/','_'), inplace=True)
pd_patientRecords.rename(columns=lambda x:x.replace(' ', '_').lower().replace('/','_'), inplace=True)

# Unify the patient code columns in both dataframes
pd_patientVisits['patient_code'] = pd_patientVisits['patient_code'].map(lambda x: x.lstrip(' ').rstrip(' ')[:8])
pd_patientRecords['patient_code'] = pd_patientRecords['patient_code'].map(lambda x: x.lstrip(' ').rstrip(' ')[:8])

print(pd_patientRecords.info())

# pd_patientRecords['date_of_birth'].fillna(pd_patientRecords['date_of_birth'].mode()) 
# #pd_patientRecords[pd_patientRecords['date_of_birth']=='#NUM!'].apply(lambda x: x.replace(to_replace='#NUM!',value=0, inplace=True ))

# pd_patientRecords['date_of_birth'] = pd_patientRecords['date_of_birth'].map(lambda x: x.strip('#NUM!'))

# #new_dataframe = pd_patientVisits.merge()
# #pd_patientRecords['date_of_birth'] = pd.to_datetime(pd_patientRecords['date_of_birth'], unit='s')

# print(pd_patientRecords.tail())
# print(pd_patientVisits.tail())
# print(pd_patientRecords[pd_patientRecords['date_of_birth']=='#NUM!'])
# #print(pd_patientRecords[pd_patientRecords['date_of_birth']].fillna(pd_patientRecords['date_of_birth'].mode()))
# #print(pd_patientRecords[pd_patientRecords['date_of_birth']=='#NUM!'].replace(to_replace='#NUM!',value=0))

# #print(pd_patientRecords[pd_patientRecords['date_of_birth']=='#NUM!'].apply(lambda x: x.replace(to_replace='#NUM!',value=0, inplace=True )))