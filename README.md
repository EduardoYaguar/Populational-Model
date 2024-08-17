# Predator-Prey Population Model

This project, created by **Eduardo Yaguar Falconí**, simulates and visualizes the relationship between predator and prey populations over time using the Lotka-Volterra equations.

## Description

The application uses a modified version of the Lotka-Volterra model, incorporating additional variables to make the simulation more realistic. The model assumes that predators only die from natural causes and prey only die when hunted by predators.

The population dynamics are described by the following discrete equations:

### Prey equation:
R(n+1) = R(n) + aR(n)(1 - R(n)/k) - bR(n)F(n)

### Predator equation:
F(n+1) = F(n) + fbR(n)F(n) - cF(n)

Where:
- n: Cycle number
- R(n): Prey population after n cycles
- F(n): Predator population after n cycles
- a: Intrinsic growth rate of prey
- K: Carrying capacity of the environment for prey
- b: Per capita attack rate of predators on prey
- f: Conversion rate of consumed prey into new predators
- c: Natural mortality rate of predators per capita

## Features

- Interactive graph showing predator and prey populations over time
- Real-time updates as parameters are adjusted
- Sliders for controlling model parameters:
  - 'a': Intrinsic growth rate of prey
  - 'b': Per capita attack rate of predators on prey
  - 'c': Natural mortality rate of predators
  - 'f': Conversion rate of consumed prey into new predators

## Requirements

- Python 3.8 or later
- Dependencies:
  - customtkinter
  - Matplotlib
  - Numpy

## Installation

1. Clone this repository
   `git clone https://github.com/username/predator-prey-model.git`  

3. Install the required dependencies:
   `pip install customtkinter matplotlib numpy`  

## Usage

Run the `App.py` file to start the application:  
`python App.py`  
Use the sliders to adjust the model parameters and observe how they affect the population dynamics in real-time.


## License

MIT License

## Author

YAGUAR FALCONI, Eduardo
