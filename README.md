# Habit Tracker Application

The Habit Tracker Application is an innovative tool designed to assist users in building and maintaining positive habits through a user-friendly interface. Developed with Python and utilizing the Tkinter library for its GUI, this application is both powerful and easy to use. It includes a unit test suite to ensure reliability and functionality.

## Features

- **Ease of Habit Management**: Add, mark as complete, and remove habits with a simple interface.
- **Custom Habit Types**: Track both daily and weekly habits, catering to various goal-setting strategies.
- **Progress Tracking**: Visual feedback on your habit streaks helps maintain motivation and visibility of your achievements.
- **User Modes**: Offers 'Test' and 'User' modes to accommodate both demonstration purposes and personal use.
- **Comprehensive Unit Test Suite**: A robust set of tests to guarantee the application performs as expected under various scenarios.

## Installation

### Prerequisites

- Ensure Python 3.6+ is installed on your system.
- Tkinter is required, which is typically included in standard Python installations.
- The pytest library is needed to run the unit test suite.

### Setup

1. **Clone the Repository**:  
git clone https://github.com/PentaPenguin237/Guglielmo_Luraschi_Sicca_Habit_Tracker_Exam_DLBDSOOFPP01.git


2. **Navigate to the Directory**:  
cd habit-tracker


3. **Install Dependencies**:  
pip install -r requirements.txt


## Usage

### Running the Application

Execute the following command in the root directory to start the application:
python main.py

Choose between 'Test' (`t`) and 'User' (`u`) modes when prompted to proceed.

### Adding a Habit

1. Input the name of your habit.
2. Select the habit type (daily or weekly).
3. Click "Add Habit".

### Completing a Habit

1. Select the habit from your list.
2. Enter the completion date (if not today).
3. Click "Complete Habit".

### Removing a Habit

1. Enter the name of the habit you wish to remove.
2. Click "Remove Habit".

## Running the Unit Tests

To ensure the application's integrity, run the unit test suite with pytest:

pytest

Choose between 'Test' (`t`) and 'User' (`u`) modes when prompted to proceed.

### Adding a Habit

1. Input the name of your habit.
2. Select the habit type (daily or weekly).
3. Click "Add Habit".

### Completing a Habit

1. Input the name of the Habit, if you don't remember clearly the name of you habit, you can display it by clicking either on "Current Daily Habits" or on "Current Weekly Habits" depending on the fact that your habit is either a daily or a weekly habit
2. Enter the completion date using the format YYYY-MM-DD if you wish to add the completion for today or a day in the past or just leave it empty and it will by default add the date of today.
3. Click "Complete Habit".

### Removing a Habit

1. Enter the name of the habit you wish to remove.
2. Click "Remove Habit".

### Longest streak

Clicking this button will show the habit for which you had the longest streak. Please note that such habit will probably be a daily habit because in the evaluation of the streaks a daily habit kept for 28 days and a weekly habit kept for the same amount of time will count 28 and 4 leading to a longer streak for the daily habit.

### Current Daily Habits

Will show all the daily habits

### Current Weekly Habits

Will show all the weekly habits

### Struggled Habits Last Month

Works the opposite as Longest Streak and Will show the habits you struggled the most within the last month.

## Running the Unit Tests

To ensure the application's integrity, run the unit test suite with pytest:

pytest

This command will execute all tests and report their outcomes, highlighting any potential issues.

## Contributing

Contributions are highly appreciated. Follow these steps to contribute:

1. Fork the project repository.
2. Create a new feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for more details.

## Acknowledgments

- Special thanks to the Python and Tkinter communities for their invaluable resources and documentation.
- Thank you to all contributors and users for your support and feedback.

Build better habits, one day at a time, with the Habit Tracker Application.
