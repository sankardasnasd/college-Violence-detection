from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type =models.CharField(max_length=100)

class Department(models.Model):
    department=models.CharField(max_length=100)

class Course(models.Model):
    course=models.CharField(max_length=100)
    no_of_semester=models.CharField(max_length=100)
    DEPARTMENT=models.ForeignKey(Department,on_delete=models.CASCADE)

class Student(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.BigIntegerField()
    e_mail=models.CharField(max_length=100)
    image=models.CharField(max_length=350)
    gender=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()
    parent_name=models.CharField(max_length=100)
    parent_number=models.BigIntegerField()
    parent_e_mail_id=models.CharField(max_length=100)
    semester=models.CharField(max_length=100,default=1)
    dob=models.DateField()
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    COURSE=models.ForeignKey(Course,on_delete=models.CASCADE)

class Staff(models.Model):
    name=models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    gender = models.CharField(max_length=100)
    e_mail=models.CharField(max_length=100)
    image=models.CharField(max_length=350)
    dob = models.DateField()
    qulification=models.CharField(max_length=100,default="")
    DEPARTMENT=models.ForeignKey(Department,on_delete=models.CASCADE)

class Authority(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    gendre = models.CharField(max_length=100)
    age = models.DateField()
    image=models.CharField(max_length=350)
    e_mail=models.CharField(max_length=100)
    # e_mail=models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class Incident(models.Model):
    date=models.DateField()
    incident=models.CharField(max_length=100)
    description=models.CharField(max_length=100)


class Violence(models.Model):
    date=models.DateField()
    time=models.CharField(max_length=100)
    image=models.CharField(max_length=350)
class Incident_sub_images(models.Model):
    VIOLENCE= models.ForeignKey(Violence, on_delete=models.CASCADE)
    image= models.CharField(max_length=500)


class checkin_chechout(models.Model):
    checkin_checkout=models.CharField(max_length=100)
    date = models.DateField()
    status=models.CharField(max_length=100)
    STUDENT=models.ForeignKey(Student, on_delete=models.CASCADE)


class Attendance(models.Model):
    date=models.DateField()
    checkin_checkout=models.CharField(max_length=100)
    time = models.TimeField()
    photo = models.CharField(max_length=200)
    STUDENT=models.ForeignKey(Student, on_delete=models.CASCADE)

class Feedback(models.Model):
    date=models.DateField()
    feedback=models.CharField(max_length=100)
    # PARENT=models.ForeignKey(Student, on_delete=models.CASCADE)
    LOGIN=models.ForeignKey(Login, on_delete=models.CASCADE)

class Complaint(models.Model):
    date=models.DateField(default="")
    status = models.CharField(max_length=100,default="")
    complaint=models.CharField(max_length=100,default="")
    reply=models.CharField(max_length=100,default="")
    PARENT = models.ForeignKey(Login, on_delete=models.CASCADE,default="")


class Alert(models.Model):
    title=models.CharField(max_length=100)
    date = models.DateField()
    alert=models.CharField(max_length=100)

class Action(models.Model):
    action=models.CharField(max_length=100)
    date = models.DateField()
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    ALERT=models.ForeignKey(Alert,on_delete=models.CASCADE)

class Chat(models.Model):
    date = models.DateField()
    massege=models.CharField(max_length=100)
    FROMID=models.ForeignKey(Login, on_delete=models.CASCADE,related_name="fuser")
    TOID=models.ForeignKey(Login, on_delete=models.CASCADE,related_name="tuser")

class Notification(models.Model):
    date = models.DateField()
    notification=models.CharField(max_length=100)
    AUTHORITY=models.ForeignKey(Authority,on_delete=models.CASCADE)

class Security_guard(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    e_mail = models.CharField(max_length=100)
    image = models.CharField(max_length=350)
    age = models.DateField()
    gender = models.CharField(max_length=100)
    image=models.CharField(max_length=350)

class message(models.Model):
    message=models.CharField(max_length=100)
    date=models.DateField()
    AUTHORITY=models.ForeignKey(Authority,on_delete=models.CASCADE)



class violence_included_face(models.Model):
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)
    VIOLENCE=models.ForeignKey(Violence,on_delete=models.CASCADE)


