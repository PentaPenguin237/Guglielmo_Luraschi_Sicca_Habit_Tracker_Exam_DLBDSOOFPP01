import json
import os
from datetime import datetime, timedelta
import tkinter as tk
from habit_gui.habit_tracker_app import HabitTrackerApp
from habit_classes.habit_tracker import HabitTracker

def chosen_file():
    """Prompt the user to select a mode and return the appropriate JSON file path based on their choice of either run the application in test mode or use it as intended in user mode."""
    string_mode = "n"
    while string_mode not in ("t", "u"):
        string_mode = input("Please press 't' for Test mode or 'u' for standard User mode: ")        
        if string_mode == "t":
            json_file_path = 'data/sample_habits.json'
            habit_tracker = HabitTracker(json_file_path)
            habit_tracker.fill_missing_dates()  
            habit_tracker.save_habits()        
        elif string_mode == "u":
            json_file_path = 'data/user_habits.json'
            if not os.path.exists(json_file_path):
                os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
                with open(json_file_path, 'a') as file:
                    json.dump({}, file)
                print(f"File '{json_file_path}' has been created.")
            else:
                print(f"File '{json_file_path}' already exists.")
        else:
            print("Invalid mode selected. Please choose 't' for Test mode or 'u' for User mode.")          
    
    return json_file_path

def main():
    """Initialize the application window and run the habit tracker app."""
    json_file_path = chosen_file()
    root = tk.Tk()
    root.title("Habit Tracker")
    root.attributes('-topmost', True)
    app = HabitTrackerApp(root, json_file_path)
    root.mainloop()

if __name__ == '__main__':
    main()
