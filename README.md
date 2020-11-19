# 3D-House-Project

 The results we're interested in are DSM (Digital Surface Map) and DTM (Digital Terrain Map).
 Which are already computed and available here :
 - [DSM](http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dsm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DSM,%20raster,%201m)
 - [DTM](http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dtm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DTM,%20raster,%201m)
 
 Deployment strategy :
	 Github page
	| Powerpoint
	| Jupyter Notebook x
	| Webpage 
	| App 
      localhost x
      
## What 

 ### The Mission
 > you make a little program that accepts a **coordinate** and shows a nice **3D plot** of the **house** at the location.
  in other words, when the coordinates be received show:  3D plot from DSM data set
 ### Must-have features :
    - 3D lookup of houses. 
      
 ### Nice-to-have features
    - Optimize your solution to have the result as fast as possible.
    - Features like the living area of the house in m², how many estimated floors, if there is a pool, the vegetation in the neighborhood, etc... 
    - Better visualization.
   
## How: 

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

## Who
    -Liza María Candamil

## When
    - Duration: `2 weeks`
    - Deadline: `20/11/20 9:00 AM` 
    
 ### Done: cecked     

- to get lat long coordinates https://rasterio.readthedocs.io/en/latest/topics/reproject.html#reprojection
    Check with this https://gis.stackexchange.com/questions/299787/finding-pixel-location-in-raster-using-coordinates/299791#299791
    
- convert from wgs84 to lambert coordinates rasterio    
https://gis.stackexchange.com/questions/78838/converting-projected- 
- do the 3D plot:
    * Using matplotlib: https://stackoverflow.com/questions/41960448/matplotlib-3d-surface-plot-from-2d-pandas-dataframe 
        
    * Using plotly: https://plotly.com/python/3d-surface-plots/ 
        plotly 3d jupyter notebook not showing
        for using this library I had to install the jupyter lab plotly extension (in Anaconda terminal): https://stackoverflow.com/a/55955851/14449195
        npm anaconda install
        And when I was installing this was required to install node.js and npm (in Anaconda Navigator)     
    - so I had to activate the enviaroment in Anaconda prompt with >> `conda activate House-Project-3D`
    - Then >> `pip install streamlit`
    - Finally I can get my 3D plot with streamlit
    
    
- Make an app to recieve and show the coordinates in the map (3d graphic deploy) with streamlit:https://www.youtube.com/watch?v=B2iAodr0fOo
    streamlit anaconda install: https://discuss.streamlit.io/t/install-streamlit-with-anaconda/714
    tutos: https://www.analyticsvidhya.com/blog/2020/10/create-interactive-dashboards-with-streamlit-and-python/
    
    install streamlit and display the text in different ways: https://www.analyticsvidhya.com/blog/2020/10/create-interactive-dashboards-with-streamlit-and-python/
    tuto:https://docs.streamlit.io/en/stable/api.html#display-text
         https://docs.streamlit.io/en/latest/getting_started.html (get started)
         https://docs.streamlit.io/en/stable/api.html#streamlit.set_page_config
         https://plotly.com/python/3d-axes/ (to smooth the pikes)
         https://plotly.com/python/colorscales/ (color scales!)
        
    streamlit videotuto: https://www.youtube.com/watch?v=VtrFjkSGgKM
                         https://www.youtube.com/watch?v=B2iAodr0fOo (slide)
                         https://www.youtube.com/watch?v=_9WiB2PDO7k
    
    
    other option: simple gui python: https://realpython.com/pysimplegui-python/
    example simple gui https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-pattern-1a-one-shot-window-the-simplest-pattern

- Try with diferent places like: lon, lat
    
    grote_markt_bruges:  3.224273, 51.208903
    De Garre 1, 8000 Brugge: 3.225766, 51.208454
    the given coordinates:    
    - chocolatier Dumon:  3.2229167, 51.2094722
    - Groeningen museum: 3.2266112, 51.20525
    - Sint-Anna church: 3.23225, 51.2120556
 
 ###  Pending things to do:
 
- Features like the living area of the house in m², how many estimated floors, if there is a pool, the vegetation in the neighborhood, etc... 
- Better visualization.-->look for a better dataframe