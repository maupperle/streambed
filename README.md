## Streambed

This Python library predicts reach-averaged streambed sediment grain size. The implementation is based on Wilkins and Snyder (2011) and Snyder et al. (2012).

[Read more...](https://github.com/nathanlyons/streambed/wiki)

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

#### References

Snyder NP, Nesheim AO, Wilkins BC, Edmonds DA, 2012, Predicting grain size in gravel-bedded rivers using digital elevation models: Application to three Maine watersheds, Geological Society of America Bulletin 43, doi: [10.1130/B30694.1](http://doi.org/10.1130/B30694.1).

Wilkins BC, Snyder NP, 2011, Geomorphic comparison of two Atlantic coastal rivers: Toward an understanding of physical controls on Atlantic salmon habitat, River Research and Applications 27, doi: [10.1002/rra.1343](http://doi.org/10.1002/rra.1343).
