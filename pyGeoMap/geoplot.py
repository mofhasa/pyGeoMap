from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


class pyGeoMap:

    
    def __init__(self, upperRightCorner, lowerLeftCorner, center, shapefiles=None, pins=None):
        '''
        Constructor
        '''
        plt.clf()
        self.shapefiles = None
        self.pins = pins
        self.map = Basemap(llcrnrlon=lowerLeftCorner[1],
                    llcrnrlat=lowerLeftCorner[0],
                    urcrnrlon=upperRightCorner[1],
                    urcrnrlat=upperRightCorner[0],
                    lon_0 = center[1],
                    lat_0 = center[0],
                    resolution='h',
                    projection='merc')
        
        self.figprops = dict(figsize=(8,6), dpi=100, facecolor='white')
        self.fig = plt.figure(id,**self.figprops)
    
        self.map.drawcoastlines()
        self.map.fillcontinents(color='white',lake_color='white')
        self.map.drawmapboundary(fill_color='white')
        
        if shapefiles is not None:
            for x in shapefiles:
                self.map.readshapefile(x, "Dummy TODO")
        
    
    def plot(self, title="Figure", pins=None):
        long = []
        lat = []
        self.setPins(pins)
        
        if self.pins is not None:
            for (l, ll) in self.pins:
                long.append(ll)
                lat.append(l)
            
            
        plt.title(title)
        x,y = self.map(long,lat)
        self.map.plot(x, y, 'bo', markersize=2)
    
    def clear(self):
        plt.clf()
        
    def setPins(self, pins):
        self.pins = pins
        
    
    def saveToPdf(self, path, dpi_setting):
        self.fig.canvas.draw()
        self.fig.savefig(path, dpi=dpi_setting)
                
    