# Staff Circle - Staff Management System

Staff Circle is a comprehensive staff management application developed with Python's Tkinter GUI toolkit and MySQL for data storage. This tool provides an easy-to-use interface to manage staff details, allowing administrators to add, update, search, and delete staff records. Designed for small to medium-sized businesses or institutions, the system ensures efficient record-keeping and quick access to staff information.

## Features

1. **Admin Login**:
   - Secured login system for administrators.
   - Error messages for invalid credentials or missing fields.
   - Directs to the main management interface after successful login.

2. **Staff Information Management**:
   - **Add Staff**: Add new staff records with details such as ID, Name, Designation, Gender, Phone Number, Email, and Address.
   - **Update Staff**: Modify existing staff information.
   - **Delete Staff**: Remove staff records from the database.
   - **Clear Fields**: Clear all input fields to add or update new information.

3. **Search and Filter**:
   - Search staff records based on ID, Name, Designation, or Phone Number.
   - Display all staff records or filtered results in the data table.

4. **Database Integration**:
   - Uses MySQL to store and manage staff data securely.
   - Supports CRUD operations for efficient record management.

5. **Responsive Interface**:
   - Built with Tkinter, featuring a well-organized and visually clear GUI.
   - Includes table view with scroll functionality for easy navigation of records.

## Prerequisites

- Python 3.x
- MySQL Database
- Required Python Libraries:
  - `tkinter`
  - `Pillow` (for image handling)
  - `mysql.connector` (for MySQL connectivity)

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone https://github.com/yourusername/staff-circle-management.git
   cd staff-circle-management
   ```

2. **Install Required Packages**:
   ```bash
   pip install pillow mysql-connector-python
   ```

3. **Configure Database**:
   - Set up a MySQL database and table with the following schema:
     ```sql
     CREATE DATABASE mydatabase;
     USE mydatabase;
     CREATE TABLE staff (
         idno VARCHAR(10) PRIMARY KEY,
         name VARCHAR(50),
         designation VARCHAR(30),
         gender ENUM('MALE', 'FEMALE', 'OTHER'),
         phoneno VARCHAR(15),
         email VARCHAR(100),
         address TEXT
     );
     ```
   - Update the `host`, `user`, `passwd`, and `database` parameters in the code with your MySQL credentials.

4. **Run the Application**:
   ```bash
   python staff_circle.py
   ```

## Usage

1. **Login** as Admin using valid credentials to access the staff management functionalities.
2. **Manage Staff Records** by adding, updating, deleting, or searching for staff members.
3. **View All Records** or use the **Search Feature** to filter staff based on specific criteria.
4. **Clear Input Fields** when adding or updating records to avoid duplicate entries.

## Screenshots

![image](https://github.com/user-attachments/assets/f02b354c-eff2-41e8-95b8-33fadae4a4f1)
![image](https://github.com/user-attachments/assets/bfd80d17-86c2-45b2-aa74-ed40c2e94095)
![image](https://github.com/user-attachments/assets/af3e18bf-f7e7-4eb8-b94b-850638e089e7)
![image](https://github.com/user-attachments/assets/72254dee-4adf-4ffe-97a7-016f55e677df)
![image](https://github.com/user-attachments/assets/d62b0646-7714-416e-aad6-911294b00cc1)
![image](https://github.com/user-attachments/assets/89c24a1c-c92e-4310-aa24-43a616e69d11)


## Acknowledgments
thank you for viewing this project staff, and fell free to contribute new features and updates on this project.




