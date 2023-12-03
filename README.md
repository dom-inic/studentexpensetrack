# StudentExpenseTracker

## Introduction
- This Expense Management Application is a web-based platform designed to help users manage their expenses efficiently. Built with Django and Django REST Framework, it offers a user-friend interface for tracking and organizing expenses.

## Features
* User Account Management: Users can create an account, log in, and log out, ensuring that each user's data is private and secure.
* Expense Management: Users can easily add, update, and delete expenses. The application calculates and displays the total expense amount for quick reference.
* Search Functionality: Users can search for expenses by card, category, notes, date, and amount.

## Installation
1. Install the required dependencies: ```pip3 install -r requirements.txt```
2. Run the server: ```python3 manage.py runserver```


---

## API Features
- User-Specific Data Management: Every user can manage their own expense records, with each user's data kept private and secure.
- Create and Manage Expenses: Users can add new expenses, view their past expense records, update details, or delete records as needed.
- Search and Filter Capabilities: Users can easily find expenses based on various criteria such as card type, category, notes, date, and amount.
- Secure Access: All endpoints require user authentication, ensuring that data is protected and only accessible by the respective user.
- You can use ```curl``` to interact with the API or view it on your web browser because Django REST Framework provides a browsable API, which is a user-friendly web interface that allows users to interact with API directly.
