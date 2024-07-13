# Sand Simulation

A simple sand simulation implemented using Python and Pygame, with dynamic colors changing over time. The simulation allows you to draw sand particles on the screen, which then fall and stack based on simple physics rules.

## Features

- **Dynamic Coloring**: Sand particles change color over time using HSB (Hue, Saturation, Brightness) color model.
- **Interactive Drawing**: Draw sand particles by clicking and dragging the mouse.
- **Realistic Sand Movement**: Particles fall straight down and spread diagonally if obstructed.

## Installation

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
2. Install the required library:

   ```bash
   pip install pygame
   ```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/sand-simulation.git
   cd sand-simulation
   ```
2. Run the simulation:

   ```bash
   python main.py
   ```
3. Click and drag the mouse to create sand particles on the screen.

## Code Overview

### `main.py`

The main file contains the following sections:

- **Imports and Initialization**:

  - Import required libraries (`pygame`, `random`, `colorsys`).
  - Initialize Pygame and set up display parameters.
- **Color Conversion Function**:

  - `hsb_to_rgb(h, s, b)`: Converts HSB color values to RGB.
- **Sand Simulation Functions**:

  - `draw_grid()`: (Optional) Draws grid lines on the display for visualization.
  - `create_sand(positions)`: Handles the sand movement logic and draws the sand particles on the display.
- **Main Loop**:

  - Handles user input (mouse events) to draw sand particles.
  - Updates the display with sand particles and handles their movement.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Pygame](https://www.pygame.org/) - The library used to create this simulation.
- [colorsys](https://docs.python.org/3/library/colorsys.html) - Python module for color system conversions.

## Video Demo

Watch the demo video below to see the sand simulation in action:

[![Sand Simulation Video](https://img.youtube.com/vi/hHPicUZk6TY/0.jpg)	](https://www.youtube.com/watch?v=hHPicUZk6TY)

---

Enjoy the simulation!
