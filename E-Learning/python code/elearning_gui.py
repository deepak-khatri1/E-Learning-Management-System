import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pandas as pd
from elearning import ELearningSystem  # Import the backend class

class ELearningGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("E-Learning Management System")
        self.root.geometry("800x600")
        self.system = ELearningSystem("D:/IT/elearning_data.xlsx")  # Initialize the backend

        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title label
        self.title_label = tk.Label(self.main_frame, text="E-Learning Management System", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Buttons frame
        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.pack(pady=10)

        # Buttons
        self.show_students_btn = tk.Button(self.buttons_frame, text="Show Students", command=self.show_students, width=20)
        self.show_students_btn.grid(row=0, column=0, padx=5, pady=5)

        self.show_courses_btn = tk.Button(self.buttons_frame, text="Show Courses", command=self.show_courses, width=20)
        self.show_courses_btn.grid(row=0, column=1, padx=5, pady=5)

        self.show_payments_btn = tk.Button(self.buttons_frame, text="Show Payments", command=self.show_payments, width=20)
        self.show_payments_btn.grid(row=0, column=2, padx=5, pady=5)

        self.search_student_btn = tk.Button(self.buttons_frame, text="Search Student by ID", command=self.search_student, width=20)
        self.search_student_btn.grid(row=1, column=0, padx=5, pady=5)

        self.reload_data_btn = tk.Button(self.buttons_frame, text="Reload Excel Data", command=self.reload_data, width=20)
        self.reload_data_btn.grid(row=1, column=1, padx=5, pady=5)

        self.add_student_btn = tk.Button(self.buttons_frame, text="Add Student", command=self.add_student, width=20)
        self.add_student_btn.grid(row=2, column=0, padx=5, pady=5)

        self.add_course_btn = tk.Button(self.buttons_frame, text="Add Course", command=self.add_course, width=20)
        self.add_course_btn.grid(row=2, column=1, padx=5, pady=5)

        self.add_payment_btn = tk.Button(self.buttons_frame, text="Add Payment", command=self.add_payment, width=20)
        self.add_payment_btn.grid(row=2, column=2, padx=5, pady=5)

        self.exit_btn = tk.Button(self.buttons_frame, text="Exit", command=self.root.quit, width=20, bg="red", fg="white")
        self.exit_btn.grid(row=3, column=1, padx=5, pady=5)

        # Display area
        self.display_text = tk.Text(self.main_frame, height=20, width=80)
        self.display_text.pack(pady=10, fill=tk.BOTH, expand=True)

    def show_students(self):
        self.display_text.delete(1.0, tk.END)
        self.display_text.insert(tk.END, self.system.students.to_string(index=False))

    def show_courses(self):
        self.display_text.delete(1.0, tk.END)
        self.display_text.insert(tk.END, self.system.courses.to_string(index=False))

    def show_payments(self):
        self.display_text.delete(1.0, tk.END)
        self.display_text.insert(tk.END, self.system.payments.to_string(index=False))

    def search_student(self):
        sid = simpledialog.askstring("Search Student", "Enter Student ID:")
        if sid:
            self.display_text.delete(1.0, tk.END)
            if "student_id" not in self.system.students.columns:
                self.display_text.insert(tk.END, "ERROR: 'student_id' column not found.")
                return
            stu = self.system.students[self.system.students["student_id"].astype(str) == sid]
            pay = self.system.payments[self.system.payments["student_id"].astype(str) == sid]
            if stu.empty:
                self.display_text.insert(tk.END, "Student not found.")
            else:
                self.display_text.insert(tk.END, "Student Information:\n" + stu.to_string(index=False) + "\n\nPayment Information:\n" + pay.to_string(index=False))

    def reload_data(self):
        self.system.load_data()
        messagebox.showinfo("Reload", "Data reloaded successfully!")

    def add_student(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Student")
        dialog.geometry("300x200")

        tk.Label(dialog, text="Student ID:").pack()
        sid_entry = tk.Entry(dialog)
        sid_entry.pack()

        tk.Label(dialog, text="Name:").pack()
        name_entry = tk.Entry(dialog)
        name_entry.pack()

        tk.Label(dialog, text="Email:").pack()
        email_entry = tk.Entry(dialog)
        email_entry.pack()

        def submit():
            sid = sid_entry.get().strip()
            name = name_entry.get().strip()
            email = email_entry.get().strip()
            if sid and name and email:
                if sid in self.system.students["student_id"].astype(str).values:
                    messagebox.showerror("Error", "Student ID already exists!")
                else:
                    new_row = pd.DataFrame({"student_id": [sid], "name": [name], "email": [email]})
                    self.system.students = pd.concat([self.system.students, new_row], ignore_index=True)
                    try:
                        self.system.students.to_excel("D:/IT/students.xlsx", sheet_name="Students", index=False)
                        messagebox.showinfo("Success", "Student added successfully!")
                        dialog.destroy()
                    except Exception as e:
                        messagebox.showerror("Error", f"Failed to save: {e}")
                        self.system.students = self.system.students[:-1]
            else:
                messagebox.showerror("Error", "All fields are required!")

        tk.Button(dialog, text="Add", command=submit).pack()

    def add_course(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Course")
        dialog.geometry("300x250")

        tk.Label(dialog, text="Course ID:").pack()
        cid_entry = tk.Entry(dialog)
        cid_entry.pack()

        tk.Label(dialog, text="Course Title:").pack()
        title_entry = tk.Entry(dialog)
        title_entry.pack()

        tk.Label(dialog, text="Teacher Name:").pack()
        teacher_entry = tk.Entry(dialog)
        teacher_entry.pack()

        tk.Label(dialog, text="Course Length / Description:").pack()
        length_entry = tk.Entry(dialog)
        length_entry.pack()

        def submit():
            cid = cid_entry.get().strip()
            title = title_entry.get().strip()
            teacher = teacher_entry.get().strip()
            length = length_entry.get().strip()
            if cid and title and teacher and length:
                if cid in self.system.courses["course_id"].astype(str).values:
                    messagebox.showerror("Error", "Course ID already exists!")
                else:
                    new_row = pd.DataFrame({"course_id": [cid], "course_title": [title], "teacher": [teacher], "course_length": [length]})
                    self.system.courses.index = range(len(self.system.courses))
                    new_row.index = range(len(new_row))
                    self.system.courses = pd.concat([self.system.courses, new_row], ignore_index=True)
                    try:
                        self.system.courses.to_excel("D:/IT/courses_sheet.xlsx", sheet_name="Courses", index=False)
                        messagebox.showinfo("Success", "Course added successfully!")
                        self.system.load_data()
                        dialog.destroy()
                    except PermissionError:
                        messagebox.showerror("Error", "Permission denied. Close the Excel file and try again.")
                        self.system.courses = self.system.courses[:-1]
                    except Exception as e:
                        messagebox.showerror("Error", f"Failed to save: {e}")
                        self.system.courses = self.system.courses[:-1]
            else:
                messagebox.showerror("Error", "All fields are required!")

        tk.Button(dialog, text="Add", command=submit).pack()

    def add_payment(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Payment")
        dialog.geometry("300x250")

        tk.Label(dialog, text="Student ID:").pack()
        sid_entry = tk.Entry(dialog)
        sid_entry.pack()

        tk.Label(dialog, text="Course ID:").pack()
        cid_entry = tk.Entry(dialog)
        cid_entry.pack()

        tk.Label(dialog, text="Amount:").pack()
        amount_entry = tk.Entry(dialog)
        amount_entry.pack()

        tk.Label(dialog, text="Date (YYYY-MM-DD):").pack()
        date_entry = tk.Entry(dialog)
        date_entry.pack()

        def submit():
            sid = sid_entry.get().strip()
            cid = cid_entry.get().strip()
            amount = amount_entry.get().strip()
            date = date_entry.get().strip()
            if sid and cid and amount and date:
                if sid not in self.system.students["student_id"].astype(str).values:
                    messagebox.showerror("Error", "Student ID not found.")
                elif cid not in self.system.courses["course_id"].astype(str).values:
                    messagebox.showerror("Error", "Course ID not found.")
                else:
                    new_row = pd.DataFrame({"student_id": [sid], "course_id": [cid], "amount": [amount], "date": [date]})
                    self.system.payments = pd.concat([self.system.payments, new_row], ignore_index=True)
                    try:
                        self.system.payments.to_excel("D:/IT/payment_records.xlsx", sheet_name="Payments", index=False)
                        messagebox.showinfo("Success", "Payment added successfully!")
                        dialog.destroy()
                    except Exception as e:
                        messagebox.showerror("Error", f"Failed to save: {e}")
                        self.system.payments = self.system.payments[:-1]
            else:
                messagebox.showerror("Error", "All fields are required!")

        tk.Button(dialog, text="Add", command=submit).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ELearningGUI(root)
    root.mainloop()
