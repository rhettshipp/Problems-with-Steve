import pandas as pd

#create a dataframe
df = pd.read_csv('/Users/rhettshipp1/Desktop/Problems-with-Steve/Data Files/AID_466_data.csv')

#create an object for each condition to subset by
active = df['PUBCHEM_ACTIVITY_OUTCOME'] == 'Active'
lowerslope = df['4^Hill Slope^FLOAT^^^^'] > 0.2
upperslope = df['4^Hill Slope^FLOAT^^^^'] < 2.0

#combine the different conditions
selection = active * lowerslope * upperslope

#subset the dataframe by those conditions
CID = df['PUBCHEM_CID'][selection]

print CID