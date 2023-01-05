'''
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

model = pickle.load(open('save_model/model.pickle', 'rb'))

df = pd.read_csv('/config/workspace/artifact/01042023__150114/data_ingestion/dataset/test.csv')
print(df.head(4))
df= df.drop(columns='class',axis=1)
# print(df.head(2))

label_encoder = LabelEncoder()
for col in df.columns:
    df[col] = label_encoder.fit_transform(df[col])
# print(df.head(2))

p = model.predict(df)

df['result']= p
print(df.head(4)) '''

import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
import joblib
import base64



def data_clean(df):
    encoder = LabelEncoder()
    for column in range(len(df.columns)):
        df[df.columns[column]]= encoder.fit_transform(df[df.columns[column]])
    return df

df = pd.read_csv('/config/workspace/mushrooms.csv')
df= df.drop(columns='class',axis=1)

file=data_clean(df)


loaded_model = joblib.load(open("save_model/model.pkl", 'rb'))

prediction = loaded_model.predict(file)

model=pd.DataFrame(prediction)
result=model.replace({0:'Edible' , 1:'Poisons'})

print(result)

