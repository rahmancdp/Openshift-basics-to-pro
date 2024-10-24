import pandas as pd
from tabulate import tabulate

# Creating the data
data = {
    'Name': ['Abdul Farook', 'Abdul Rahman', 'Shajahan'],
    'Profession': ['Engineer', 'Architect', 'Engineer']
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame in a beautiful format using tabulate
print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
