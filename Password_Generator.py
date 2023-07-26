import random
import string
import pyperclip
import zxcvbn

from CTkMessagebox import CTkMessagebox
import customtkinter

# Function to generate a random password based on selected options.
def generate_password():
    length = int(Lenght_slider.get())
    options = []

    if not any([lowercase_var.get(), uppercase_var.get(), numbers_var.get(), special_var.get()]):
        CTkMessagebox(title="Password Generation Error", message="Please select at least one option.", icon="cancel")
        return

    if lowercase_var.get():
        options.extend(string.ascii_lowercase)
    if uppercase_var.get():
        options.extend(string.ascii_uppercase)
    if numbers_var.get():
        options.extend(string.digits)
    if special_var.get():
        options.extend(string.punctuation)

    password = "".join(random.choice(options) for _ in range(length))

    Password_Display.configure(state="normal")
    Password_Display.delete(0.0, "end")
    Password_Display.insert("end", password)
    Password_Display.configure(state="disabled")
# Function to copy the generated password to the clipboard.
def copy_to_clipboard():
    password = Password_Display.get(0.0, "end").strip()
    if password:
        pyperclip.copy(password)
        CTkMessagebox(title="Copy Password", message="Password copied to clipboard.",icon="check", option_1="Ok")
    else:
        msg = CTkMessagebox(title="Copy Password", message="There is no password to copy.",icon="warning", option_1="Ok")
#Function to reset all settings (checkboxes, slider, and text displays).
def clear_settings():
    # Set all checkboxes to unchecked
    lowercase_var.set(0)
    uppercase_var.set(0)
    numbers_var.set(0)
    special_var.set(0)

    # Set the slider value to 1

    Lenght_slider.set(1)

    # Set the password display to empty and disabl

    Password_Display.configure(state="normal")
    Password_Display.delete(0.0, "end")
    Password_Display.configure(state="disabled")

    # Set the character display to "1" and disabled

    Character_Display.configure(state="normal")
    Character_Display.delete(0.0, "end")
    Character_Display.insert("end", "1")
    Character_Display.configure(state="disabled")
#Function to update the character display based on the selected password length.
def update_character_display(_event):
    length = int(Lenght_slider.get())
    Character_Display.configure(state="normal")
    Character_Display.delete(0.0, "end")
    Character_Display.insert("end",length)
    Character_Display.configure(state="disabled")
# Function to calculate password strength using zxcvbn


#Window Settings
app = customtkinter.CTk()
app.geometry("500x500")
app.title("Random Password Generator")
app.resizable(False, False)
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("C:\\Python\\Passwordgeneratornewgui\\theme.json")


Character_Display = customtkinter.CTkTextbox(app, height=1,width=50, state="disabled", wrap="none")
Character_Display.grid(row=1, column=0, padx=20, pady=(20,0), sticky="w")

#Slider

Lenght_slider = customtkinter.CTkSlider(app, from_=1, to=32, number_of_steps=32)
Lenght_slider.grid(row=1, column=0, padx=90, pady=(20,0))

Lenght_slider.bind("<Motion>", update_character_display)
Lenght_slider.bind("<ButtonRelease-1>", update_character_display)



#Checkbox
lowercase_var = customtkinter.IntVar()
lowercase_checkbox = customtkinter.CTkCheckBox(app, text="Lowercase", variable=lowercase_var)
lowercase_checkbox.grid(row=2, column=0, padx=0, pady=(0,0))

uppercase_var = customtkinter.IntVar()
Uppercase_checkbox = customtkinter.CTkCheckBox(app, text="Uppercase", variable=uppercase_var)
Uppercase_checkbox.grid(row=2, column=0, padx=0, pady=(0,0))

numbers_var = customtkinter.IntVar()
Number_checkbox = customtkinter.CTkCheckBox(app, text="Number", variable=numbers_var)
Number_checkbox.grid(row=2, column=0, padx=0, pady=(0,0))

special_var = customtkinter.IntVar()
Special_checkbox = customtkinter.CTkCheckBox(app, text="Special", variable=special_var)
Special_checkbox.grid(row=2, column=0, padx=0, pady=(0,0))


Generate_Button = customtkinter.CTkButton(app, text="Generate", command=generate_password)
Generate_Button.grid()

#TextBox
Password_Display = customtkinter.CTkTextbox(app, height=10, width=300, state="disabled")
Password_Display.grid()


#Button
Copy_Button = customtkinter.CTkButton(app, text="Copy", command=copy_to_clipboard)
Copy_Button.grid()

#Reset
Clear_Button = customtkinter.CTkButton(app, text="Clear", command=clear_settings)
Clear_Button.grid()



app.mainloop()