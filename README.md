# InventoryManagementSystem

# Coffee Management System

## I. Project Overview
The Coffee Management System is a desktop application designed for managing inventory, sales, and customer interactions in a coffee shop environment. This application allows users to add, update, delete, and view products in the inventory, manage customer purchases, and generate bills. The user interface is built using the Tkinter library, providing a user-friendly experience.

## II. Python Concepts and Libraries Applied
This project utilizes several key Python concepts and libraries:
- **Tkinter**: The primary library for creating the graphical user interface (GUI). It provides various widgets like buttons, labels, entries, and frames to construct the application layout.
- **SQLite3**: Used for database management, allowing for persistent storage of inventory and sales data. The application performs CRUD (Create, Read, Update, Delete) operations on the SQLite database.
- **Regular Expressions (re)**: Employed for validating phone numbers and ensuring that user inputs conform to expected formats.
- **Random**: Used for generating random bill numbers to ensure uniqueness for each transaction.
- **PIL (Pillow)**: Used for image handling, allowing for the inclusion of logos and icons in the application interface.
- **Date and Time Handling**: The application utilizes the `datetime` module to manage and display the current date and time, enhancing the billing and transaction processes.

## III. Sustainable Development Goal (SDG) Integration
This project aligns with **SDG 12: Responsible Consumption and Production**. By providing a comprehensive inventory management system, it encourages efficient resource use and minimizes waste in the coffee shop environment. The system helps track product availability, manage discounts, and reduce overstock, promoting sustainable practices within the business.

## IV. Instructions for Running the Program
To run the Coffee Management System, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/CoffeeManagementSystem.git
   cd CoffeeManagementSystem
