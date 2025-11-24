VITyarthi Academic Planner

Course: Introduction to Problem Solving and Programming  
Project Type: Python Console Application

Overview

VITyarthi Academic Planner is a command-line tool to help students stay on top of their workload. You can create tasks, set priorities, track deadlines, and make sure nothing slips through the cracks.

Features

- Add Tasks: Enter details like title, subject, deadline, and priority.
- View Dashboard: Check out all your tasks in a neat table.
- Status Tracking: Mark tasks as ‘Completed’ once you’re done.
- Data Persistence: Everything saves automatically to vityarthi_data.json.
- Analytics: See simple stats on your progress.

Technologies Used

- Language: Python 3.x
- Libraries: json (data storage), os (file checks), datetime (dates)
- Concepts: Object-Oriented Programming, file handling, exceptions, lists, and dictionaries

How to Install & Run

- Make sure Python 3.x is set up on your computer.
- Download or clone this repository; grab main.py.
- Open your terminal, go to the project folder, and type:

python main.py

- Follow the menu prompts on screen to get started.

Testing

- Try adding a task: Choose Option 1, enter “Math HW,” Subject “Calculus,” Priority “High.” See if it saves.
- Test error handling: When prompted for a Task ID, type “Two” instead of a number. The app should handle it without crashing.
- Test persistence: Add a task, close the app, open it again. Your task should still be there.

Screenshots

