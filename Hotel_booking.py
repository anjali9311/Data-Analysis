# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:25:22 2024

@author: Anjali
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import warnings warning.fliterwarnings('ignore')
df=pd.read_csv(r"C:\\Users\\Anjali\\Desktop\\college\\projects\\hotel_booking.csv")
print(df)

df.head()

df.tail()

df.shape

df.columns
df.info()

df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])
df.info()

df.describe()
df.describe(include='object')

for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    print("_"*50)

df.isnull().sum()

df.drop(['company','agent'], axis=1,inplace=True)
df.dropna(inplace=True)
df.isnull().sum()

df.describe()

df['adr'].plot(kind="box")

df=df[df['adr']<5000]
df.describe()

cancelled_perc=df['is_canceled'].value_counts(normalize=True)
cancelled_perc

print(cancelled_perc)

plt.figure(figsize=(5,4))
plt.title("Reservation Status Count")
plt.bar(['Not Cancelled','Cancelled'],df['is_canceled'].value_counts())
plt.show


plt.figure(figsize = (8,4))
axl = sns.countplot(x = 'hotel', hue = 'is_canceled', data = df, palette = 'Blues')
legend_labels,_ =axl.get_legend_handles_labels()
axl.legend("bbox_to_anchor"(1,1))
plt.title("Reservation Status In Different Hotel", size = 20)
plt.xlabel('hotel')
plt.ylabel('number of reservation')


resot_hotel = df[df['hotel']=='Resort Hotel']
resot_hotel['is_canceled'].value_counts(normalize=True)

city_hotel = df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)

resot_hotel = resot_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()

plt.figure(figsize=(20,8))
plt.title('Average Daily Rate In City And Resot Hotel', fontsize = 30)
plt.plot(resot_hotel.index,resot_hotel['adr'],label='Resot Hotel')
plt.plot(city_hotel.index,city_hotel['adr'],label='City Hotel')

df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize = (16,8))
axl = sns.countplot(x = 'month', hue = 'is_canceled', data = df, palette = 'pink')
legend_labels,_ =axl.get_legend_handles_labels()
axl.legend("bbox_to_anchor"(1,1))
plt.title("Reservation Status Per Month", size = 20)
plt.xlabel('month')
plt.ylabel('number of reservation')
plt.legend(['not canceled','canceled'])
plt.show()


plt.figure(figsize=(15, 8))
plt.title('ADR per Month', fontsize=30)
data = df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index()
sns.barplot(x='month', y='adr', data=data, palette='viridis')
plt.xlabel('Month', fontsize=20)
plt.ylabel('Average Daily Rate (ADR)', fontsize=20)
plt.show()


cancelled_data = df[df['is_canceled'] == 1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title("Top 10 Countries Reservation Cancelled")
plt.pie(top_10_country, autopct = '%.2f', labels=top_10_country.index)
plt.show()

df['market_segment'].value_counts()
df['market_segment'].value_counts(normalize = True)

cancelled_data['market_segment'].value_counts(normalize = True)

cancelled_df_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace = True)
cancelled_df_adr.sort_values('reservation_status_date', inplace = True)


not_cancelled_data= df[df['is_canceled'] == 0]
not_cancelled_df_adr = not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace = True)
not_cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

plt.figure(figsize = (20,6))
plt.title("Average Daily Rate")
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label='not_cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'],label='cancelled')
plt.legend()

cancelled_df_adr=cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016')&(cancelled_df_adr['reservation_status_date']<'2017-09')]
not_cancelled_df_adr=not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016')&(not_cancelled_df_adr['reservation_status_date']<'2017-09')]

plt.figure(figsize = (20,6))
plt.title("Average Daily Rate")
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label='not_cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'],label='cancelled')
plt.legend()

























