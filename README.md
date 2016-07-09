This package is not yet fully functional.

## Streambed

This Python library predicts reach-averaged streambed sediment grain size.

[Read more...](https://github.com/nathanlyons/streambed/wiki)

<<<<<<< HEAD
<<<<<<< HEAD
#### User Installation

The Python distribution on your computer must include MapPlotLib, Numpy, and setuptools. Consider using [Anaconda](https://www.continuum.io/downloads), a  Python distribution that is preassembled with many scientific and analytic packages.
=======
#### Installation
>>>>>>> refs/remotes/nathanlyons/master
=======
#### Installation
>>>>>>> refs/remotes/nathanlyons/master

If you wish to use the library as-is, follow the [User Installation](https://github.com/nathanlyons/streambed/wiki/User-Installation) instructions.

Those who wish to modify and contribute to this library should follow the
[Developer Installation](https://github.com/nathanlyons/streambed/wiki/Developer-Installation) instructions.

#### Example usage

Initialize a model by inputing the directory that contains data files:
```python
model = streambed.Model('/tutorials/exampleData/')
```
Print the domains in the data directory dictionary:
```python
print(model.domain.keys()) 
# ['LittleRiver', 'NiagaraCarthrage-78', 'SandhillsGages']
```
Plot channel parameters:
```python
channel = streambed.Channel(model.domain['LittleRiver'])
channel.plot()
```

See more in the [example model script](https://github.com/nathanlyons/streambed/blob/master/tutorials/littleRiverModeling.py).
