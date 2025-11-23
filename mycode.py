import pandas as pd
import os 

data={
    'name':['kaif','zain','kazi'],
    'age':['20','20','21'],
    'city':['Monaco','barzil','new york']
}

df=pd.DataFrame(data)

new={'name':'kubar','age':'20','city':'bombay'}
df.loc[len(df.index)]=new


data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)
print("csv file is saved to {file_path}")