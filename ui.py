import tkinter as tk
from tkinter import messagebox
from simulation import Simulation

class SimulationUI:
    def __init__(self, win, entries: list):
        self.win = win
        self.win.geometry("500x500")
        self.win.title("Beyond The Sunrise Simulation")
        self.entries = entries

        self.labels = ["World Size", "Hydrothermal Vent Count", "Autotrophs Count", 
                       "Heterotrophs Count", "H2S Production Rate", "Steps"]

        for label_i, label_text in enumerate(self.labels):
            label = tk.Label(self.win, text=label_text + ":")
            label.grid(row=label_i, column=0)

            entry = tk.Entry(self.win)
            entry.grid(row=label_i, column=1)
            self.entries.append(entry)

        # Correct command binding for the button
        self.executeButton = tk.Button(self.win, text="Run Simulation", command=self.run_simulation)
        self.executeButton.grid(row=len(self.labels), columnspan=2)

    def run_simulation(self):
        try:
            # Retrieve input values from entry widgets
            worldsize = int(self.entries[0].get() or 0)
            num_vents = int(self.entries[1].get() or 0)
            num_autotrophs = int(self.entries[2].get() or 0)
            num_heterotrophs = int(self.entries[3].get() or 0)
            vent_production_rate = int(self.entries[4].get() or 0)
            steps = int(self.entries[5].get() or 0)

            # Initialize and run the simulation
            simulation = Simulation(worldsize, num_vents, num_autotrophs, num_heterotrophs, vent_production_rate)
            simulation.run(steps)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create the main window
win = tk.Tk()
entries = []
simulationUI = SimulationUI(win, entries)

# Start the Tkinter event loop
win.mainloop()
