import random
from environment import OceanWorld, HydrothermalVent, Autotroph, Heterotroph

class Simulation:
    def __init__(self, world_size, num_vents, num_autotrophs, num_heterotrophs, vent_production_rate):
        # Initialize the ocean world
        self.ocean_world = OceanWorld(world_size)

        # Create hydrothermal vents
        self.vents = [HydrothermalVent(random.randint(0, world_size - 1), random.randint(0, world_size - 1), vent_production_rate) 
                      for _ in range(num_vents)]

        # Create autotroph bacteria.
        self.autotrophs = [Autotroph(random.randint(0, world_size - 1), random.randint(0, world_size - 1)) 
                           for _ in range(num_autotrophs)]
        
        # Create heterotroph bacteria.
        self.heterotrophs = [Heterotroph(random.randint(0, world_size - 1), random.randint(0, world_size - 1)) 
                           for _ in range(num_heterotrophs)]

    def step(self):
        """Run one time step of the simulation."""
        # Vents release chemicals
        for vent in self.vents:
            vent.release_chemicals(self.ocean_world)

        # Diffuse chemicals in the ocean
        self.ocean_world.diffuse_chemicals()

        # Life forms move and consume chemicals
        for autotroph in self.autotrophs:
            autotroph.move(self.ocean_world.size)
            autotroph.try_metabolism(self.ocean_world)
            new_autotroph = autotroph.try_reproduce()
            if new_autotroph != None:
                self.autotrophs.append(new_autotroph)

        for heterotroph in self.heterotrophs:
            heterotroph.move(self.ocean_world.size)
            heterotroph.try_metabolism(self.autotrophs, len(self.heterotrophs))
            new_heterotroph = heterotroph.try_reproduce()
            if new_heterotroph != None:
                self.heterotrophs.append(new_heterotroph)

        # Remove dead life autotrophs
        self.autotrophs = [lf for lf in self.autotrophs if lf.is_alive()]
        self.heterotrophs = [lf for lf in self.heterotrophs if lf.is_alive()]

    def run(self, steps):
        # Run the simulation for a given number of steps.
        for step in range(steps):
            print(f"Step {step}: Autotrophs remaining: {len(self.autotrophs)} | Heterotrophs remaining: {len(self.heterotrophs)}")
            self.step()
            if not self.autotrophs and not self.heterotrophs:
                print("All life forms have died.")
                break

        # Visualize the final state of the ocean world
        self.ocean_world.retrieve_lifeform_grids(self.autotrophs, self.heterotrophs)
        self.ocean_world.display_grid(len(self.autotrophs), len(self.heterotrophs))

# Example usage
simulation = Simulation(world_size=100, num_vents=30, num_autotrophs=500, num_heterotrophs=10, vent_production_rate=100)
simulation.run(steps=500)
