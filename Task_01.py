import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("300x250")
        self.addUI()

    def addUI(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12))

        inputFrame = ttk.Frame(self.root, padding="10")
        inputFrame.grid(column=0, row=0, sticky=(tk.W, tk.E))
        tempLabel = ttk.Label(inputFrame, text="Temperature:")
        tempLabel.grid(column=0, row=0, sticky=tk.W)
        unitLabel = ttk.Label(inputFrame, text="Original Unit:")
        unitLabel.grid(column=0, row=1, sticky=tk.W)

        self.tempInput = ttk.Entry(inputFrame, width=10)
        self.tempInput.grid(column=1, row=0, sticky=tk.W)

        self.var = tk.StringVar()
        combo = ttk.Combobox(inputFrame, textvariable=self.var, state='readonly')
        combo['values'] = ('Celsius', 'Fahrenheit', 'Kelvin')
        combo.grid(column=1, row=1, sticky=tk.W)
        combo.current(0)

        convertButton = ttk.Button(self.root, text="Convert", command=self.convert_temperature)
        convertButton.grid(column=0, row=1, padx=10, pady=10)

        resultFrame = ttk.Frame(self.root, padding="10")
        resultFrame.grid(column=0, row=2, sticky=(tk.W, tk.E))
        resultLabel = ttk.Label(resultFrame, text="Converted Temperatures:", font=("Arial", 12, "bold"))
        resultLabel.grid(column=0, row=0, sticky=tk.W)

        self.resultVar = tk.StringVar()
        finalResultDisplay = ttk.Label(resultFrame, textvariable=self.resultVar, font=("Arial", 12))
        finalResultDisplay.grid(column=0, row=1, sticky=tk.W)

        for child in inputFrame.winfo_children():
            child.grid_configure(padx=5, pady=5)
        for child in resultFrame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def convert_temperature(self):
        global result
        try:
            value = float(self.tempInput.get())
            original_unit = self.var.get()
            if original_unit == 'Celsius':
                f_temp = (value * 9 / 5) + 32
                k_temp = value + 273.15
                result = f"Fahrenheit: {f_temp:.2f}°F\nKelvin: {k_temp:.2f}K"
            elif original_unit == 'Fahrenheit':
                c_temp = (value - 32) * 5 / 9
                k_temp = (value - 32) * 5 / 9 + 273.15
                result = f"Celsius: {c_temp:.2f}°C\nKelvin: {k_temp:.2f}K"
            elif original_unit == 'Kelvin':
                c_temp = value - 273.15
                f_temp = (value - 273.15) * 9 / 5 + 32
                result = f"Celsius: {c_temp:.2f}°C\nFahrenheit: {f_temp:.2f}°F"
            self.resultVar.set(result)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for the temperature.")

if __name__ == "__main__":
    root = tk.Tk()
    y = TemperatureConverter(root)
    root.mainloop()
