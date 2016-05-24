## Streambed

This Python program predicts reach-averaged streambed sediment grain size. The implementation is based on Wilkins et al. (2011) and Snyder et al. (2012).

#### Installation

Simply download or clone this repository. The python distribution on your computer must include Numpy. 

#### Data Files

Data files can be opened in text editors.

##### .channel files

These files contain stream channel longitudinal parameters. The first line contains the field names. Rows below contain parameter values. Fields are comma separated. The fields are:

1.	x: The x-coordinate of the point along the stream in length units.
2.	y: The y-coordinate of the point along the stream in length units.
3.	elevation: The z-coordinate of the point along the stream in length units.
4.	drainageArea: The upstream drainage area in area units.
5.	distanceFromMouth: The stream-long distance of the point to the mouth.
6.	distanceFromDivide: The stream-long distance of the point to the divide along the longest flowpath.

##### .pebble files

##### .xsection files


#### References

Snyder NP, Nesheim AO, Wilkins BC, Edmonds DA, 2012, Predicting grain size in gravel-bedded rivers using digital elevation models: Application to three Maine watersheds, Geological Society of America Bulletin 43, doi: [10.1130/B30694.1](http://doi.org/10.1130/B30694.1).

Wilkins BC, Snyder NP, 2011, Geomorphic comparison of two Atlantic coastal rivers: Toward an understanding of physical controls on Atlantic salmon habitat, River Research and Applications 27, doi: [10.1002/rra.1343](http://doi.org/10.1002/rra.1343).
