## Streambed

This Python library predicts reach-averaged streambed sediment grain size.

[Read more...](https://github.com/nathanlyons/streambed/wiki)

#### User Installation

The Python distribution on your computer must include Numpy.

Install using pip in the terminal or command prompt (Windows). See [this page](https://pip.pypa.io/en/stable/installing) if pip is not installed on your computer

```bash
pip install streambed
```

[Developer installation](https://github.com/nathanlyons/streambed/wiki/Developer-Installation)

#### Quick start

Set parameters:
```python
parameters = streambed.Parameters(os.getcwd() + '/exampleData/')
```
Initialize channel:
```python
channel = streambed.Channel(parameters.dataDirectory + 'LittleRiver.channel')
```
