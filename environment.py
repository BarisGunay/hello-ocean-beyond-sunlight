import numpy as np
import random

class OceanWorld:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size))  # Chemical concentration grid
        self.autotroph_grid = np.zeros((size, size))
        self.heterotroph_grid = np.zeros((size, size))

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
    
    def retrieve_lifeform_grids(self, autotrophs, heterotrophs):
        for autotroph in autotrophs:
            self.autotroph_grid[autotroph.x, autotroph.y] += 1
        
        for heterotroph in heterotrophs:
            self.heterotroph_grid[heterotroph.x, heterotroph.y] += 1

    def display_grid(self, autotroph_count, heterotroph_count):
        # Display the chemical, autotroph, and heterotroph grids for visualization. 
        import matplotlib.pyplot as plt

        # Create a figure with three subplots (1 row, 3 columns)
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))  # Adjust the figsize as needed

        # First subplot for the chemical concentration grid
        cax1 = ax1.imshow(self.grid, cmap='hot')  # Display chemical grid with 'hot' colormap
        fig.colorbar(cax1, ax=ax1, label='H₂S Concentration')
        ax1.set_title('H₂S Concentration in Ocean World')

        # Second subplot for the autotroph map
        cax2 = ax2.imshow(self.autotroph_grid, cmap='bone')  # Display autotroph grid with 'bone' colormap
        fig.colorbar(cax2, ax=ax2, label='Autotroph Count (' + str(autotroph_count) + ' total)')
        ax2.set_title('Autotroph Map in Ocean World')

        # Third subplot for the heterotroph map
        cax3 = ax3.imshow(self.heterotroph_grid, cmap='cool')  # Display heterotroph grid with 'cool' colormap
        fig.colorbar(cax3, ax=ax3, label='Heterotroph Count (' + str(heterotroph_count) + ' total)')
        ax3.set_title('Heterotroph Map in Ocean World')

        # Adjust layout to prevent overlap
        plt.tight_layout()
        plt.show()

class HydrothermalVent:
    def __init__(self, x, y, production_rate):
        self.x = x
        self.y = y
        self.production_rate = production_rate

    def release_chemicals(self, ocean_world):
        """Release chemical compounds into the ocean world grid."""
        ocean_world.add_chemical(self.x, self.y, self.production_rate)

class Lifeform:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.energy = energy
        self.survival_threshold = 10  # Minimum energy required to survive

    def move(self, ocean_world_size):
        """Move randomly across the ocean world."""
        self.x = (self.x + random.choice([-1, 1])) % ocean_world_size
        self.y = (self.y + random.choice([-1, 1])) % ocean_world_size

    def try_metabolism(self):
        pass

    def is_alive(self):
        # Check if the life form is alive.
        return self.energy > self.survival_threshold
    
    def try_reproduce(self):
        pass
    
class Autotroph(Lifeform):

    def __init__(self, x, y, energy=50):
        super().__init__(x, y, energy)
        self.survival_threshold = 10

    def move(self, ocean_world_size):
        super().move(ocean_world_size)
    
    def try_metabolism(self, ocean_world: OceanWorld):
        # Consume chemical energy from the environment.
        chemical_energy = ocean_world.get_chemical_concentration(self.x, self.y)
        if chemical_energy > 15:
            self.energy += chemical_energy * 0.1  # Convert chemical energy to biological energy
            ocean_world.add_chemical(self.x, self.y, -chemical_energy * 0.1)  # Reduce chemical concentration
        self.energy -= 1 # Metabolic energy drain

    def is_alive(self):
        return super().is_alive()
    
    def try_reproduce(self):
        reproduce_threshold = 50
        if self.energy < reproduce_threshold:
            return None
        self.energy = self.energy / 2
        return Autotroph(self.x, self.y, self.energy)

class Heterotroph(Lifeform):

    def __init__(self, x, y, energy=30):
        super().__init__(x, y, energy)
        self.survival_threshold = 15

    def move(self, ocean_world_size):
        super().move(ocean_world_size)
    
    # TODO:
    def try_metabolism(self, prey_list, heterotroph_count):
        # Find an autotroph in nearby grid cells
        for prey in prey_list:
            if abs(prey.x - self.x) <= 1 and abs(prey.y - self.y) <= 1 and prey.is_alive():
                # Consume the energy of prey autotroph.
                self.energy += prey.energy / 2 # Heterotroph consumes half of prey's energy 
                prey.energy = 0 # Autotroph dies
                break
        self.energy -= max(1, heterotroph_count / 100) # Metabolic energy drain
        

    def is_alive(self):
        return super().is_alive()

    def try_reproduce(self):
        reproduce_threshold = 60
        if self.energy < reproduce_threshold:
            return None
        self.energy = self.energy / 2
        return Heterotroph(self.x, self.y, self.energy)