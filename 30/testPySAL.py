import numpy as np
import pysal as ps
import random as rdm
from pysal.contrib.viz import mapping as maps
from pylab import *
from matplotlib.collections import LineCollection


def multiClassification():
    shp = ps.open(r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\30\texas.shp")
    dbf = ps.open(r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\30\texas.dbf")
    # some = [bool(rdm.getrandbits(1)) for i in ps.open(r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\30\texas.shp")]
    values = np.array(ps.open(r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\30\texas.dbf").by_col("HR90"))
    types = ["classless", "unique_values", "quantiles", "equal_interval","fisher_jenks"]
    for typ in types:
        maps.plot_choropleth(r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\30\texas.shp",values,typ,title=typ)

def geoPandaWay():
    shp_link = r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\30\texas.shp"
    tx = gpd.read_file(shp_link)
    tx.plot(color='blue')
    tx.plot(column='HR90', scheme='QUANTILES')

def w2line_graph(w, cents):
    segments = []
    for i in w.id2i:
        origin = cents[i]
        for j in w.neighbors[i]:
            dest = cents[j]
            ij = [i,j]
            ij.sort()
            segments.append([origin, dest])
    #segs = LineCollection(segments)
    
    #maps._add_axes2col(segs, [minx, miny, maxx, maxy])
    return segments  

def taz():
    shp = ps.open(ps.examples.get_path("taz.shp"))
    dbf = ps.open(ps.examples.get_path("taz.dbf"))
    wrook = ps.rook_from_shapefile(ps.examples.get_path("taz.shp"))
    cnty = np.array(dbf.by_col("CNTY"))
    fig = figure(figsize=(9,9))
    base = maps.map_poly_shp(shp)
    base.set_linewidth(0.75)
    base.set_facecolor('none')
    base.set_edgecolor('0.8')
    counties = maps.base_choropleth_unique(maps.map_poly_shp(shp), cnty)
    counties.set_linewidth(0)
    counties.set_alpha(.5)
    cents = np.array([poly.centroid for poly in shp])
    segs = w2line_graph(wrook, cents)

multiClassification()
