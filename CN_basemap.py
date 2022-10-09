#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2022/7/4 12:04
# @Author  : weather
# @Software: PyCharm
"""

import geopandas as gpd
import cartopy.crs as ccrs
import numpy as np
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.pyplot as plt


def main():
    china = gpd.read_file('./china_map/中国省级地图GS（2019）1719号.geojson')
    nine = gpd.read_file('./china_map/九段线GS（2019）1719号.geojson')

    fig = plt.figure(figsize=(5,4))
    ax = fig.add_subplot(projection=ccrs.LambertConformal(central_longitude=105, standard_parallels=(25, 47)))
    nine.plot(ax=ax,transform=ccrs.PlateCarree(),facecolor='w',edgecolor='k',lw=1)
    china.plot(ax=ax,transform=ccrs.PlateCarree(),facecolor='w',edgecolor='k',lw=1,zorder=3)
    ax.set_extent([74, 136, 14, 56],crs=ccrs.PlateCarree())
    gl = ax.gridlines(draw_labels=True,linewidth=1, color='gray', alpha=0.5, linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.x_inline = False
    gl.xlocator = mticker.FixedLocator([80, 90, 100, 110, 120, 130])
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.rotate_labels = False
    gl.xpadding = 7

    sub_ax = fig.add_axes([0.72, 0.1, 0.15, 0.3], projection=ccrs.LambertConformal(standard_parallels=(25, 47),
                                                                                   central_longitude=115))
    china.plot(ax=sub_ax, transform=ccrs.PlateCarree(), facecolor='w', edgecolor='k', lw=1, zorder=2)
    nine.plot(ax=sub_ax, transform=ccrs.PlateCarree(), facecolor='w', edgecolor='k', lw=2)
    sub_ax.set_extent([100, 125, 0, 25])
    plt.savefig('./china_map.tiff',dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
