import psycopg2

# Function to create a connection to the database
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="school",
            user="postgres",
            password="dollar25A",
            host="localhost"
        )
        return conn
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")

# Function to retrieve all students
def get_all_students():
    conn = connect_db()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students;")
        students = cur.fetchall()
        for student in students:
            print(student)
    conn.close()

# Function to add a new student, now including student_id
def add_student(first_name, last_name, email, enrollment_date):
    conn = connect_db()
    with conn.cursor() as cur:
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                    (first_name, last_name, email, enrollment_date))
        conn.commit()
    conn.close()

# Function to update a student's email
def update_student_email(student_id, new_email):
    conn = connect_db()
    with conn.cursor() as cur:
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s;",
                    (new_email, student_id))
        conn.commit()
    conn.close()

# Function to delete a student, requires only student_id
def delete_student(student_id):
    conn = connect_db()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        conn.commit()
    conn.close()

