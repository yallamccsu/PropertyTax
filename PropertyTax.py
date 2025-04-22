import tkinter

class PropertyGUI:
    def __init__(self):
        # Main window setup
        self.main_window = tkinter.Tk()
        self.main_window.title("Property Tax Calculator")  # give it a title for that professional touch

        # Create frames to organize stuff
        self.value_frame = tkinter.Frame(self.main_window)
        self.assess_frame = tkinter.Frame(self.main_window)
        self.tax_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # --- Property Value Input ---
        self.value_label = tkinter.Label(self.value_frame, text='Enter property value ($): ')
        self.value_entry = tkinter.Entry(self.value_frame, width=12)  # give it a little more room

        self.value_label.pack(side='left')
        self.value_entry.pack(side='left')

        # --- Assessment Value Output ---
        self.assess_results_label = tkinter.Label(self.assess_frame, text='Assessment Value: ')
        self.assess_var = tkinter.StringVar()
        self.assess_label = tkinter.Label(self.assess_frame, textvariable=self.assess_var)

        self.assess_results_label.pack(side='left')
        self.assess_label.pack(side='left')

        # --- Tax Output ---
        self.tax_results_label = tkinter.Label(self.tax_frame, text='Property Tax: ')
        self.tax_var = tkinter.StringVar()
        self.tax_label = tkinter.Label(self.tax_frame, textvariable=self.tax_var)

        self.tax_results_label.pack(side='left')
        self.tax_label.pack(side='left')

        # --- Buttons ---
        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left', padx=5)
        self.quit_button.pack(side='left')

        # Pack all the frames
        self.value_frame.pack(pady=5)
        self.assess_frame.pack(pady=5)
        self.tax_frame.pack(pady=5)
        self.bottom_frame.pack(pady=10)

        # Keep the window open
        tkinter.mainloop()

    def calculate(self):
        # Try to grab the input and calculate the stuff
        try:
            property_value = float(self.value_entry.get())

            # Assessment is 60% of the property value
            assessment_value = property_value * 0.60
            self.assess_var.set(f"${assessment_value:,.2f}")

            # Tax is 0.75% of the assessment
            tax_amount = assessment_value * 0.0075
            self.tax_var.set(f"${tax_amount:,.2f}")
        except ValueError:
            self.assess_var.set("Invalid input")
            self.tax_var.set("Try again")

# Run the GUI
if __name__ == '__main__':
    PropertyGUI()
