import re
from tkinter import *
from tkinter import ttk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

        # Define professional colors
        bg_color = "#F0F0F0"  # Light gray
        text_color = "#333333"  # Dark gray
        button_color = "#4CAF50"  # Green
        button_text_color = "white"

        # Main frame
        main_frame = Frame(self.root, bd=2, bg=bg_color)
        main_frame.pack(fill=BOTH, expand=True)

        # Left frame for student details and photo options
        left_frame = LabelFrame(main_frame, bd=2, bg=bg_color, relief=RIDGE, text="STUDENT DETAILS", font=("Arial", 12, "bold"))
        left_frame.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=True)

        # Labels and entry widgets for student details
        student_info_labels = [
            "Student Name:", "Class Division:", "Gender:",
            "Roll No:", "Email:", "Phone No:",
            "Address:", "Teacher Name:", "Date of Birth:"
        ]
        self.student_entries = {}
        for i, label_text in enumerate(student_info_labels):
            label = Label(left_frame, text=label_text, font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
            label.grid(row=i, column=0, padx=10, pady=5, sticky=W)

            entry = ttk.Entry(left_frame, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=W)
            self.student_entries[label_text] = entry

            if "Gender" in label_text:
                combo = ttk.Combobox(left_frame, font=("Arial", 12), state="readonly", width=10)
                combo["values"] = ("Male", "Female", "Other")
                combo.current(0)
                combo.grid(row=i, column=1, padx=10, pady=5, sticky=W)

            if "Date of Birth" in label_text:
                vcmd = (root.register(self.validate_date), '%P')
                dob_entry = ttk.Entry(left_frame, font=("Arial", 12), validate="key", validatecommand=vcmd)
                dob_entry.grid(row=i, column=1, padx=10, pady=5, sticky=W)
                self.student_entries[label_text] = dob_entry

        # Radio buttons for taking photo sample or not
        self.take_photo_var = BooleanVar()
        self.take_photo_var.set(True)  # Default to take photo
        take_photo_radio = Radiobutton(left_frame, text="Take Photo Sample", variable=self.take_photo_var, value=True, font=("Arial", 12), bg=bg_color, fg=text_color)
        take_photo_radio.grid(row=len(student_info_labels), column=0, columnspan=2, padx=10, pady=5, sticky=W)

        no_photo_radio = Radiobutton(left_frame, text="No Photo Sample", variable=self.take_photo_var, value=False, font=("Arial", 12), bg=bg_color, fg=text_color)
        no_photo_radio.grid(row=len(student_info_labels) + 1, column=0, columnspan=2, padx=10, pady=5, sticky=W)

        # Right frame for current course information and search system
        right_frame = LabelFrame(main_frame, bd=2, bg=bg_color, relief=RIDGE, text="CURRENT COURSE INFORMATION", font=("Arial", 12, "bold"))
        right_frame.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=True)

        # Labels and comboboxes for current course
        current_course_labels = ["Department:", "Course:", "Year:", "Semester:"]
        for i, label_text in enumerate(current_course_labels):
            label = Label(right_frame, text=label_text, font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
            label.grid(row=i, column=0, padx=10, pady=5, sticky=W)

            combo = ttk.Combobox(right_frame, font=("Arial", 12), state="readonly", width=20)
            if label_text == "Department:":
                combo["values"] = ("Select Department", "Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering")
            elif label_text == "Course:":
                combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
            elif label_text == "Year:":
                combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
            elif label_text == "Semester:":
                combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4")
            combo.current(0)
            combo.grid(row=i, column=1, padx=10, pady=5, sticky=W)

        # Dropdown for selecting search criteria
        search_criteria_label = Label(right_frame, text="Search by:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
        search_criteria_label.grid(row=len(current_course_labels), column=0, padx=10, pady=5, sticky=W)

        self.search_option_var = StringVar()
        search_dropdown = ttk.Combobox(right_frame, font=("Arial", 12), state="readonly", width=15, textvariable=self.search_option_var)
        search_dropdown["values"] = ("Search by","Roll No", "Phone No")
        search_dropdown.current(0)
        search_dropdown.grid(row=len(current_course_labels), column=1, padx=10, pady=5, sticky=W)

        # Submit and Show All buttons
        submit_button = Button(right_frame, text="Submit", command=self.search_student, font=("Arial", 12), bg=button_color, fg=button_text_color)
        submit_button.grid(row=len(current_course_labels) + 1, column=0, padx=10, pady=5, sticky=W)

        show_all_button = Button(right_frame, text="Show All", command=self.show_all_students, font=("Arial", 12), bg=button_color, fg=button_text_color)
        show_all_button.grid(row=len(current_course_labels) + 1, column=1, padx=10, pady=5, sticky=W)
        
        # Table frame with scrollbars
        table_frame = Frame(main_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=True)
        
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configure Treeview columns
        self.student_table.heading('#0', text='Department')
        self.student_table.heading('#1', text='Course')
        self.student_table.heading('#2', text='Year')
        self.student_table.heading('#3', text='Semester')
        self.student_table.heading('#4', text='ID')
        self.student_table.heading('#5', text='Name')
        self.student_table.heading('#6', text='Address')
        self.student_table.heading('#7', text='Teacher')
        self.student_table.heading('#8', text='Photo')

        # Add Treeview to the frame
        self.student_table.pack(fill='both', expand=True)

    def validate_date(self, value):
        if re.match(r'^\d{4}-\d{2}-\d{2}$', value) is not None:
            return True
        elif value == "":
            return True
        else:
            return False

    def save_student(self):
        # Logic to save student data
        pass

    def update_student(self):
        # Logic to update student data
        pass

    def delete_student(self):
        # Logic to delete student data
        pass

    def reset_fields(self):
        for entry in self.student_entries.values():
            entry.delete(0, END)

    def take_photo(self):
        # Logic to take photo sample
        pass

    def update_photo(self):
        # Logic to update photo sample
        pass

    def search_student(self):
        # Placeholder logic for searching student data
        search_option = self.search_option_var.get()
        search_text = self.search_entry.get()
        print(f"Searching for student by {search_option}: {search_text}")

    def show_all_students(self):
        # Placeholder logic for showing all students
        print("Showing all students")

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
