# Open the right CSV File and search through "right" apartments
import pandas as pd
import csv

filepath = "C:/Users/silas/wohnung_alert/data/wohnungen.csv"

with open (filepath, "r") as file:
    content = pd.read_csv(file)

    print(content['Preis'].head(5))         #check the output value of the data
    print(content.dtypes)
    print(content["Quadratmeter"].unique())
    print(content[content['Quadratmeter'].isnull()])        # NaN-Werte
    print(content[content['Quadratmeter'].str.strip() == ''])  # leere Strings
    print(content['Quadratmeter'].str.encode('unicode_escape'))



#Content not homogeneous (Euros, Decimals,) --> Data Cleansing

#Data Cleansing Price
content['Preis'] = content['Preis'].str.replace(r"[^\d]", "", regex=True)
content['Preis'] = content['Preis'].astype(int)

#Data Cleansing Squaremeter
content['Quadratmeter'] = content['Quadratmeter'].str.replace(r"[^\d]", "", regex=True)
content['Quadratmeter'] = content['Quadratmeter'].astype(int)


filter = content[(content['Preis'] < 800) & (content['Quadratmeter'] > 45)] #filter the apartments as price under 700 Euros and size over 45 squaremeter
print(filter.head())

#Cluster Data as Lists of Dicitonarys

def df_to_dictionary():
    df_dict = filter.to_dict()
    print(df_dict)

print(df_to_dictionary)