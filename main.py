from tkinter import *
from tensorflow.keras.models import model_from_json
from sklearn import metrics
from PIL import *
import numpy as np
import cv2
def FacialExpressionModel(json_file,weight_file):
    with open(json_file,"r") as file:
        loaded_model_json=file.read()
        model=model_from_json(loaded_model_json)
    model.load_weights(weight_file)
    model.compile(optimizer="adam",loss="categorical_crossentropy",metrice=["accuracy"])
    return model
def Detect(file_path):
    global Label_packed
    img=cv2.imread(file_path)
    gray_img=cv2.cvtcolor(img,cv2.COLOR_BGR2GRAY)
    faces=faces.detectMultiScale(gray_img,1.3,5)
    try:
        for (x,y,w,h) in faces:
            fc=grey_image[y:y+h,x:x+w]
            roi=cv2.resize(fc,(48,48))
            pred=EMOTION_LIST[np.argMax(model.predict(roi[np.newaxis,:,:,np.newaxis]))]
            print("predicated Emotion is"+pred)
            lable.config(fg="#011638",text=pred)
    except:
        label.config(fg="#011638",text="Unable to detect")
def Show_Detect_Image(file_path):
    detect_b=Button(window,text="Detect Emotion",command=lambda:Detect(file_path),padx=10,pady=5)
    detect_b.config(bg="#364156",fg="white",font=("ariel",14,"bold"))
    detect_b.place(relax=0.79,rely=0.46)
def upload_image():
    try:
        file_path=filedialog.askopenfile()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((window.wininfo_width()/2.3),(window.wininfo_height()/2.3)))
        im=PhotoImage(uploaded)
        sign_image.config(image=im)
        sign_image.image=im
        label.config(text="")
        Show_Detect_Image(filoe_path)
    except:
        pass
    
    
    
window=Tk()
window.geometry=("800 × 500 ")
window.title("Face Detection App")
window.config(bg="#cdcdcd")

label=Label(window,bg="#cdcdcd",font=("ariel",14,"bold"))
sign_image=Label(window)

faces=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
model=FacialExpressionModel("model_a1.json","model_weights1.h5")

EMOTION_LIST=["Angry","Disgust","Fear","Happy","Neutral","Sad","Suprise"]
upload=Button(window,text="Upload a Image",command=upload_image,padx=10,pady=5)
upload.config(bg="#364156",fg="white",font=("ariel",14,"bold"))
upload.pack(side="bottom",pady=50)
sign_image.pack(side="bottom",expand="True")
lebel.pack(side="bottom",expand="True")
headings=Label(window,text="Emotion Detector App",pady=20,font=("ariel",20,"Italic"))
headings.config(bg="#cdcdcd",fg="#364156")
headings.pack()
window.mainloop()