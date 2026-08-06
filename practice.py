import pandas as pd
sf = pd.read_csv('practice.csv')
print (sf.head())
print (sf.tail())
print(sf)
print(sf.head(10))
print(sf['Country'])
print(sf['age'])
print('mean of age:', sf['age'].mean())
print("max of age:", sf['age'].max())
print("min of age:", sf['age'].min())
sf['Full Name'] = sf['First Name'] + ' ' + sf['Last Name']
print(sf['Full Name'])
result = sf['age']* sf['age']
print(result)
def transform_country(country):
    if country == 'USA':
        return 'United States'
    elif country == 'Brasil':
        return 'Brazil'
    else:
        return country
    sf['Country'] = sf['Country'].apply(transform_country)
    print(sf['Country'])
    print(sf)