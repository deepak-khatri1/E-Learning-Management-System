# 🎓 E-Learning Management System

> A GUI-based desktop application to manage students, courses, and payments using Python.

---

## 📌 Project Information

- 🏫 **University:** FAST University, Karachi  
- 📘 **Course:** IT in Business  
- 📅 **Semester:** 1st Semester  
- 👨‍💻 **Project Type:** Group Project  

### 👥 Group Members
- Deepak Kumar 
- Faiz Ahmad  
- Shuja Ahmad Shamsi  
- M. Ammar  

---

## 🚀 Overview

This project is a **desktop-based E-Learning Management System** developed using **Python Tkinter** and **Pandas**.

It provides a simple interface to:
- Manage student records
- Manage courses
- Track payments

Excel files are used as a lightweight database system.

---

## ✨ Features

### 📊 Data Management
- View Students, Courses, and Payments
- Store and retrieve data from Excel files

### 🔍 Search Functionality
- Search student by ID
- View student details along with payment history

### ➕ Add Records
- Add new students
- Add new courses
- Add payment records

### 🔄 System Operations
- Reload Excel data instantly
- Input validation and error handling

---

## 🛠️ Technologies Used

- **Python**
- **Tkinter (GUI)**
- **Pandas**
- **Excel (.xlsx)**

---

## 📂 Project Structure

```bash
E-Learning-System/
│
├── elearning_gui.py        # Main GUI application
├── elearning.py           # Backend logic
├── students.xlsx          # Student data
├── courses_sheet.xlsx     # Course data
├── payment_records.xlsx   # Payment data
└── README.md              # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Install Dependencies

```bash
pip install pandas openpyxl
```

---

### 2️⃣ Update File Paths ⚠️

Replace this:

```python
"D:/IT/elearning_data.xlsx"
```

With:

```python
"elearning_data.xlsx"
```

---

### 3️⃣ Run the Application

```bash
python elearning_gui.py
```

---

## 🖥️ Application Interface

The application includes:
- Buttons for all operations
- Display panel for data
- Input forms for adding records

---

## ⚠️ Important Notes

- Close Excel files before saving data
- Ensure correct file paths

### Required Columns

#### Students
- `student_id`
- `name`
- `email`

#### Courses
- `course_id`
- `course_title`
- `teacher`
- `course_length`

#### Payments
- `student_id`
- `course_id`
- `amount`
- `date`

---

## 💡 Future Improvements

- 🔐 Login system
- 🌐 Web-based version
- 📊 Dashboard with charts
- 🗄️ Database integration (MySQL)

---

## 🤝 Contribution

This is a university project. Contributions and improvements are welcome.

---

## 📜 License

Free for educational use.

---

## ⭐ Acknowledgment

Special thanks to **FAST University Karachi** for this project opportunity.

---

## 👨‍💻 Developed By

**Deepak & Team**
