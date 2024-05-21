from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class xyz:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        
        # Load and resize images
        img1 = self.load_and_resize_image(r"C:\Users\AsisKaur\Downloads\download (3).jpg", (300, 130))
        img2 = self.load_and_resize_image(r"C:\Users\AsisKaur\Downloads\Student portal.jpg", (300, 130))
        img3 = self.load_and_resize_image(r"C:\Users\AsisKaur\Downloads\face.jpg", (1530, 710))

        # Place buttons and labels
        self.create_button_with_image(img1, 10, 10, 300, 130, "STUDENTS DETAILS")
        self.create_button_with_image(img2, 1220, 10, 300, 130, "FACE DETECTOR")
        self.create_label_with_image(img3, 0, 130, 1530, 710, "STUDENT MANAGEMENT SYSTEM")

        # Create main frame
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=0, y=0, width=1500, height=650)
        
        # Create left and right label frames
        self.LEFT_frame = self.create_label_frame(main_frame, 10, 10, 760, 580, "STUDENT DETAILS")
        self.RIGHT_frame = self.create_label_frame(main_frame, 750, 10, 660, 580, "STUDENT DETAILS")

        # Create current course frame
        self.create_current_course_frame(self.LEFT_frame, 5, 130, 720, 200)

        # Create class student information frame
        self.class_Student_frame = self.create_label_frame(self.LEFT_frame, 5, 260, 720, 400, "Class student information")

        # Add labels and entry widgets
        self.create_label_and_entry(self.class_Student_frame, "StudentId", 0, 0)

    def load_and_resize_image(self, path, size):
        img = Image.open(path)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def create_button_with_image(self, image, x, y, width, height, text):
        button = Button(self.root, image=image, cursor="hand2")
        button.place(x=x, y=y, width=width, height=height)
        label = Button(self.root, text=text, cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        label.place(x=x, y=y+height, width=width, height=25)

    def create_label_with_image(self, image, x, y, width, height, text):
        label = Label(self.root, image=image)
        label.place(x=x, y=y, width=width, height=height)
        title_lbl = Label(self.root, text=text, font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=x, y=y, width=width, height=45)

    def create_label_frame(self, parent, x, y, width, height, text):
        label_frame = LabelFrame(parent, bd=2, bg="white", relief=RIDGE, text=text, font=("times new roman", 12, "bold"))
        label_frame.place(x=x, y=y, width=width, height=height)
        return label_frame

    def create_current_course_frame(self, parent, x, y, width, height):
        current_course_frame = LabelFrame(parent, bd=2, bg="white", relief=RIDGE, text="Current course", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=x, y=y, width=width, height=height)

        self.create_combo_box(current_course_frame, "Department", 0, 0, ("Select Department", "Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering"))
        self.create_combo_box(current_course_frame, "Course", 0, 2, ("Select Course", "FE", "SE", "TE", "BE"))
        self.create_combo_box(current_course_frame, "Year", 1, 0, ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24"))
        self.create_combo_box(current_course_frame, "Semester", 1, 2, ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4"))

    def create_combo_box(self, parent, label_text, row, column, values):
        label = Label(parent, text=label_text, font=("times new roman", 13, "bold"), bg="white")
        label.grid(row=row, column=column, padx=10, sticky=W)

        combo_box = ttk.Combobox(parent, font=("times new roman", 13, "bold"), state="readonly", width=20)
        combo_box["values"] = values
        combo_box.current(0)
        combo_box.grid(row=row, column=column+1, padx=2, pady=10, sticky=W)

    def create_label_and_entry(self, parent, label_text, row, column):
        label = Label(parent, text=label_text, font=("times new roman", 13, "bold"), bg="white")
        label.grid(row=row, column=column, padx=10, sticky=W)

        entry = ttk.Entry(parent, font=("times new roman", 13, "bold"), background="white")
        entry.grid(row=row, column=column+1, padx=10, sticky=W)


if __name__ == "__main__":
    root = Tk()
    obj = xyz(root)
    root.mainloop()