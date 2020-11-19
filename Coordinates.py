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

st.sidebar.write('Insert your coordinates ')
#Longitude
lon_degrees = st.sidebar.text_input('Longitude:', 3.0)

#Latitude

lat_degrees = st.sidebar.text_input('Latitud:', 51.0)

st.sidebar.text('EPSG:4326 WGS 84 System, dec format')

infile = "./DHMVIIDSMRAS1m_k13.tif"

#convert from wgs84 to lambert coordinates
inProj = Proj(init='epsg:4326')  #EPSG:4326 WGS 84 
outProj = Proj(init='epsg:31370')  #EPSG:31370 Belge 1972 / Belgian Lambert 72
lon0,lat0 = lon_degrees, lat_degrees  #3.227062, 51.214465
lon1,lat1 = transform(inProj,outProj,lon0,lat0)
#print (lon1,lat1)

#coordinates = (lon, lat) # lon, lat of ~centre of Brugge: 3.227062, 51.214465 
   
# Your NxN window
N = 100

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

fig = go.Figure(data=[go.Surface(z=df.values)])

fig.update_layout(title='Brugge', autosize=False,
                  width=700, height=700,
                  margin=dict(l=50, r=50, b=65, t=90))
#fig.show()

st.write(fig)



