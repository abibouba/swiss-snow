[![PyPI Version](https://img.shields.io/pypi/v/swiss-snow.svg)](https://pypi.org/project/swiss-snow/)


# swiss-snow
A Python module for accessing swiss snow conditions and resort status. No API key is required.

## Sources
- Verbier/4 vallées: http://www.infosnow.ch/~apgmontagne/?lang=en&pid=31

## Installation
```python
$ pip install swiss-snow
```

## Usage
```python
import swiss_snow

# Initiate the Resorts object
resorts = swiss_snow.Resorts()

# Get the list of available resorts
list_of_resorts = resorts.list_resorts
print(list_of_resorts)

# Get data for one of the resort
condition_verbier = resorts.conditions("Verbier")
print(condition_verbier)

# Get detailed snow levels for the resort previously selected
for snow_condition in condition_verbier.conditions:
    print(snow_condition)
```

## Exemple output
```python
['Verbier']

Verbier - 4 vallées - Avalanche risk: 0 - Open slopes: 0/48 - Open lifts: 0/33 - Last update: 2020-06-12 11:24:00

Verbier (1500 m): 50 cm - Fresh snow: 0 cm
Les Ruinettes (2200 m): 230 cm - Fresh snow: 0 cm
Les Gentianes (2950 m): 385 cm - Fresh snow: 0 cm
```

## Features

- List all resorts available
- Get the following information: avalanche risk level, number of slopes and lifts opened, detailed snow conditions

## Coming next

- Add more resorts
- Get detailed 