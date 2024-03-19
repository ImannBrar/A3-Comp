Video Demonstration
(https://www.youtube.com/watch?v=wW19h4Kkox0)

Prerequisites
To prepare for running this script, ensure you have:

-Python installed on your system.

-PostgreSQL installed and operational on your local machine or within your network.

Setup Instructions:
-Clone the Repository
-Clone the repository to your local machine using the command: git clone https://github.com/MoesaMalik/COMP3005_Assignment3.1.git
-If Git is not installed, you can directly download the source code from the repository.

Import Database Schema
-Ensure your PostgreSQL database is ready. Import the database schema with the SQL scripts available. These scripts are located in the database directory of the repository. Follow these steps to import:
-Open your PostgreSQL database management tool (e.g., pgAdmin).
-Create a new database.
-Open the SQL script file (e.g., schema.sql) in a text editor.
-Execute the SQL commands in the script to establish the required tables and schema in your PostgreSQL database.


-- Create the students table
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

-- Insert initial data
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

Configure Database Connection
Modify the Python script to include your PostgreSQL server's details:
URL: Update with your server's connection string, formatted as postgresql://<username>:<password>@<hostname>:<port>/<database_name>.
USERNAME: Your PostgreSQL username.
PASSWORD: Your PostgreSQL password.
Completing these steps readies your environment for using the student database management script.

Functionality
get_all_students(): Fetches and displays all student records.
add_student(first_name, last_name, email, enrollment_date): Inserts a new student record into the database.
update_student_email(student_id, new_email): Modifies the email of a specified student.
delete_student(student_id): Removes a student's record from the database by their ID.

