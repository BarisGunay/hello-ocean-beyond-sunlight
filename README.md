# Beyond Sunlight: An Aquatic Chemosynthetic World

## (DEMO INCLUDED IN PRESENTATION)

**Project Name**: Hello Ocean  
**Challenge**: NASA Space Apps 2024 - Beyond Sunlight: An Aquatic Chemosynthetic World  
**Team Members**:  
- Barış Günay  
- İsmail Kaan Sönmez  

## Project Description

This project simulates life in an ocean world devoid of sunlight, mimicking environments such as the subsurface oceans of Jupiter's moon **Europa** and Saturn's moon **Enceladus**. These worlds are hypothesized to host life forms that rely on **chemosynthesis**, a process by which organisms convert chemical energy from compounds like hydrogen sulfide into usable energy, as opposed to photosynthesis which requires sunlight.

In our simulation, we model an ecosystem driven by hydrothermal vents that release chemicals to sustain autotrophic and heterotrophic organisms. The simulation shows how these life forms interact, metabolize chemical compounds, and reproduce in a world without sunlight.

## Features

- **2D Simulation Grid**: A virtual ocean environment where chemical concentrations, autotrophs, and heterotrophs are tracked and visualized.
- **Hydrothermal Vent System**: Randomly placed vents release hydrogen sulfide (H₂S), providing energy for autotrophs.
- **Lifeform Interactions**: Autotrophs convert chemical energy to biological energy, while heterotrophs consume autotrophs to survive.
- **Visualization**: Real-time display of the ocean grid with heatmaps representing chemical concentration and organism distribution.
- **Adjustable Parameters**: A user-friendly interface allows experimentation with different parameters like the number of autotrophs, heterotrophs, and vents, as well as the chemical production rate.

## Code Overview

### `simulation.py`
This script handles the core simulation logic:
- **`OceanWorld`**: Manages the grid for chemical diffusion and lifeform interactions.
- **`HydrothermalVent`**: Represents vents that release chemicals.
- **`Autotroph` and `Heterotroph`**: Classes for lifeforms that metabolize chemicals and reproduce.
- **Simulation Loop**: The simulation runs for a set number of steps, evolving the ecosystem based on chemical availability and lifeform interactions. Results are displayed in heatmaps at the end of each run.

### `environment.py`
Defines the environment for the simulation, including the diffusion of chemicals across the grid and the release of chemicals by hydrothermal vents. It also manages the visualization of the simulation results using Matplotlib.

### `ui.py`
Provides a user-friendly interface using **Tkinter**. The UI allows users to input parameters (e.g., world size, number of autotrophs, heterotrophs, hydrothermal vents, etc.) and run the simulation with ease. The preferred values for a balanced ecosystem are preloaded.

## Installation

1. Clone the repository

```bash
   git clone https://github.com/BarisGunay/hello-ocean.git
```

2. Install the required Python packages.

```bash
   pip install numpy matplotlib
```

3. Run the simulation with the UI.

```bash
   python ui.py
```

## Dependencies

- Python 3.x
- Numpy
- Matplotlib
- Tkinter

Ensure all dependencies are installed.

## How to Use

1. Launch the simulation using the UI.
2. Enter desired simulation parameters (or leave blank to use default values).
3. Click **Run Simulation** to start the simulation.
4. Watch the real-time progress as the simulation displays chemical concentrations, autotroph, and heterotroph distributions.

## Example Output

- The simulation will output a series of heatmaps that show the concentration of chemicals, and the distribution of autotrophs and heterotrophs in the environment.
- Autotrophs tend to cluster around hydrothermal vents where chemical energy is highest, while heterotrophs congregate near autotrophs to feed.

## Results & Key Findings

- Autotrophs reproduce as long as chemical concentrations are sufficient around hydrothermal vents.
- Heterotrophs depend on autotrophs for energy, creating a fragile balance that can collapse if resources become scarce.
- Our simulation suggests that life, even in extreme environments like those found on Europa or Enceladus, could sustain itself through chemosynthesis.

## Future Improvements

- Expand the simulation to model additional types of lifeforms or chemical reactions.
- Incorporate machine learning algorithms to simulate evolution and adaptation over time.
- Add more complex environmental factors, such as varying temperatures or pressure.

## References

1. V. Da Poian, B. Theiling, L. Clough, et al., "Exploratory data analysis (EDA) machine learning approaches for ocean world analog mass spectrometry," *Frontiers in Astronomy and Space Sciences*, vol. 10, May 2023. DOI: 10.3389/fspas.2023.1134141.
2. C. Q. Choi, "Hydrothermal Vent Experiments Bring Enceladus to Earth," *Astrobiology*, NASA, Dec. 2017. Available: https://astrobiology.nasa.gov/news/hydrothermal-vent-experiments-bring-enceladus-to-earth/
3. NASA Science, "Life Signs Could Survive Near Surfaces of Enceladus and Europa," *NASA Science*, Jul. 2024. Available: https://science.nasa.gov/science-research/planetary-science/astrobiology/nasa-life-signs-could-survive-near-surfaces-of-enceladus-and-europa/
