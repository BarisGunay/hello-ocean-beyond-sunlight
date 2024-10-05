import numpy as np
import random

class OceanWorld:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size))  # Chemical concentration grid
        self.lf_grid = np.zeros((size, size))

    def diffuse_chemicals(self, diffusion_rate=0.1):
        new_grid = np.copy(self.grid)
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                # Diffusion formula: averaging with neighbors
                new_grid[i, j] += diffusion_rate * (
                    self.grid[i + 1, j] + self.grid[i - 1, j] + self.grid[i, j + 1] + self.grid[i, j - 1] - 4 * self.grid[i, j]
                )
        self.grid = new_grid

    def add_chemical(self, x, y, amount):
        """Add chemical concentration to a specific cell."""
        self.grid[x, y] += amount

    def get_chemical_concentration(self, x, y):
        """Returns the chemical concentration at a specific position."""
        return self.grid[x, y]
    
    def retrieve_lf_grid(self, life_forms):
        for life_form in life_forms:
            self.lf_grid[life_form.x, life_form.y] += 1

    def display_grid(self, lf_count):
        """Display the chemical grid for visualization."""
        import matplotlib.pyplot as plt

        # Create a figure with two subplots (1 row, 2 columns)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))  # Adjust the figsize as needed
    
        # First subplot for the chemical concentration grid
        cax1 = ax1.imshow(self.grid, cmap='hot')  # Display chemical grid with 'hot' colormap
        fig.colorbar(cax1, ax=ax1, label='H₂S Concentration')
        ax1.set_title('Chemical Concentration in Ocean World')

        # Second subplot for the lifeform map
        cax2 = ax2.imshow(self.lf_grid, cmap='bone')  # Display lifeform grid with 'bone' colormap
        fig.colorbar(cax2, ax=ax2, label='Life Form Count (' + str(lf_count) + ' total)')
        ax2.set_title('Life Form Map in Ocean World')

        # Adjust layout to prevent overlap
        plt.tight_layout()
        plt.show()

class Lifeform:
    def __init__(self, x, y, energy=50):
        self.x = x
        self.y = y
        self.energy = energy
        self.survival_threshold = 10  # Minimum energy required to survive

    def move(self, ocean_world_size):
        """Move randomly across the ocean world."""
        self.x = (self.x + random.choice([-1, 1])) % ocean_world_size
        self.y = (self.y + random.choice([-1, 1])) % ocean_world_size

    def consume_chemicals(self, ocean_world):
        """Consume chemical energy from the environment."""
        chemical_energy = ocean_world.get_chemical_concentration(self.x, self.y)
        if chemical_energy > 15:
            self.energy += chemical_energy * 0.1  # Convert chemical energy to biological energy
            ocean_world.add_chemical(self.x, self.y, -chemical_energy * 0.1)  # Reduce chemical concentration
        self.energy -= 1

    def is_alive(self):
        """Check if the life form is alive."""
        return self.energy > self.survival_threshold
    
    def try_reproduce(self):
        if self.energy < 50:
            return None
        self.energy = self.energy / 2
        child = Lifeform(self.x, self.y, self.energy)
        return child

class HydrothermalVent:
    def __init__(self, x, y, production_rate):
        self.x = x
        self.y = y
        self.production_rate = production_rate

    def release_chemicals(self, ocean_world):
        """Release chemical compounds into the ocean world grid."""
        ocean_world.add_chemical(self.x, self.y, self.production_rate)