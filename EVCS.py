#import the libraries that are required for the analysis. 
#pandas is for dataframe construction and manipulation; 
#folium is for generalising visualisation of data on an interative map.
import pandas as pd
import folium

#import and read the CSV file into Python using pandas.
EV_df = pd.read_csv("C:\\Users\kcho4\OneDrive\Desktop\Project _Python\EV Charging Stations in NSW\EVCS.csv",sep=";")
# constructive a data frame including all the important columns and rows.
EVCS_df = pd.DataFrame(EV_df, columns=['Organisation_Name','Service_Station_Location','Lat_decrypted','Long_decrypted'])
# replacing the commas of the coordinates with dots.
EVCS_coord = EVCS_df['Lat_decrypted'].replace(',','.', regex=True)

EVCS_df['Lat_decrypted'] = EVCS_df['Lat_decrypted'].str.replace(',','.') 
EVCS_df['Long_decrypted'] = EVCS_df['Long_decrypted'].str.replace(',','.')
EVCS_df.head()

EVCS_df['Lat_decrypted'] = pd.to_numeric(EVCS_df['Lat_decrypted'])
EVCS_df['Long_decrypted'] = pd.to_numeric(EVCS_df['Long_decrypted'])

EVCS_df['Organisation_Name'].value_counts()

for i in range(0,len(EVCS_df)):
    num_Organisation = EVCS_df['Organisation_Name'].iloc[i]
    if num_Organisation == 'National Roads and Motorists Association Limited':
        color = 'blue'
    elif num_Organisation == 'Telsa Motors Australia Pty Ltd':
        color = 'green'
    elif num_Organisation == 'Wilson Parking Australia 1992 Pty Ltd':
        color = 'black'
    elif num_Organisation == 'Srinivasa Fuels Pty Ltd':
        color = 'orange'
    else:
        color = 'red'
    
    popup = folium.Popup(num_Organisation)
    folium.Marker([EVCS_df['Lat_decrypted'].iloc[i],EVCS_df['Long_decrypted'].iloc[i]],popup=popup,icon=folium.Icon(color=color, icon='info-sign')).add_to(map)

map
