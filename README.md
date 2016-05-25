## Streambed

This Python library predicts reach-averaged streambed sediment grain size. The implementation is based on Wilkins and Snyder (2011) and Snyder et al. (2012).

#### Installation

Simply download or clone this repository. The Python distribution on your computer must include Numpy. 

#### Quick start

Set parameters:
```python
parameters = streambed.Parameters(root + '/exampleData/')
```
Initialize channel:
```python
channel = streambed.Channel(parameters.dataDirectory + 'LittleRiver.channel')
```

#### Data Files

Data files can be opened in text editors.

##### .channel Files

These files contain channel parameters at points along a stream. The first line contains the field names. Rows below contain parameter values. Fields are comma separated. The fields are:

1.	x: The x-coordinate of the point along the stream.
2.	y: The y-coordinate of the point along the stream.
3.	elevation: The z-coordinate of the point along the stream.
4.	drainageArea: The upstream area that drains to the point.
5.	distanceFromMouth: The stream-long distance from the stream mouth to the point.

##### .pebble Files

<TODO>

##### .xsection Files

<TODO>

#### References

Snyder NP, Nesheim AO, Wilkins BC, Edmonds DA, 2012, Predicting grain size in gravel-bedded rivers using digital elevation models: Application to three Maine watersheds, Geological Society of America Bulletin 43, doi: [10.1130/B30694.1](http://doi.org/10.1130/B30694.1).

Wilkins BC, Snyder NP, 2011, Geomorphic comparison of two Atlantic coastal rivers: Toward an understanding of physical controls on Atlantic salmon habitat, River Research and Applications 27, doi: [10.1002/rra.1343](http://doi.org/10.1002/rra.1343).
