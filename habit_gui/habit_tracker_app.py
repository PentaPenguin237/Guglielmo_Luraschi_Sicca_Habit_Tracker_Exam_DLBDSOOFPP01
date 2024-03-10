import json
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import scrolledtext
from habit_classes.habit_tracker import HabitTracker

class HabitTrackerApp():
    """
    A GUI class for the Habit Tracker application using Tkinter.
    This class defines the user interface and interactions for managing habits.
    """

    def __init__(self, master, json_file_path):
        """
        Initialize the GUI application with the master window and a path to the habit data JSON file.

        :param master: The Tkinter root window.
        :param json_file_path: Path to the JSON file where habit data is stored.
        """
        self.master = master
        self.tracker = HabitTracker(json_file_path)
        self.json_file_path = json_file_path
        self.create_widgets()
        self.schedule_sorting()

    def sort_completion_dates(self):
        """
        Sort the completion dates of each habit in the JSON file.
        """
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)

        for habit, details in data.items():
            sorted_dates = sorted(details['completion_dates'], key=lambda x: datetime.strptime(x, '%Y-%m-%d'))
            details['completion_dates'] = sorted_dates

        with open(self.json_file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def schedule_sorting(self):
        """
        Schedule periodic sorting of completion dates.
        """
        self.sort_completion_dates()
        self.master.after(2000, self.schedule_sorting)

    def create_widgets(self):
        """
        Create and place the GUI widgets like labels, entries, buttons, etc., on the master window.
        """

        # Widgets for adding a habit
        self.add_name_label = tk.Label(self.master, text="Add Habit Name:")
        self.add_name_label.grid(row=0, column=0, pady=(10, 0))  # Padding above the label
        self.add_name_entry = tk.Entry(self.master)
        self.add_name_entry.grid(row=0, column=1, pady=(10, 5))  # Consistent padding for alignment
        
        # Widgets for adding a habit
        self.add_name_label = tk.Label(self.master, text="Add Habit Name:")
        self.add_name_label.grid(row=0, column=0, pady=(10, 0))
        self.add_name_entry = tk.Entry(self.master)
        self.add_name_entry.grid(row=0, column=1, pady=(10, 5))

        # Widgets for selecting the type of habit (daily or weekly)
        self.add_type_label = tk.Label(self.master, text="Add Habit Type:")
        self.add_type_label.grid(row=1, column=0, pady=(5, 0))
        self.habit_type_var = tk.StringVar(value='daily')
        self.add_type_daily_radio = tk.Radiobutton(self.master, text="Daily", variable=self.habit_type_var, value='daily')
        self.add_type_daily_radio.grid(row=1, column=1, sticky='w', pady=(5, 0))
        self.add_type_weekly_radio = tk.Radiobutton(self.master, text="Weekly", variable=self.habit_type_var, value='weekly')
        self.add_type_weekly_radio.grid(row=1, column=2, pady=(5, 5))

        # Widgets for adding a habit button
        self.add_habit_button = tk.Button(self.master, text="Add Habit", command=self.add_habit)
        self.add_habit_button.grid(row=2, column=0, columnspan=2, pady=(5, 10))

        # Widgets for updating a habit as completed with custom date
        self.update_name_label = tk.Label(self.master, text="Complete Habit Name:")
        self.update_name_label.grid(row=3, column=0, pady=(10, 0))
        self.update_name_entry = tk.Entry(self.master)
        self.update_name_entry.grid(row=3, column=1, pady=(10, 5))
        
        self.update_date_label = tk.Label(self.master, text="Date (YYYY-MM-DD):")
        self.update_date_label.grid(row=4, column=0, pady=(10, 0))
        self.update_date_entry = tk.Entry(self.master)
        self.update_date_entry.grid(row=4, column=1, pady=(10, 5))

        self.update_habit_button = tk.Button(self.master, text="Complete Habit", command=self.update_habit)
        self.update_habit_button.grid(row=5, column=0, columnspan=2, pady=(5, 10))

        # Widgets for removing a habit
        self.remove_name_label = tk.Label(self.master, text="Remove Habit by Name:")
        self.remove_name_label.grid(row=6, column=0, pady=(10, 0))
        self.remove_name_entry = tk.Entry(self.master)
        self.remove_name_entry.grid(row=6, column=1, pady=(10, 5))
        self.remove_habit_button = tk.Button(self.master, text="Remove Habit", command=self.remove_habit)
        self.remove_habit_button.grid(row=7, column=0, columnspan=2, pady=(5, 10))

        # Widgets for displaying the streak of a habit
        self.display_name_label = tk.Label(self.master, text="Display Habit Streak:")
        self.display_name_label.grid(row=8, column=0, pady=(10, 0))
        self.display_name_entry = tk.Entry(self.master)
        self.display_name_entry.grid(row=8, column=1, pady=(10, 5))
        self.display_habit_button = tk.Button(self.master, text="Display Streak", command=self.display_streak)
        self.display_habit_button.grid(row=9, column=0, columnspan=2, pady=(5, 10))

        # Text box for output messages with scroll feature
        self.output_text = scrolledtext.ScrolledText(self.master, height=10, width=50)
        self.output_text.grid(row=10, column=0, columnspan=3, padx=10, pady=(10, 20))  

        # Widgets for visualizing the longest streaks, current daily habits, and struggled habits
        self.longest_streak_button = tk.Button(self.master, text="Longest Streak", command=self.display_longest_streak)
        self.longest_streak_button.grid(row=11, column=0, columnspan=1, pady=(10, 0))  # Padding above the button

        self.current_daily_habits_button = tk.Button(self.master, text="Current Daily Habits", command=self.display_current_daily_habits)
        self.current_daily_habits_button.grid(row=11, column=1, columnspan=3, pady=(10, 0))  # Same padding for alignment

        self.current_weekly_habits_button = tk.Button(self.master, text="Current Weekly Habits", command=self.display_current_weekly_habits)
        self.current_weekly_habits_button.grid(row=12, column=0, columnspan=1, pady=(10, 10))  # Padding above and below

        self.struggled_habits_button = tk.Button(self.master, text="Struggled Habits Last Month", command=self.display_struggled_habits)
        self.struggled_habits_button.grid(row=12, column=1, columnspan=3, pady=(10, 10))  # Same padding for alignment


    def add_habit(self):
        """
        Add a habit to the tracker when the "Add Habit" button is pressed.
        """
        name = self.add_name_entry.get()
        habit_type = self.habit_type_var.get()
        self.tracker.add_habit(name, habit_type, [])
        self.output_text.insert(tk.END, f"Added habit: {name} ({habit_type})\n")
        self.add_name_entry.delete(0, tk.END)

    def update_habit(self):
        """
        Update a habit's completion status with a custom date or today's date if no date is provided.
        """
        name = self.update_name_entry.get()
        custom_date = self.update_date_entry.get()
        
        if not custom_date:  # If no date is provided, use today's date
            custom_date = datetime.today().strftime('%Y-%m-%d')
            message = f"No date entered. Using today's date: {custom_date}. "
            message += self.tracker.update_habit_custom_date(name, custom_date)
        else:
            message = self.tracker.update_habit_custom_date(name, custom_date)

        self.output_text.insert(tk.END, f"{message}\n")
        self.update_name_entry.delete(0, tk.END)
        self.update_date_entry.delete(0, tk.END)

    def remove_habit(self):
        """
        Remove a habit from the tracker.
        """
        name = self.remove_name_entry.get()
        message = self.tracker.remove_habit(name)
        self.output_text.insert(tk.END, f"{message}\n")
        self.remove_name_entry.delete(0, tk.END)
    def display_streak(self):
        """
        Display habit streak when the "Display Streak" button is pressed
        """        
        name = self.display_name_entry.get()
        if name in self.tracker.habits:
            streak = self.tracker.habits[name].verify_streak()
            day_or_week = self.tracker.habits[name].day_or_week()
            self.output_text.insert(tk.END, f"{name} streak: {streak} - {day_or_week}\n")
        else:
            self.output_text.insert(tk.END, f"Habit not found: {name}\n")
        self.display_name_entry.delete(0, tk.END)  # Clear the entry field after displaying
    def display_longest_streak(self):
        """
        Returns the name of the habit for which we had the longest streak
        """           
        name, streak = self.tracker.longest_habit_streak()
        day_or_week = self.tracker.habits[name].day_or_week()
        if name:
            self.output_text.insert(tk.END, f"Longest Streak: {name} with {streak} {day_or_week}.\n")
        else:
            self.output_text.insert(tk.END, "No streaks to display.\n")
 
    def display_current_daily_habits(self):
        """
        Returns the name of all the daily habits
        """             
        daily_habits = self.tracker.current_daily_habits()  # Make sure this calls the correct method
        if len(daily_habits) == 0:
            self.output_text.insert(tk.END, "You currently have no daily habits.\n")
        else:
            self.output_text.insert(tk.END, f"Current Daily Habits: {', '.join(daily_habits)}\n")
            
    def display_current_weekly_habits(self):
        """
        Returns the name of all the weekly habits
        """              
        weekly_habits = self.tracker.current_weekly_habits()
        if len(weekly_habits) == 0:
            self.output_text.insert(tk.END, "You currently have no weekly habits.\n")
        else:
            self.output_text.insert(tk.END, f"Current Weekly Habits: {', '.join(weekly_habits)}\n")
  
    def display_struggled_habits(self):
        """
        Returns the name of habit that we skipped for most days in case of daily habits or weeks in case of weekly habits
        """              
        struggled_habits = self.tracker.habits_most_struggled_last_month()
        if len(struggled_habits) < 3:
            self.output_text.insert(tk.END, "This function will be available once you will have created at least 3 habits.\n")
        elif len(struggled_habits) >= 3:
            self.output_text.insert(tk.END, f"3 Habits struggled most last month: {', '.join(struggled_habits)}\n")
        else:
            self.output_text.insert(tk.END, "The application has encountered an unexpected problem.\n")
            