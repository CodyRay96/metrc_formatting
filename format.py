import os
import pandas as pd

# Specify the relative path
relative_path = r'F:\Consulting business\Clients\Ordi Nary\36th st\METRC\immature.xlsx'

# Convert to absolute path
absolute_path_baby = os.path.abspath(relative_path)
print(absolute_path_baby)

# Read Excel file using absolute path
df = pd.read_excel(absolute_path_baby)

#DataFrame
new_df = df.groupby(['Strain', 'Location'])['Plants'].count().reset_index()

baby_df = new_df.pivot(index = 'Strain', columns = 'Location', values = 'Plants')

baby_df.to_csv('metrc immature formatting.csv')


#Vegitative plants

# Specify the relative path
veg_relative_path = r'F:\Consulting business\Clients\Ordi Nary\36th st\METRC\veg.xlsx'

# Convert to absolute path
veg_absolute_path = os.path.abspath(veg_relative_path)
print(veg_absolute_path)

# Read Excel file using absolute path
pveg_df = pd.read_excel(veg_absolute_path)


veg_df = pveg_df.groupby(['Strain', 'Location']).size().reset_index(name='Count')

veg_df = veg_df.sort_values(by='Location')

veg_df.to_csv('metrc veg formatting.csv', index = False)

