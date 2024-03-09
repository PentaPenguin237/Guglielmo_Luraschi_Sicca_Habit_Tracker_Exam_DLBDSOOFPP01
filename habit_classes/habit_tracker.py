import json
import os
from datetime import datetime, timedelta
from habit_classes.habit import Habit

class HabitTracker:
    """A class to track, add, update, and delete habits stored in a JSON file."""

    def __init__(self, json_file_path):
        """Initialize HabitTracker with a path to a JSON file."""
        self.json_file_path = json_file_path
        self.habits = self.load_habits()

    def load_habits(self):
        """Load habits from the specified JSON file."""
        if os.path.isfile(self.json_file_path):
            with open(self.json_file_path, 'r') as f:
                data = json.load(f)
            return {name: Habit(name, info['type'], info['completion_dates']) for name, info in data.items()}
        return {}

    def save_habits(self):
        """Save the current habits to the JSON file."""
        with open(self.json_file_path, 'w') as f:
            data = {name: {'type': habit.habit_type, 'completion_dates': habit.completion_dates}
                    for name, habit in self.habits.items()}
            json.dump(data, f, indent=4)

    def add_habit(self, name, habit_type, completion_dates):
        """Add a new habit to the tracker."""
        if name not in self.habits:
            self.habits[name] = Habit(name, habit_type, completion_dates)
            self.save_habits()

    def update_habit_custom_date(self, name, custom_date):
        """Update a habit's completion with a custom date."""
        try:
            custom_date_obj = datetime.strptime(custom_date, '%Y-%m-%d').date()
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."
        if custom_date_obj > datetime.today().date():
            return "Cannot update habit with a future date."
        if name not in self.habits:
            return f"Habit '{name}' does not exist."
        if custom_date in self.habits[name].completion_dates:
            return f"Habit '{name}' is already marked as completed on {custom_date}."

        self.habits[name].completion_dates.append(custom_date)
        self.save_habits()
        return f"Habit '{name}' marked as completed on {custom_date}."

    def remove_habit(self, name):
        """Remove a habit from the tracker by name."""
        if name not in self.habits:
            return f"Habit '{name}' does not exist."
        del self.habits[name]
        self.save_habits()
        return f"Habit '{name}' correctly deleted."

    def longest_habit_streak(self):
        # Initialize variables to keep track of the habit name and length of longest streak
        longest_name = None
        longest_streak = 0
        # Iterate through all habits to find the longest streak
        for name, habit in self.habits.items():
            # Check the streak of the current habit
            streak = habit.verify_streak()
            # If the current habit's streak is longer than the longest found so far, update the records
            if streak > longest_streak:
                longest_name = name
                longest_streak = streak
        # Return the name of the habit with the longest streak and the length of the streak
        return longest_name, longest_streak

    def current_daily_habits(self):
        # List comprehension iterates through all habits and picks only those with the 'daily' type
        return [name for name, habit in self.habits.items() if habit.habit_type == 'daily']

    def current_weekly_habits(self):
        # List comprehension iterates through all habits and picks only those with the 'daily' type
        return [name for name, habit in self.habits.items() if habit.habit_type == 'weekly']    

    def habits_most_struggled_last_month(self):
        # Get today's date
        today = datetime.today().date()
        # Calculate the first day of last month
        first_day_last_month = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
        # Calculate the last day of last month
        last_day_last_month = today.replace(day=1) - timedelta(days=1)
        # Initialize a dictionary to keep track of each habit's struggle score
        struggle_list = {}
        # Iterate through all the habits
        for name, habit in self.habits.items():
            # Initialize the count of missed days for the current habit
            missed_days = 0
            # Check each completion date to see if it falls in the last month
            for date_str in habit.completion_dates:
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                if first_day_last_month <= date <= last_day_last_month:
                    missed_days += 1
            # Calculate the number of days in the last month
            total_days_last_month = (last_day_last_month - first_day_last_month).days + 1
            # Determine the number of possible occurrences based on habit type
            if habit.habit_type == 'daily':
                possible_occurrences = total_days_last_month
            elif habit.habit_type == 'weekly':
                possible_occurrences = total_days_last_month // 7
            # Calculate the struggle score (potential minus actual completion)
            struggle_score = possible_occurrences - missed_days
            # Add the struggle score for the habit to the dictionary
            struggle_list[name] = struggle_score
        # Sort the struggle_list dictionary by struggle score (lowest to highest) and return the names of top 3 habits
        return sorted(struggle_list, key=struggle_list.get, reverse = True)[:3]