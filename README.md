This package is not yet fully functional.

## Streambed

This Python library predicts reach-averaged streambed sediment grain size.

[Read more...](https://github.com/nathanlyons/streambed/wiki)

#### Installation

If you wish to use the library as-is, follow the [User Installation](https://github.com/nathanlyons/streambed/wiki/User-Installation) instructions.

Those who wish to modify and contribute to this library should follow the
[Developer Installation](https://github.com/nathanlyons/streambed/wiki/Developer-Installation) instructions.

#### Example usage

Initialize a model by inputing the directory that contains data files:
```python
model = streambed.Model('/tutorials/exampleData/')
```
 $ python model = streambed.Model('/tutorials/exampleData/')

Print the domains in the data directory dictionary
```python
print(model.domain.keys())
```
Plot channel parameters:
```python
channel = streambed.Channel(model.domain['LittleRiver'])
channel.plot()
```
