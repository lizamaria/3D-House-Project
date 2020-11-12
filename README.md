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
 


 ## The Mission
 > you make a little program that accepts a **coordinate** and shows a nice **3D plot** of the **house** at the location.
 
 ### Must-have features :
    - 3D lookup of houses.
    - Some ideas: when the coordinates be received show:
        - the slope of the ground, which is so humid¡?

 ### Nice-to-have features
    - Optimize your solution to have the result as fast as possible.
    - Features like the living area of the house in m², how many estimated floors, if there is a pool, the vegetation in the neighborhood, etc... 
    - Better visualization.

## Why

## When
    - Duration: `2 weeks`
    - Deadline: `20/11/20 9:00 AM`

## Who.
    Liza-María Candamil
    
### Pending things to do:
- to get lat long coordinates https://rasterio.readthedocs.io/en/latest/topics/reproject.html#reprojection
Reprojection
Rasterio can map the pixels of a destination raster with an associated coordinate reference system and transform to the pixels of a source image with a different coordinate reference system and transform. This process is known as reprojection.
- 