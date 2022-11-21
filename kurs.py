import pandas as pd
import datetime 
import numpy as np

nowa_0 = datetime.datetime.now().strftime('%d.%m.%Y')
nowa_1 = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d.%m.%Y')
nowa_2 = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime('%d.%m.%Y')


try:
    df = pd.read_excel('kurs.xlsx')
except:
    df = pd.DataFrame(data=[],columns=[nowa_0, nowa_1, nowa_2])

content_get = pd.read_html(f'https://www.nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-\
rynochnye-kursy-valyut/report?rates%5B%5D=5&rates%5B%5D=6&rates%5B%5D=8&rates%5B%5D=\
16&beginDate={nowa_2}&endDate={nowa_0}')
df_new_data = pd.DataFrame([i for i in np.array(content_get)[0]]).rename(columns={0:"Currency",
                                                                                  2:"Dollar", 
                                                                                  4:"Euro", 
                                                                                  6:"Yuan", 
                                                                                  8:"Ruble"})
df_new_data = df_new_data[["Currency","Dollar", "Euro", "Yuan", "Ruble"]].T
df_new_data.columns = df_new_data.iloc[0]
df_new_data = df_new_data.iloc[1:].reset_index().rename(columns={'index':"Currency"})

for i in df_new_data.columns:
    df[i] = df_new_data[i]

df.to_excel('kurs.xlsx', index=False)

print(1)
