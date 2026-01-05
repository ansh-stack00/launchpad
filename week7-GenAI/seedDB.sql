-- Students
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    enrollment_year INTEGER
);

-- Instructors
CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT
);

-- Courses
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    instructor_id INTEGER,
    credits INTEGER,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

-- Enrollments
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    grade TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Attendance (per class session)
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY,
    enrollment_id INTEGER,
    session_date TEXT,
    status TEXT CHECK(status IN ('Present', 'Absent')),
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);

-- Payments
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    amount REAL,
    payment_date TEXT,
    status TEXT CHECK(status IN ('Paid', 'Pending')),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Instructors
INSERT INTO instructors VALUES
(1, 'Dr. Smith', 'Computer Science'),
(2, 'Dr. Johnson', 'Mathematics'),
(3, 'Dr. Lee', 'Physics');

-- Courses
INSERT INTO courses VALUES
(1, 'Databases', 1, 4),
(2, 'Algorithms', 1, 4),
(3, 'Linear Algebra', 2, 3),
(4, 'Quantum Mechanics', 3, 4);

-- Students
INSERT INTO students VALUES
(1, 'Alice', 'alice@mail.com', 2023),
(2, 'Bob', 'bob@mail.com', 2022),
(3, 'Charlie', 'charlie@mail.com', 2023),
(4, 'Diana', 'diana@mail.com', 2021),
(5, 'Eve', 'eve@mail.com', 2022);

-- Enrollments
INSERT INTO enrollments VALUES
(1, 1, 1, '2023-01-10', 'A'),
(2, 1, 2, '2023-01-12', 'A-'),
(3, 2, 1, '2022-01-15', 'B'),
(4, 2, 3, '2022-01-20', 'B+'),
(5, 3, 1, '2023-02-01', 'A'),
(6, 3, 4, '2023-02-05', 'B'),
(7, 4, 3, '2021-01-10', 'A-'),
(8, 5, 2, '2022-02-12', 'B+');

-- Attendance
INSERT INTO attendance VALUES
(1, 1, '2023-02-01', 'Present'),
(2, 1, '2023-02-08', 'Absent'),
(3, 2, '2023-02-01', 'Present'),
(4, 3, '2022-02-01', 'Present'),
(5, 4, '2022-02-03', 'Absent'),
(6, 5, '2023-02-10', 'Present'),
(7, 6, '2023-02-12', 'Absent'),
(8, 7, '2021-02-01', 'Present'),
(9, 8, '2022-02-15', 'Present');

-- Payments
INSERT INTO payments VALUES
(1, 1, 1200, '2023-01-05', 'Paid'),
(2, 2, 1000, '2022-01-05', 'Paid'),
(3, 3, 1200, '2023-01-07', 'Pending'),
(4, 4, 900, '2021-01-10', 'Paid'),
(5, 5, 1000, '2022-01-15', 'Paid');
