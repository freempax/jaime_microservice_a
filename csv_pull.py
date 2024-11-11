import pandas as pd

file = 'phzm_us_zipcode_2023.csv'
df = pd.read_csv(file)

zip_code = 72719
print(df.loc[df['zipcode'] == 72719], 'zone')
# print(df.loc[df['zipcode'] == 72719])
# print(df.loc[df['zipcode']])
matching_zone = df.loc[df['zipcode'] == 72719, 'zone'].values[0]
print(matching_zone)


print(df.loc[df['zone'] == matching_zone],'zipcode')
# print(df.loc[df['zone'] == matching_zone].iloc[0],'zipcode')

# print(df.loc[df['zone'] == matching_zone].iloc[0],'zipcode')

