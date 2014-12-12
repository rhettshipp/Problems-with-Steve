import pandas as pd

chemdf = pd.read_csv('/Users/rhettshipp1/Desktop/Problems-with-Steve/Data Files/AID_466_data.csv',
                     na_values = '')
shrtchemdf = chemdf[['PUBCHEM_CID',
                     'PUBCHEM_ACTIVITY_OUTCOME', 
                     '4^Hill Slope^FLOAT^^^^']]

