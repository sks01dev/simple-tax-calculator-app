import customtkinter as ctk

class TaxCalculator:
    def __init__(self):
        # Initialize the main window
        self.window = ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry('350x250')
        self.window.resizable(False, False)
        self.padding = {'padx': 20, 'pady': 10}

        # Set default theme to Dark mode
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Income label and entry
        self.income_label = ctk.CTkLabel(self.window, text='Income:')
        self.income_label.grid(row=0, column=0, **self.padding)

        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Tax Percentage label and entry
        self.tax_label = ctk.CTkLabel(self.window, text='Tax Percent:')
        self.tax_label.grid(row=1, column=0, **self.padding)

        self.tax_entry = ctk.CTkEntry(self.window)
        self.tax_entry.grid(row=1, column=1, **self.padding)

        # Tax Result label and read-only entry
        self.result_label = ctk.CTkLabel(self.window, text='Tax Amount:')
        self.result_label.grid(row=2, column=0, **self.padding)

        self.result_entry = ctk.CTkEntry(self.window, state="readonly")  # Read-only result field
        self.result_entry.grid(row=2, column=1, **self.padding)

        # Calculate button
        self.calculate_button = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_tax)
        self.calculate_button.grid(row=3, column=1, **self.padding)

        # Theme Toggle button
        self.theme_button = ctk.CTkButton(self.window, text='Toggle Theme', command=self.toggle_theme)
        self.theme_button.grid(row=4, column=1, **self.padding)

        # Variable to track current theme
        self.current_theme = "Dark"

    def update_result(self, text: str):
        # Make the entry editable temporarily to update the result, then set it back to readonly
        self.result_entry.configure(state='normal')
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)
        self.result_entry.configure(state='readonly')

    def calculate_tax(self):
        try:
            income = float(self.income_entry.get())
            tax_rate = float(self.tax_entry.get())
            tax_amount = income * (tax_rate / 100)
            self.update_result(f'${tax_amount:,.2f}')
        except ValueError:
            self.update_result('Invalid Input')

    def toggle_theme(self):
        # Toggle between Light and Dark modes
        if self.current_theme == "Dark":
            ctk.set_appearance_mode("Light")
            self.current_theme = "Light"
        else:
            ctk.set_appearance_mode("Dark")
            self.current_theme = "Dark"

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()
