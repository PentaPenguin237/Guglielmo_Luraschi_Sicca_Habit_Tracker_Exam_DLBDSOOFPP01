from datetime import datetime, timedelta

class Habit:
    """
    Represents a habit with a name, type, and list of completion dates.
    Supports operations to verify the current streak of habit completion.
    """
    
    def __init__(self, name, habit_type, completion_dates):
        """
        Initializes a Habit object with its name, type, and completion dates.

        :param name: The name of the habit.
        :param habit_type: The type of the habit ('daily' or 'weekly').
        :param completion_dates: A list of dates (strings) when the habit was completed.
        """
        self.name = name
        self.habit_type = habit_type
        self.completion_dates = completion_dates

    def verify_streak(self):
        """
        Calculate the current streak of completed habit occurrences based on its type.

        For 'daily' habits, it counts the number of consecutive days up to today.
        For 'weekly' habits, it checks completions week by week without missing any week up to the current week.

        :return: The length of the current streak in days (for daily habits) or weeks (for weekly habits).
        """
        streak_counter = 0
        today = datetime.today().date()
        date_check = today
        if self.habit_type == 'daily':
            day_or_week = "days";
            # Iterate over each day backwards from today, checking if the habit was completed.
            for date_str in reversed(self.completion_dates):
                if str(date_check) == date_str:
                    streak_counter += 1
                    date_check -= timedelta(days=1)
                else:
                    break

        elif self.habit_type == 'weekly':
            day_or_week = "weeks";
            # Sort the completion dates and iterate week by week.
            sorted_dates = sorted([datetime.strptime(d, '%Y-%m-%d').date() for d in self.completion_dates])
            if sorted_dates:
                current_week_start = today - timedelta(days=today.weekday())
                for date in sorted_dates[::-1]:
                    week_start = date - timedelta(days=date.weekday())
                    if current_week_start == week_start:
                        streak_counter += 1
                        current_week_start -= timedelta(weeks=1)
                    elif week_start < current_week_start:
                        break

        return streak_counter, day_or_week
