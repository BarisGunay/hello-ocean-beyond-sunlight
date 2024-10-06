import tkinter as tk
from tkinter import messagebox
from simulation import Simulation

class SimulationUI:
    def __init__(self, win, entries: list):
        self.win = win
        self.win.geometry("410x410")
        self.win.title("Beyond Sunlight Simulation")
        self.entries = entries

        self.labels = ["World Size", "Hydrothermal Vent Count", "Autotrophs Count", 
                       "Heterotrophs Count", "H2S Production Rate", "Steps"]

        for label_i, label_text in enumerate(self.labels):
            label = tk.Label(self.win, text=label_text + ":")
            label.grid(row=label_i, column=0)

            entry = tk.Entry(self.win)
            entry.grid(row=label_i, column=1)
            self.entries.append(entry)

        # Add a non-writable text box for displaying preferred values
        self.text_output = tk.Text(self.win, height=10, width=40)
        self.text_output.grid(row=len(self.labels), columnspan=2, pady=10)

        # Insert preferred values and make the text box uneditable
        self.text_output.insert(tk.END, "Preferred Values:\n")
        self.text_output.insert(tk.END, "World Size: 100\n")
        self.text_output.insert(tk.END, "Hydrothermal Vent Count: 30\n")
        self.text_output.insert(tk.END, "Autotrophs Count: 500\n")
        self.text_output.insert(tk.END, "Heterotrophs Count: 10\n")
        self.text_output.insert(tk.END, "H2S Production Rate: 75\n")
        self.text_output.insert(tk.END, "Steps: 150\n")
        self.text_output.insert(tk.END, "Values for most balanced ecosystem. The program will run these values when input\ntext boxes left empty.")
        self.text_output.config(state=tk.DISABLED)  # Make the text box read-only

        # Correct command binding for the button
        self.executeButton = tk.Button(self.win, text="Run Simulation", command=self.run_simulation)
        self.executeButton.grid(row=len(self.labels) + 1, columnspan=2)

    def run_simulation(self):
        try:
            # Display 'Simulation is running' before starting the simulation
            self.text_output.config(state=tk.NORMAL)  # Enable editing temporarily
            self.text_output.delete(1.0, tk.END)  # Clear the previous content
            self.text_output.insert(tk.END, "Simulation is running...\n")
            self.text_output.config(state=tk.DISABLED)  # Make it read-only again
            self.win.update_idletasks()  # Ensure the UI updates before running the simulation

            # Retrieve input values from entry widgets
            worldsize = int(self.entries[0].get() or 100)
            num_vents = int(self.entries[1].get() or 30)
            num_autotrophs = int(self.entries[2].get() or 500)
            num_heterotrophs = int(self.entries[3].get() or 10)
            vent_production_rate = int(self.entries[4].get() or 75)
            steps = int(self.entries[5].get() or 150)

            # Initialize and run the simulation
            simulation = Simulation(worldsize, num_vents, num_autotrophs, num_heterotrophs, vent_production_rate)
            simulation.run(steps)

            # After simulation completes, display completion message
            self.text_output.config(state=tk.NORMAL)  # Enable editing temporarily
            self.text_output.delete(1.0, tk.END)  # Clear the previous content
            self.text_output.insert(tk.END, "Simulation Completed!\n")
            self.text_output.config(state=tk.DISABLED)  # Make it read-only again

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create the main window
win = tk.Tk()
entries = []
simulationUI = SimulationUI(win, entries)

# Start the Tkinter event loop
win.mainloop()