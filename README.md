## Streambed

This Python library predicts reach-averaged streambed sediment grain size.

[Read more...](https://github.com/nathanlyons/streambed/wiki)

#### Installation

Simply download or clone this repository. The Python distribution on your computer must include Numpy. 

#### Quick start

Set parameters:
```python
parameters = streambed.Parameters(os.getcwd() + '/exampleData/')
```
Initialize channel:
```python
channel = streambed.Channel(parameters.dataDirectory + 'LittleRiver.channel')
```
