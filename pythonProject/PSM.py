import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('C:\\Users\\zoes\\Documents\\Github\\Pricing\\pythonProject\\data\\psm.csv')
'''
print(df.columns)
print(df.shape)
print(df.describe())
'''
df_1=(df.unstack().reset_index().rename(columns={'level_0':'label','level_1':'#',0:'price'})
                                        .groupby(['label','price'])
                                        .size().reset_index()
                                        .rename(columns={0:'freq'}))
df_1['sum']=df_1.groupby(['label'])['freq'].transform('sum')
df_1['cumsum']=df_1.groupby(['label'])['freq'].cumsum()
df_1['percentage']=df_1['cumsum']/df_1['sum']
print(df_1)

df_2=df_1.pivot_table('percentage','price','label')
print(df_2)

df_3=df_2.interpolate().fillna(0)
df_3['Too Cheap']=1.00-df_3['Too Cheap']
df_3['Cheap']=1.00-df_3['Cheap']

df_3.plot()
plt.show()