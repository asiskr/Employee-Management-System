from tkinter import *
from PIL import Image, ImageTk
from student import Student

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)  # Set fullscreen
        self.root.title("face recognition system")
        
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Load and resize image
        img = Image.open(r"C:\Users\AsisKaur\Downloads\download.jpeg")
        img = img.resize((screen_width, screen_height))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=screen_width, height=screen_height)

        title_lbl = Label(f_lbl, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=screen_width-55, height=45)


     # STUDENT BUTTON 
        img1=Image.open(r"C:\Users\AsisKaur\Downloads\download (3).jpg")
        img1=img1.resize((220,220))
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(f_lbl,image=self.photoimg1,cursor="hand2")
        b1.place(x=80,y=100,width=220,height=220)

        b1=Button(f_lbl,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1.place(x=80,y=300,width=220,height=40)


     #DETECT FACE BUTTON 
        
        img2=Image.open(r"C:\Users\AsisKaur\Downloads\FaceDetector.jpg")
        img2=img2.resize((220,220))
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(f_lbl,image=self.photoimg2,cursor="hand2")
        b1.place(x=380,y=100,width=220,height=220)

        b1=Button(f_lbl,text="Face Deector",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1.place(x=380,y=300,width=220,height=40)


     #ATTENDANCE FACE BUTTON
        
        img3=Image.open(r"C:\Users\AsisKaur\Downloads\Attendance.png")
        img3=img3.resize((220,220))
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(f_lbl,image=self.photoimg3,cursor="hand2")
        b1.place(x=680,y=100,width=220,height=220)

        b1=Button(f_lbl,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1.place(x=680,y=300,width=220,height=40)


     #HELP FACE BUTTON 
        
        img4=Image.open(r"C:\Users\AsisKaur\Downloads\Helpdesk.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(f_lbl,image=self.photoimg4,cursor="hand2")
        b1.place(x=980,y=100,width=220,height=220)

        b1=Button(f_lbl,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1.place(x=980,y=300,width=220,height=40)

        
     #TRAIN FACE BUTTON 
        
        img5=Image.open(r"C:\Users\AsisKaur\Downloads\Train data.png")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(f_lbl,image=self.photoimg5,cursor="hand2")
        b1.place(x=80,y=380,width=220,height=220)

        b1=Button(f_lbl,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1.place(x=80,y=580,width=220,height=40)


     #PHOTOS FACE BUTTON 
    
        img6=Image.open(r"C:\Users\AsisKaur\Downloads\photos.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(f_lbl,image=self.photoimg6,cursor="hand2")
        b1.place(x=380,y=380,width=220,height=220)

        b1=Button(f_lbl,text="Photo",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1.place(x=380,y=580,width=220,height=40)


     #DEVELOPER FACE BUTTON 
        
        img7=Image.open(r"C:\Users\AsisKaur\Downloads\developer.png")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(f_lbl,image=self.photoimg7,cursor="hand2")
        b1.place(x=680,y=380,width=220,height=220)

        b1=Button(f_lbl,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1.place(x=680,y=580,width=220,height=40)


     #EXIT FACE BUTTON 
        
        img8=Image.open(r"C:\Users\AsisKaur\Downloads\exit.png")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(f_lbl,image=self.photoimg8,cursor="hand2")
        b1.place(x=980,y=380,width=220,height=220)

        b1=Button(f_lbl,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1.place(x=980,y=580,width=220,height=40)




if __name__== "__main__":
    root=Tk()
    object=Face_Recognition_System(root)
    root.mainloop()