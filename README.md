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
