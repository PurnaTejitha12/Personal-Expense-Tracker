
# Personal Expense Tracker

## 1. Project Overview

The Personal Expense Tracker is a web-based application developed using Python and Streamlit to help users manage and monitor their daily expenses.

The application allows users to add, view, update, and delete expense records. It also provides interactive charts and visualizations to analyze spending patterns and understand monthly expenses.

SQLite is used for database management, while Pandas and Plotly are used for data processing and visualization.

## 2. Problem Statement

Managing daily expenses manually can be difficult and time-consuming. People often find it challenging to maintain expense records, track their spending habits, and identify unnecessary expenses.

Traditional methods such as notebooks and spreadsheets may not provide convenient searching, filtering, and graphical analysis.

Therefore, there is a need for a simple and interactive application that helps users record expenses, organize financial information, and analyze their spending patterns efficiently.

## 3. Objective

The main objectives of this project are:

- To develop a simple and user-friendly expense management application.
- To maintain daily expense records digitally.
- To implement Add, View, Update, and Delete operations.
- To categorize expenses for better financial management.
- To analyze monthly and category-wise spending patterns.
- To visualize expense data using interactive charts.
- To provide an option to download expense reports in CSV format.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application development |
| SQLite | Database management |
| Pandas | Data processing and analysis |
| Plotly | Interactive data visualization |
| Git | Version control |
| GitHub | Source code management |
| Streamlit Community Cloud | Application deployment |

## 5. Key Features

### Dashboard
- Displays total expenses.
- Shows current month's expenses.
- Displays the total number of transactions.
- Provides a summary of recent transactions.
- Displays category-wise expense distribution.

### Add Expense
- Add new expense records.
- Enter expense amount, category, description, date, and payment method.
- Store expense information in the SQLite database.

### View Expenses
- Display all expense records.
- Search expenses using descriptions.
- Filter expenses based on categories.
- Download expense records in CSV format.

### Update Expense
- Select an existing expense record.
- Modify expense amount, category, description, date, and payment method.
- Save updated information in the database.

### Delete Expense
- Select an existing expense record.
- Confirm before deleting the record.
- Remove unwanted expense records from the database.

### Expense Analytics
- Category-wise expense analysis.
- Monthly spending trend visualization.
- Payment method analysis.
- Interactive pie charts, bar charts, and line charts.

## 6. Implementation

The application is developed using Python and Streamlit, with SQLite as the backend database.

### Application Workflow

1. The application establishes a connection to the SQLite database.
2. If the database or expenses table does not exist, it is created automatically.
3. Users can select different operations from the sidebar.
4. Expense details are collected through Streamlit input forms.
5. SQL queries are used to insert, retrieve, update, and delete expense records.
6. Pandas is used to retrieve and process expense data.
7. Plotly is used to generate interactive charts and visualizations.
8. Users can download expense records as CSV files.

### Database Structure

The application uses an SQLite table named `expenses`.

| Column Name | Description |
|---|---|
| expense_id | Unique expense ID (Primary Key) |
| amount | Expense amount |
| category | Expense category |
| description | Description of the expense |
| expense_date | Date of the expense |
| payment_method | Mode of payment |

### Application Architecture

User
  |
  v
Streamlit User Interface
  |
  v
Python Application Logic
  |
  v
SQLite Database
  |
  v
Pandas Data Processing
  |
  v
Plotly Data Visualization

## 7. Results / Outcomes

The Personal Expense Tracker successfully provides an interactive platform for managing daily expenses.

The application achieves the following outcomes:

- Successfully stores expense records in an SQLite database.
- Performs CRUD operations on expense records.
- Displays total and monthly spending information.
- Provides category-wise expense summaries.
- Visualizes monthly spending trends.
- Generates interactive charts for better understanding of financial data.
- Allows users to export expense records in CSV format.
- Provides a web-based interface accessible through a browser.

The project demonstrates how Python, database management, and data visualization technologies can be integrated to develop a practical web application.

## 8. Key Learnings

Through this project, I gained practical experience in:

- Python programming and application development.
- Building interactive web applications using Streamlit.
- Database connectivity and SQLite operations.
- Implementing CRUD operations using SQL queries.
- Data manipulation and analysis using Pandas.
- Creating interactive visualizations using Plotly.
- Handling user inputs and form validations.
- Exporting data into CSV format.
- Managing project files using Git and GitHub.
- Deploying Python applications using Streamlit Community Cloud.

## 9. GitHub Repository Link

The complete source code of this project is available on GitHub.

Repository Link:

https://github.com/PurnaTejitha12/Personal-Expense-Tracker

## 10. Live Application

The application is deployed using Streamlit Community Cloud.

Live Application Link:

https://personal-expense-tracker-python.streamlit.app/

## 11. Project Structure

Personal-Expense-Tracker/
|
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- expenses.db (created automatically)

## 12. Installation and Execution

Follow the steps below to run the project locally.

### Step 1: Clone the Repository

git clone https://github.com/PurnaTejitha12/Personal-Expense-Tracker

### Step 2: Navigate to the Project Directory

cd Personal-Expense-Tracker

### Step 3: Install Required Dependencies

pip install -r requirements.txt

### Step 4: Run the Application

streamlit run app.py

The application will open in your default web browser.

Local Application URL:

http://localhost:8501

## 13. Future Enhancements

The application can be further improved by implementing the following features:

- User authentication and registration.
- Individual user accounts.
- Monthly budget planning.
- Budget limit notifications.
- Income and savings tracking.
- Cloud database integration.
- Downloadable PDF reports.
- Advanced financial analytics.

## 14. Conclusion

The Personal Expense Tracker is a Python-based web application developed to simplify daily expense management.

It combines Streamlit, SQLite, Pandas, and Plotly to provide an interactive platform for recording expenses, managing transactions, and analyzing spending patterns.

This project provided practical experience in Python programming, database management, CRUD operations, data analysis, visualization, and web application deployment.

---

## Author
Sanisetty Purna Tejitha
