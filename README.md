This package is not yet fully functional.

## Streambed

This Python library predicts reach-averaged streambed sediment grain size.

[Read more...](https://github.com/nathanlyons/streambed/wiki)

#### User Installation

The Python distribution on your computer must include MapPlotLib, Numpy, and setuptools. Consider using [Anaconda](https://www.continuum.io/downloads), a  Python distribution that is preassembled with many scientific and analytic packages.

Install using pip in the terminal or command prompt (Windows). See [this page](https://pip.pypa.io/en/stable/installing) if pip is not installed on your computer.

```bash
pip install streambed
```

Streambed is now installed in the site-packages directory of your Python distribution.

The library can be uninstalled also using the command line.
```bash
pip uninstall streambed
```

[Developer installation](https://github.com/nathanlyons/streambed/wiki/Developer-Installation)

#### Example usage

Initialize a model by inputing the directory that contains data files:
```python
model = streambed.Model('/tutorials/exampleData/')
```
Plot channel parameters:
```python
channel = streambed.Channel(model.domain['LittleRiver'])
channel.plot()
```
