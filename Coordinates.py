import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import rasterio as rio
from rasterio.plot import show

from pyproj import Proj, transform

import plotly.offline as pyo
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import streamlit as st

#deploy the gui
# map_data = pd.DataFrame(clip[0])
# st.map(map_data)

st.sidebar.write('Enter the coordinates ')
#Longitude
lon_degrees = st.sidebar.text_input('Longitude:', 3.2229167)

#Latitude
lat_degrees = st.sidebar.text_input('Latitude:', 51.2094722)

st.sidebar.text('EPSG:4326 WGS 84 System, dec format')

#Window size
win_size = st.sidebar.slider('Window size', 0, 50, 250, 1)

infile = "./DHMVIIDSMRAS1m_k13.tif"

#convert from wgs84 to lambert coordinates
inProj = Proj(init='epsg:4326')  #EPSG:4326 WGS 84 
outProj = Proj(init='epsg:31370')  #EPSG:31370 Belge 1972 / Belgian Lambert 72
lon0,lat0 = lon_degrees, lat_degrees  #3.227062, 51.214465
lon1,lat1 = transform(inProj,outProj,lon0,lat0)
#print (lon1,lat1)

#coordinates = (lon, lat) # lon, lat of ~centre of Brugge: 3.227062, 51.214465 
# tries : chocolatier Dumon 3.2229167, 51.2094722
#         Groeningen museum: 3.2266112, 51.20525
#         Sint-Anna church: 3.23225, 51.2120556
   
# Your NxN window
N = win_size # 50, 100

# Open the raster
with rio.open(infile) as dataset:

    # Get pixel coordinates from map coordinates
    py, px = dataset.index(lon1, lat1)
    #print('Pixel Y, X coords: {}, {}'.format(py, px))

    # Build an NxN window
    window = rio.windows.Window(px - N//2, py - N//2, N, N)
    #print(window)

    # Read the data in the window
    # clip is a nbands * N * N numpy array
    clip = dataset.read(window=window)
    #show(clip, cmap='terrain')  

# Read data from an array from numpy
df =  pd.DataFrame(clip[0])

fig = go.Figure(data=[go.Surface(z=df.values, colorscale='blugrn')]) #tropic,bupu

fig.update_layout(title='Brugge', autosize=False,# xaxis_autorange="reversed",
                  scene = dict(
                     xaxis = dict(nticks=4, range=[-5,N+5],),
                     yaxis = dict(nticks=4, range=[-5,N+5],),
                     zaxis = dict(nticks=4, range=[3,N*0.7],),),
                  width=800, height=600,
                  margin=dict(l=10, r=10, b=65, t=90))
#fig.show()

st.write(fig)



