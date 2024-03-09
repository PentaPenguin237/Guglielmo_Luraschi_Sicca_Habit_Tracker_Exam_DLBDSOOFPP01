import pytest
from datetime import datetime, timedelta
from habit_classes.habit_tracker import HabitTracker

@pytest.fixture
def tracker(tmp_path):
    """
    A pytest fixture that creates a HabitTracker instance with a temporary JSON file for testing.

    :param tmp_path: A pytest fixture that provides a temporary directory unique to the test function.
    :return: A HabitTracker instance for testing.
    """
    test_json_path = tmp_path / "test_habits.json"
    test_json_path.write_text("{}")  # Initialize the JSON file with an empty dictionary.
    return HabitTracker(str(test_json_path))

def test_add_and_remove_habit(tracker):
    """
    Test that a habit can be added to and removed from the tracker.
    """
    habit_name = "Exercise"
    tracker.add_habit(habit_name, "daily", [])  # Add a new habit.
    assert habit_name in tracker.habits  # Verify the habit was added.
    tracker.remove_habit(habit_name)  # Remove the habit.
    assert habit_name not in tracker.habits  # Verify the habit was removed.

def test_update_habit_with_valid_and_invalid_dates(tracker):
    """
    Test updating a habit with both valid and invalid completion dates.
    """
    habit_name = "Read"
    valid_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')  # A date in the past.
    invalid_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')  # Any date in the future.

    tracker.add_habit(habit_name, "daily", [])  # Add a new habit.
    tracker.update_habit_custom_date(habit_name, valid_date)  # Update with a valid date.
    assert valid_date in tracker.habits[habit_name].completion_dates  # Verify the valid update.
    
    response = tracker.update_habit_custom_date(habit_name, invalid_date)  # Attempt to update with an invalid date.
    assert "future date" in response  # Verify the response indicates a future date.
    assert invalid_date not in tracker.habits[habit_name].completion_dates  # Ensure the invalid date wasn't added.

def test_add_habit_with_duplicate_name(tracker):
    """
    Test that adding a habit with a name that already exists does not create a duplicate.
    """
    habit_name = "Meditate"
    tracker.add_habit(habit_name, "daily", [])  # Add a habit.
    tracker.add_habit(habit_name, "daily", [])  # Attempt to add another habit with the same name.
    assert len(tracker.habits) == 1  # Ensure no duplicate was added.
