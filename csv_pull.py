import pandas as pd

file = 'phzm_us_zipcode_2023.csv'
df = pd.read_csv(file)

zip_code = 72719
print(df.loc[df['zipcode'] == 72719], 'zone')
# print(df.loc[df['zipcode'] == 72719])
# print(df.loc[df['zipcode']])
matching_zone = df.loc[df['zipcode'] == 72719, 'zone'].values[0]
print(matching_zone)


# print(df.loc[df['zone'] == matching_zone],'zipcode')
# print(df.loc[df['zone'] == matching_zone].head(5),'zipcode')
# print(type(df.loc[df['zone'] == matching_zone].head(5),'zipcode'))
# result = df.loc[df['zone'] == matching_zone].head(5),'zipcode'
# result = df.loc[df['zone'] == matching_zone, 'zipcode'].head(5)
result = df.loc[df['zone'] == matching_zone, 'zipcode'].head(5).reset_index(drop=True) #  as pandas obj
# result = df.loc[df['zone'] == matching_zone, 'zipcode'].head(5).tolist() # as a listd
result = result.to_json() # as json obj
print(result)
print(type(result))
# print(df.loc[df['zone'] == matching_zone].iloc[0],'zipcode')

# print(df.loc[df['zone'] == matching_zone].iloc[0],'zipcode')

