from tkinter import *
from PIL import Image, ImageTk
from student import Student  # Assuming Student class is implemented properly

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        # Background Image
        img3 = Image.open("C:\Users\AsisKaur\Downloads\download.jpeg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=710)

        # Student Button
        img1 = Image.open("C:/Users/AsisKaur/Downloads/download (3).jpg")
        img1 = img1.resize((300, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(self.root, image=self.photoimg1, command=self.student_detail, cursor="hand2")
        b1.place(x=10, y=10, width=300, height=130)

        b1_1 = Button(self.root, text="STUDENTS DETAILS", command=self.student_detail, cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=10, y=150, width=300, height=25)

        # Attendance Button
        img5 = Image.open("C:/Users/AsisKaur/Downloads/Attendance.png")
        img5 = img5.resize((300, 130), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5 = Button(self.root, image=self.photoimg5, cursor="hand2")
        b5.place(x=620, y=10, width=300, height=130)

        b5_1 = Button(self.root, text="ATTENDANCE", cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=620, y=150, width=300, height=25)

        # Photos Button
        img7 = Image.open("C:/Users/AsisKaur/Downloads/photos.jpg")
        img7 = img7.resize((300, 130), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b7 = Button(self.root, image=self.photoimg7, cursor="hand2")
        b7.place(x=1230, y=10, width=300, height=130)

        b7_1 = Button(self.root, text="PHOTOS", cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        b7_1.place(x=1230, y=150, width=300, height=25)

        # Train Data Button
        img6 = Image.open("C:/Users/AsisKaur/Downloads/Train data.png")
        img6 = img6.resize((300, 130), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6 = Button(self.root, image=self.photoimg6, cursor="hand2")
        b6.place(x=10, y=290, width=300, height=130)

        b6_1 = Button(self.root, text="TRAIN DATA", cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=10, y=430, width=300, height=25)

        # FaceDetector Button
        img2 = Image.open("C:/Users/AsisKaur/Downloads/FaceDetector.jpg")
        img2 = img2.resize((300, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2 = Button(self.root, image=self.photoimg2, cursor="hand2")
        b2.place(x=620, y=290, width=300, height=130)

        b2_1 = Button(self.root, text="FACE DETECTOR", cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=620, y=430, width=300, height=25)

        # HelpDesk Button
        img4 = Image.open("C:/Users/AsisKaur/Downloads/Helpdesk.jpg")
        img4 = img4.resize((300, 130), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4 = Button(self.root, image=self.photoimg4, cursor="hand2")
        b4.place(x=1230, y=290, width=300, height=130)

        b4_1 = Button(self.root, text="HELPDESK", cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=1230, y=430, width=300, height=25)

        # Developer Button
        img8 = Image.open("C:/Users/AsisKaur/Downloads/developer.png")
        img8 = img8.resize((300, 130), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b8 = Button(self.root, image=self.photoimg8, cursor="hand2")
        b8.place(x=10, y=570, width=300, height=130)

        b8_1 = Button(self.root, text="DEVELOPER", cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        b8_1.place(x=10, y=710, width=300, height=25)

        # Exit Button
        img9 = Image.open("C:/Users/AsisKaur/Downloads/exit.png")
        img9 = img9.resize((300, 130), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b9 = Button(self.root, image=self.photoimg9, cursor="hand2")
        b9.place(x=1230, y=570, width=300, height=130)

        b9_1 = Button(self.root, text="EXIT", cursor="hand2", font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        b9_1.place(x=1230, y=710, width=300, height=25)
        
        # Define other functions here...

    def student_detail(self):
        self.new_window = Toplevel(self.root)
        # Assuming Student class is defined here and implemented properly
        self.app = Student(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
