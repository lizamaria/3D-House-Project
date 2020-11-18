# 3D-House-Project

 The results we're interested in are DSM (Digital Surface Map) and DTM (Digital Terrain Map).
 Which are already computed and available here :
 - [DSM](http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dsm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DSM,%20raster,%201m)
 - [DTM](http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dtm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DTM,%20raster,%201m)
 
 Deployment strategy :
	 Github page
	| Powerpoint
	| Jupyter Notebook
	| Webpage
	| App
## How: so far...
0. Download the data and understand new diferent concepts

    -DIFERENCIAS ENTRE UN DSM, DEM & DTM https://www.youtube.com/watch?v=TjnM4r5c4zw 

1. Discover how the data can be read
    -This article discusses different ways of reading and visualizing these images with python using a jupyter notebook. The libraries      used are GDAL, rasterio, georaster, and Matplotlib(for visualization).https://towardsdatascience.com/reading-and-visualizing-geotiff-images-with-python-8dcca7a74510 

2. Install all the tools I need:
    -libraries: 
        richdem: for DEM anlysis
        rasterio: mainly for reading and writing raster data
        geopandas
        shapely: created geopoint objects or geopandas
3. How to find the right zip to download
    -http://www.geopunt.be/kaart?type=service&data=[%27https%3A%2F%2Fgeoservices.informatievlaanderen.be%2Fraadpleegdiensten%2FDHMV%2Fwms%3F%27]
    -http://epsg.io/map#srs=31370&x=69253.78&y=213645.63&z=11&layer=streets
    -https://epsg.io/transform#s_srs=31370&t_srs=4326&x=70137.0600000&y=211813.5200000

        

  
## What 
 extract the coordinates from the tif or (shp file could be?)
 https://gis.stackexchange.com/questions/299787/finding-pixel-location-in-raster-using-coordinates/299791#299791
 


 ## The Mission
 > you make a little program that accepts a **coordinate** and shows a nice **3D plot** of the **house** at the location.
 
 ### Must-have features :
    - 3D lookup of houses.
    - Some ideas: when the coordinates be received show:   3D plot from DSM data set
        - the slope of the ground, which is so humid¡?

 ### Nice-to-have features
    - Optimize your solution to have the result as fast as possible.
    - Features like the living area of the house in m², how many estimated floors, if there is a pool, the vegetation in the neighborhood, etc... 
    - Better visualization.
    - Deadline: `20/11/20 9:00 AM`

## Who.

## Why

## When
    - Duration: `2 weeks`
    Liza-María Candamil
    

- to get lat long coordinates https://rasterio.readthedocs.io/en/latest/topics/reproject.html#reprojection
    Check with this https://gis.stackexchange.com/questions/299787/finding-pixel-location-in-raster-using-coordinates/299791#299791
    
- convert from wgs84 to lambert coordinates rasterio    
https://gis.stackexchange.com/questions/78838/converting-projected- 
- do the 3D plot:
    * Using matplotlib: https://stackoverflow.com/questions/41960448/matplotlib-3d-surface-plot-from-2d-pandas-dataframe 
        
    * Using plotly: https://plotly.com/python/3d-surface-plots/ 
    
        for using this library I had to install the jupyter lab plotly extension (in Anaconda terminal): https://stackoverflow.com/a/55955851/14449195
        And when I was installing this was required to install node.js and npm (in Anaconda Navigator)     
    - so I had to activate the enviaroment in Anaconda prompt with >> `conda activate House-Project-3D`
    - Then >> `pip install streamlit`
    - Finally I can get my 3D plot with streamlit
    
  plotly 3d jupyter notebook not showing so 

### Pending things to do:    
- Make a web app to recieve and show the coordinates in the map with streamlit:https://www.youtube.com/watch?v=B2iAodr0fOo


