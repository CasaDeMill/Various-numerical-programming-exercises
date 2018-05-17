# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 14:55:59 2016

@author: Martin
"""
from scipy import *
from pylab import *
import sys
from mpl_toolkits.mplot3d import axes3d 
from mpl_toolkits.basemap import Basemap

X,Y,Z = axes3d.get_test_data(0.05)

fig = figure()
ax=fig.gca(projection='3d')
ax.plot_surface(X,Y,Z, alpha=0.5)

#m=Basemap(projection='merc',llcrnrlat=-10, urcrnrlat=80, llcrnrlon=-140, urcrnrlon=100,lat_ts=40, resolution='c')
#
#
#m.drawcoastlines()
#m.drawcountries()
#
#sea_lat,sea_lon=47.448889, -122.30944
#arn_lat,arn_lon=59.651944,17.918611
#
#m.drawgreatcircle(arn_lon, arn_lat, sea_lon, sea_lat, linewidth=1.5)