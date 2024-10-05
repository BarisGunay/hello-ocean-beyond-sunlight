import random
from environment import OceanWorld, Lifeform, HydrothermalVent

class Simulation:
    def __init__(self, world_size, num_vents, num_life_forms, vent_production_rate):
        # Initialize the ocean world
        self.ocean_world = OceanWorld(world_size)

        # Create hydrothermal vents
        self.vents = [HydrothermalVent(random.randint(0, world_size - 1), random.randint(0, world_size - 1), vent_production_rate) 
                      for _ in range(num_vents)]

        # Create life forms
        self.life_forms = [Lifeform(random.randint(0, world_size - 1), random.randint(0, world_size - 1)) 
                           for _ in range(num_life_forms)]

    def step(self):
        """Run one time step of the simulation."""
        # Vents release chemicals
        for vent in self.vents:
            vent.release_chemicals(self.ocean_world)

        # Diffuse chemicals in the ocean
        self.ocean_world.diffuse_chemicals()

        # Life forms move and consume chemicals
        for life_form in self.life_forms:
            life_form.move(self.ocean_world.size)
            life_form.consume_chemicals(self.ocean_world)
            new_life_form = life_form.try_reproduce()
            if new_life_form != None:
                self.life_forms.append(new_life_form)

        # Remove dead life forms
        self.life_forms = [lf for lf in self.life_forms if lf.is_alive()]

    def run(self, steps):
        """Run the simulation for a given number of steps."""
        for step in range(steps):
            print(f"Step {step}: Life forms remaining: {len(self.life_forms)}")
            self.step()
            if not self.life_forms:
                print("All life forms have died.")
                break

        # Visualize the final state of the ocean world
        self.ocean_world.display_grid()

# Example usage
simulation = Simulation(world_size=200, num_vents=25, num_life_forms=100, vent_production_rate=50)
simulation.run(steps=1000)
