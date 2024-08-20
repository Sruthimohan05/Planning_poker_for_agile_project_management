from tkinter import *
from tkinter import simpledialog, messagebox
import os

def save_to_file(player_data):
    with open('player_selections.txt', 'w') as file:
        for player, card in player_data.items():
            file.write(f"{player}: {card}\n")

def ask_for_teammates():
    num_teammates = simpledialog.askinteger("Input", "Enter the number of teammates:", minvalue=1, maxvalue=100)
    if num_teammates:
        open_player_selection_window(num_teammates)

def open_player_selection_window(num_teammates):
    # Hide the main window
    window.withdraw()
    
    # Create a new window for player input
    input_window = Toplevel(window)
    input_window.title("Player Card Selection")
    
    player_data = {}
    
    def collect_data():
        player_name = player_name_entry.get()
        card_choice = card_choice_var.get()
        if player_name and card_choice:
            player_data[player_name] = card_choice
            player_name_entry.delete(0, END)
            card_choice_var.set(0)
            if len(player_data) == num_teammates:
                save_to_file(player_data)
                messagebox.showinfo("Info", "Data saved to player_selections.txt")
                input_window.destroy()
                window.deiconify()  # Show the main window again
        else:
            messagebox.showwarning("Warning", "Please enter both name and card choice")
    
    # Player name entry
    Label(input_window, text="Player Name:").grid(row=0, column=0)
    player_name_entry = Entry(input_window)
    player_name_entry.grid(row=0, column=1)
    
    # Card choice options
    Label(input_window, text="Select Card:").grid(row=1, column=0)
    card_choice_var = IntVar()
    for value in [0, 1, 2, 3, 5, 8, 13, 20, 40, 100]:
        Radiobutton(input_window, text=value, variable=card_choice_var, value=value).grid(row=1, column=value//10 + 1)
    
    # Submit button
    Button(input_window, text="Submit", command=collect_data).grid(row=2, columnspan=3)

window = Tk()
window.title("Planning Poker")

# Set up canvas with an image
canvas = Canvas(window, width=200, height=200)
bg_image = PhotoImage(file='meeting_resized.png')
canvas.create_image(100, 100, image=bg_image)
canvas.grid(row=1, column=1)

# Heading label
heading_label = Label(window, text="Planning Poker")
heading_label.grid(row=0, column=1)

# Start button
deal_button = Button(window, text='Start', command=ask_for_teammates)
deal_button.grid(row=2, column=1)

window.mainloop()
