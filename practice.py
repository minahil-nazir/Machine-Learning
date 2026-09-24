import pandas as pd
    # First, make sure you have your dataframe created
# For example:
sf = pd.DataFrame({
    'Full Name': ['Bob Smith', 'Alice Williams', 'Malcolm Jones', 'Felix Brown', 'Nancy Cooper'],
    'age': [576, 529, 484, 529, 529],
    'Country': ['USA', 'UK', 'Canada', 'USA', 'UK'],
    'First Name': ['Bob', 'Alice', 'Malcolm', 'Felix', 'Nancy']
})

def transform_country(country):
    # Do something with the country if needed, but remove the return
    # or keep it at the end
    return country  # This should be the LAST line in the function

# Apply the transformation (but since it just returns the same value, 
# you might not need this function at all)
sf['Country'] = sf['Country'].apply(transform_country)
print(sf['Country'])
print(sf)
print('number of rows:', len(sf))

# Sort and get first 10 first names
sf_sorted = sf.sort_values('First Name', ascending=True)
first_name = sf_sorted[0:10]['First Name']
print(first_name)
