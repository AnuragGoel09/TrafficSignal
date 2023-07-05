import cv2
import tkinter as tk
from PIL import Image,ImageTk
import time
import math
# 1 and 2 are opposite cameras and 3 and 4 are opposite cameras 
mintime=10
maxTime=60
timeRequired=mintime
lane1=2
lane2=2
lane3=2
lane4=2
red=False
cam1=cv2.VideoCapture('video2.avi')
cam2=cv2.VideoCapture('video2.avi')
cam3=cv2.VideoCapture('video1.avi')
cam4=cv2.VideoCapture('video1.avi')   

root=tk.Tk()
root.geometry("1080x1080")
root.config(bg="black")
root.title("Traffic Management System")

# widgets

# Camera Frame

f1=tk.LabelFrame(root,bg="black")
f1.place(x=440,y=0)
L1=tk.Label(f1,bg="black")
L1.pack()

f2=tk.LabelFrame(root,bg="black")
f2.place(x=440,y=580)
L2=tk.Label(f2,bg="black")
L2.pack()

f3=tk.LabelFrame(root,bg="black")
f3.place(x=0,y=300)
L3=tk.Label(f3,bg="black")
L3.pack()

f4=tk.LabelFrame(root,bg="black")
f4.place(x=880,y=300)
L4=tk.Label(f4,bg="black")
L4.pack()

# Traffic Lights
canvas1=tk.Canvas(width=40,height=125,bg="black")
canvas1.place(x=380,y=10)
canvas2=tk.Canvas(width=40,height=125,bg="black")
canvas2.place(x=380,y=590)
canvas3=tk.Canvas(width=40,height=125,bg="black")
canvas3.place(x=230,y=300)
canvas4=tk.Canvas(width=40,height=125,bg="black")
canvas4.place(x=810,y=300)

# Main Heading
Title = tk.Label(root, text="Automatic Traffic Signal \n Manegement System", font=('Helvetica 15'))
Title.place(x=0,y=0)

# Timer heading
timeHead=tk.Label(root,text="Timer",font=("Helvetica", "16"))
timeHead.place(x=1000,y=10)

# Timer
timer = tk.Label(root, text=timeRequired,font=("Helvetica", "16"))
timer.place(x=1000,y=50)

# helps to identify vehicles
cascade_path='cars.xml'
classifier = cv2.CascadeClassifier(cascade_path)
cap=cv2.VideoCapture('video1.avi')

def count(cam1,cam2,cam3,cam4,runTime,L1,L2,L3,L4,red):
    try:
        start=time.time()
        while (time.time()-start)<runTime:
            c1=0
            #camera 1
            ret,frame1=cam1.read()
            if (type(frame1) == type(None)):
                break
            gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            vehicles = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
            c1=len(vehicles)/lane1
            for (x, y, w, h) in vehicles:
                cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            resized1 = cv2.resize(frame1, (200,200), interpolation= cv2.INTER_LINEAR)
            img1=ImageTk.PhotoImage(Image.fromarray(resized1))
            L1["image"]=img1
            
            #camera 2
            ret,frame2=cam2.read()
            if (type(frame2) == type(None)):
                break
            gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
            vehicles = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
            c1+=len(vehicles)/lane2
            # counting=c
            for (x, y, w, h) in vehicles:
                cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)
            resized2 = cv2.resize(frame2, (200,200), interpolation= cv2.INTER_LINEAR)
            img2=ImageTk.PhotoImage(Image.fromarray(resized2))
            L2["image"]=img2


            c2=0
            #camera 3
            ret,frame3=cam3.read()
            if (type(frame3) == type(None)):
                break
            gray = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
            vehicles = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
            c2=len(vehicles)/lane3
            for (x, y, w, h) in vehicles:
                cv2.rectangle(frame3, (x, y), (x+w, y+h), (0, 255, 0), 2)
            resized3 = cv2.resize(frame3, (200,200), interpolation= cv2.INTER_LINEAR)
            img3=ImageTk.PhotoImage(Image.fromarray(resized3))
            L3["image"]=img3
            
            #camera 4
            ret,frame4=cam4.read()
            if (type(frame4) == type(None)):
                break
            gray = cv2.cvtColor(frame4, cv2.COLOR_BGR2GRAY)
            vehicles = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
            c2+=len(vehicles)/lane4
            for (x, y, w, h) in vehicles:
                cv2.rectangle(frame4, (x, y), (x+w, y+h), (0, 255, 0), 2)
            resized4 = cv2.resize(frame4, (200,200), interpolation= cv2.INTER_LINEAR)
            img4=ImageTk.PhotoImage(Image.fromarray(resized4))
            L4["image"]=img4
            root.update()
            if cv2.waitKey(33) == 27:
                break 
        if(red):
            return c2
        return c1
    except:
        print("Terminated")

def initialLight(canvas1,canvas2,canvas3,canvas4):
    canvas1.create_oval(3,3,40,40,fill="red")
    canvas1.create_oval(3,40+3,40,40+40,fill="white")
    canvas1.create_oval(3,80+3,40,80+40,fill="white")
    canvas2.create_oval(3,3,40,40,fill="red")
    canvas2.create_oval(3,40+3,40,40+40,fill="white")
    canvas2.create_oval(3,80+3,40,80+40,fill="white")
    
    canvas3.create_oval(3,3,40,40,fill="white")
    canvas3.create_oval(3,40+3,40,40+40,fill="white")
    canvas3.create_oval(3,80+3,40,80+40,fill="green")
    canvas4.create_oval(3,3,40,40,fill="white")
    canvas4.create_oval(3,40+3,40,40+40,fill="white")
    canvas4.create_oval(3,80+3,40,80+40,fill="green")

def changeLights(canvas1,canvas2,canvas3,canvas4):# 1 and 2 g to r and 3 and 4 r to g
    label = tk.Label(root, text=" Changing Lights", font=('Helvetica 15'))
    label.pack(pady=20)
    canvas1.create_oval(3,3,40,40,fill="white")
    canvas1.create_oval(3,40+3,40,40+40,fill="white")
    canvas1.create_oval(3,80+3,40,80+40,fill="green")
    canvas2.create_oval(3,3,40,40,fill="white")
    canvas2.create_oval(3,40+3,40,40+40,fill="white")
    canvas2.create_oval(3,80+3,40,80+40,fill="green")
    
    canvas3.create_oval(3,3,40,40,fill="red")
    canvas3.create_oval(3,40+3,40,40+40,fill="white")
    canvas3.create_oval(3,80+3,40,80+40,fill="white")
    canvas4.create_oval(3,3,40,40,fill="red")
    canvas4.create_oval(3,40+3,40,40+40,fill="white")
    canvas4.create_oval(3,80+3,40,80+40,fill="white")
    
    root.update()
    time.sleep(1)
    canvas1.create_oval(3,40+3,40,40+40,fill="orange")
    canvas1.create_oval(3,80+3,40,80+40,fill="white")
    canvas2.create_oval(3,40+3,40,40+40,fill="orange")
    canvas2.create_oval(3,80+3,40,80+40,fill="white")
    
    canvas3.create_oval(3,3,40,40,fill="white")
    canvas3.create_oval(3,40+3,40,40+40,fill="orange")
    canvas4.create_oval(3,3,40,40,fill="white")
    canvas4.create_oval(3,40+3,40,40+40,fill="orange")
    
    root.update()
    time.sleep(1)
    canvas1.create_oval(3,3,40,40,fill="red")
    canvas1.create_oval(3,40+3,40,40+40,fill="white")
    canvas2.create_oval(3,3,40,40,fill="red")
    canvas2.create_oval(3,40+3,40,40+40,fill="white")
    
    canvas3.create_oval(3,40+3,40,40+40,fill="white")
    canvas3.create_oval(3,80+3,40,80+40,fill="green")
    canvas4.create_oval(3,40+3,40,40+40,fill="white")
    canvas4.create_oval(3,80+3,40,80+40,fill="green")
    label.destroy()
    root.update()


initialLight(canvas1,canvas2,canvas3,canvas4)
c1=canvas3
c2=canvas4
c3=canvas1
c4=canvas2
def swap(a,b):
    temp=a
    a=b
    b=temp
    return [a,b]

def update():
    if(timer['text']==0):
        return
    timer.config(text=timer['text']-1)
    timer.after(1000, update)

def run(timeRequired,red,c1,c2,c3,c4):
    button.destroy()
    try:
        while True:
            update()
            timeRequired=count(cam1,cam2,cam3,cam4,timeRequired,L1,L2,L3,L4,red)*2.5
            print("shit")
            if(timeRequired<mintime):
                timeRequired=mintime
            if(timeRequired>maxTime):
                timeRequired=maxTime      
            changeLights(c1,c2,c3,c4)
            [c1,c3]=swap(c1,c3)
            [c2,c4]=swap(c2,c4)
            timer.config(text=math.ceil(timeRequired))
            red=not red             
    except:
        print("Software Terminated")
button=tk.Button(root,text="Start",command=lambda:run(timeRequired,red,c1,c2,c3,c4),font = "Verdana 20 underline",bg="Blue",fg="white")
button.pack(pady=200)
b=tk.Button(root,text="Stop",command=lambda:root.destroy(),font = "Verdana 20 underline",bg="Blue",fg="white")
b.place(x=900,y=700)
    
# run()
root.mainloop()

cv2.destroyAllWindows()