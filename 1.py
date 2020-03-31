import pandas as pd
df = pd.read_csv('pokemon.csv')

is_water = df['Type 1']=="Water"

water_filter = df[is_water]

w_elements = water_filter.sample(n=6)

print(w_elements)