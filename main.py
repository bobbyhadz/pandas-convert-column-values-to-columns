# Convert column Values to Columns in a Pandas DataFrame

import pandas as pd


df = pd.DataFrame({
    'Frontend': ['React', 'Vue', 'Angular'],
    'Styles': ['Bootstrap', 'Vuetify', 'Material'],

})

print(df)

print('-' * 50)

df2 = df.pivot_table(values='Styles', index=df.index,
                     columns='Frontend', aggfunc='first')

print(df2)