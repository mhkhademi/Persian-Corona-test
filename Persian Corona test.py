import tkinter
from tkinter import messagebox
#hide main window
t = tkinter.Tk()
t.withdraw()
v=0
x = messagebox.askyesno("تست کرونا","تست کرونا.مي خواهيد ادامه دهيد؟", default= messagebox.YES)
if x==True:
    y=messagebox.askyesno("سوال اول","آيا اخيرا لرز داشتيد؟")
    if y==True:
        v = v+1
    z=messagebox.askyesno("سوال دوم","آيا سرفه مي کنيد؟")
    if z==True:
        v = v+1
    r=messagebox.askyesno("سوال سوم","آيا گلودرد داريد؟")
    if r==True:
        v = v+1
    f=messagebox.askyesno("سوال چهارم","آيا دچار بدن درد و بي حالي هستيد؟")
    if f==True:
        v = v+1
    g=messagebox.askyesno("سوال پنجم","آيا استفراغ و اسهال داريد؟")
    if g==True:
        v = v+1
    h=messagebox.askyesno("سوال ششم","آيا اخيرا تب داشتيد؟")
    if h==True:
        v = v+1
    j=messagebox.askyesno("سوال هفتم","آيا مشکلات تنفسي و نفس تنگي داريد؟")
    if j==True:
        v = v+1
    k=messagebox.askyesno("سوال هشتم","آيا کاهش حس بويايي و چشايي داريد؟")
    if k==True:
        v = v+1
if v==0:
    messagebox.showinfo("جواب تست کرونا",".شما کرونا نداريد")
elif v==1:
    messagebox.showinfo("جواب تست کرونا",".شما مشکوک به کرونا هستيد")
elif v==2 or v==3:
    messagebox.ashowinfo("جواب تست کرونا",".شما مبتلا به کروناي خفيف هستيد")
elif v==4 or v==5:
    messagebox.showinfo("جواب تست کرونا",".شما مبتلا به کروناي شديد هستيد")
elif v==6 or v==7 or v==8:
    messagebox.showinfo("جواب تست کرونا",".شما مبتلا به کروناي بحراني هستيد")
a=messagebox.askyesno("درباره ما","آيا مي خواهيد در مورد اين برنامه و سازنده آن اطلاعات کسب کنيد؟")
if a==True:
    messagebox.showinfo("اطلاعات برنامه و سازنده آن","اين برنامه با استفاده از زبان برنامه نويسي پايتون نوشته شده است و نويسنده اين .برنامه آقاي محمد حسين خادمي است")
