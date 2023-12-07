from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *


def adminhome(request):

    if request.session['lid']=='':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')

    return render(request,'Admin/aindex.html')

def login(request):
    return render(request,'login_index.html')

def login_post(request):
    uname=request.POST['textfield']
    password=request.POST['textfield2']
    log=Login.objects.filter(username=uname,password=password)
    if log.exists():
        log1=Login.objects.get(username=uname,password=password)
        request.session['lid']=log1.id
        if log1.type=='admin':
            return HttpResponse('''<script>alert('login successfullly');window.location='/myapp/adminhome/'</script>''')
        elif log1.type=='authority':
            return HttpResponse('''<script>alert('login successfullly');window.location='/myapp/authorityhome/'</script>''')
        else:
            return HttpResponse('''<script>alert('login failed');window.location='/myapp/login/'</script>''')

    else:
        return HttpResponse('''<script>alert('login failed');window.location='/myapp/login/'</script>''')


def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>window.location='/myapp/login/'</script>''')


def adminchangepassword(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')

    return render(request,'Admin/change password.html')

def adminchangepassword_post(request):
   currentpassword = request.POST['textfield']
   newpassword = request.POST['textfield2']
   confirmpassword=request.POST['textfield3']
   log=Login.objects.get(id=request.session['lid'],password=currentpassword)
   if newpassword==confirmpassword:
        log1 = Login.objects.filter(id=request.session['lid'], password=currentpassword).update(password=confirmpassword)
        request.session['lid']=''

        return HttpResponse('''<script>alert('password change success');window.location='/myapp/login/'</script>''')
   else:
        return HttpResponse('''<script>alert('password not change ');window.location='/myapp/adminchangepassword/'</script>''')

def adminadddepartment(request):

    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')

    return render(request,'Admin/Add Department.html')

def adminadddepartment_post(request):




     deptname=request.POST['textfield']

     dpt=Department()
     dpt.department=deptname
     dpt.save()
     return HttpResponse('''<script>alert('department added');window.location='/myapp/adminadddepartment/'</script>''')



def adminviewdepartment(request):

    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    res=Department.objects.all()
    return render(request,'Admin/View department.html',{'data':res})

def adminviewdepartment_post(request):

     search=request.POST['textfield']
     res = Department.objects.filter(department__icontains=search)
     return render(request, 'Admin/View department.html', {'data': res})

def admineditdepartment(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    data=Department.objects.get(id=id)
    return render(request,'Admin/Edit Department.html',{'dt':data})

def admineeditdepartment_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    deptname=request.POST['textfield']
    id=request.POST['id']

    dobj=Department.objects.get(id=id)
    dobj.department=deptname
    dobj.save()
    return HttpResponse('''<script>alert('Successfully edited');window.location='/myapp/adminviewdepartment/'</script>''')

def admindeletedepartment(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    data=Department.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert('Successfully deleted');window.location='/myapp/adminviewdepartment/'</script>''')

def adminaddcourse(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    dobj=Department.objects.all()
    return render(request,'Admin/Add Course.html',{"data":dobj})




def adminaddcourse_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    deptname=request.POST['select']
    course=request.POST['select2']
    noofsem=request.POST['select3']
    crs=Course()
    crs.course=course
    crs.no_of_semester=noofsem
    crs.DEPARTMENT_id=deptname
    crs.save()

    return HttpResponse('''<script>alert('course added');window.location='/myapp/adminaddcourse/'</script>''')


def adminviewcourse(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    dpt=Course.objects.all()
    return render(request,'Admin/View Course.html',{'data':dpt})

def adminviewcourse_POST(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    search=request.POST['textfield']
    dpt=Course.objects.filter(course__icontains=search)
    return render(request, 'Admin/view course.html',{'data':dpt })




def admineditcourse(request, id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    data = Course.objects.get(id=id)
    data1=Department.objects.all()
    return render(request, 'Admin/Edit Course.html',{'dt':data,'dt1':data1})

def admineditcourse_POST(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    dptname=request.POST['select']
    course=request.POST['cource']
    nosem=request.POST['nos']
    id=request.POST['id']

    dobj=Course.objects.get(id=id)
    dobj.DEPARTMENT_id=dptname
    dobj.course=course
    dobj.no_of_semester=nosem
    dobj.save()
    return HttpResponse('''<script>alert('Successfully edited');window.location='/myapp/adminviewcourse/'</script>''')









def admindeletecourse(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    data=Course.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert('Successfully deleted');window.location='/myapp/adminviewcourse/'</script>''')


def adminaddstudent(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    crs = Course.objects.all()
    import datetime
    dty=datetime.date.today()
    dt=str(dty.year-18)+"-"+str(dty.month)+"-"+str(dty.day)
    return render(request, 'Admin/Add student.html', {'data': crs,"dt":dt})

def adminaddstudent_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    name=request.POST['textfield']
    course=request.POST['select']
    phnum=request.POST['textfield2']
    gender=request.POST['RadioGroup1']
    dob=request.POST['select2']
    place=request.POST['textfield3']
    city=request.POST['textfield4']
    dis=request.POST['select3']
    state=request.POST['select4']
    pin=request.POST['textfield5']
    email=request.POST['textfield6']
    paraentname=request.POST['textfield7']
    paraentnum=request.POST['textfield8']
    parent_e_mail_id=request.POST['textfield18']
    semester=request.POST['semseter']
    photo=request.FILES['fileField']

    if Login.objects.filter(username=email).exists():
        return HttpResponse('''<script>alert('student mail already exists');history.back()</script>''')

    lobj=Login()
    lobj.username=email
    lobj.password=phnum
    lobj.type='student'
    lobj.save()
    if not Login.objects.filter(username=parent_e_mail_id).exists():
        lobj2 = Login()
        lobj2.username = parent_e_mail_id
        lobj2.password = paraentnum
        lobj2.type = 'parent'
        lobj2.save()
    stdnt=Student()
    stdnt.name=name
    stdnt.phone_number= phnum
    stdnt.e_mail= email

    from datetime import datetime
    date=datetime.now().strftime('%Y%m%d-%H%M%S') +".jpg"
    fs=FileSystemStorage()
    fs.save(date,photo)
    path=fs.url(date)
    stdnt.image=path

    stdnt.gender=gender
    stdnt.dob=dob
    stdnt.semester=semester
    stdnt.place=place
    stdnt.city=city
    stdnt.district=dis
    stdnt.state=state
    stdnt.pincode=pin
    stdnt.parent_name=paraentname
    stdnt.parent_number=paraentnum
    stdnt.parent_e_mail_id=parent_e_mail_id
    stdnt.COURSE_id=course
    stdnt.LOGIN=lobj
    stdnt.save()
    return HttpResponse('''<script>alert('student added');window.location='/myapp/adminaddstudent/'</script>''')






def admineditstudent(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    data=Student.objects.get(id=id)
    dat=Course.objects.all()
    return render(request,'Admin/EditStudent.html',{'dt':data,'data':dat})

def admineditstudent_POST(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    name = request.POST['textfield']
    course = request.POST['select']
    phnum = request.POST['textfield2']
    gender = request.POST['RadioGroup1']
    dob = request.POST['select2']
    place = request.POST['textfield3']
    city = request.POST['textfield4']
    dis = request.POST['select3']
    state = request.POST['select4']
    pin = request.POST['textfield5']
    semseter = request.POST['semseter']
    # email = request.POST['textfield6']
    paraentname = request.POST['textfield7']
    paraentnum = request.POST['textfield8']
    id=request.POST['id']

    stdnt = Student.objects.get(id=id)
    stdnt.name = name
    stdnt.phone_number = phnum
    # stdnt.e_mail = email
    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']
        if photo.name != '':
            from datetime import datetime
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
            fs = FileSystemStorage()
            fs.save(date, photo)
            path = fs.url(date)
            stdnt.image = path
    stdnt.gender = gender
    stdnt.dob = dob
    stdnt.place = place
    stdnt.city = city
    stdnt.district = dis
    stdnt.state = state
    stdnt.pincode = pin
    stdnt.semseter = semseter
    stdnt.parent_name = paraentname
    stdnt.parent_number = paraentnum
    stdnt.COURSE_id = course
    stdnt.save()
    return HttpResponse('''<script>alert('student added');window.location='/myapp/adminviewstudent/'</script>''')


def admindeletestudent(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    data=Student.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert('Successfully deleted');window.location='/myapp/adminviewstudent/'</script>''')


def adminviewstudent(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    sobj=Student.objects.all()

    c=Course.objects.all()



    return render(request,'Admin/view student.html',{"data":sobj,'c':c})





def adminviewstudent_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    if request.POST["button"]=="Go":

        crs= request.POST["select"]
        sem= request.POST["semseter"]

        sobj = Student.objects.filter(COURSE_id=crs, semester=sem)
        c = Course.objects.all()
        return render(request, 'Admin/view student.html', {'data': sobj,'c':c})
    else:
        search=request.POST['textfield']
        sobj=Student.objects.filter(name__icontains=search)
        c = Course.objects.all()
        return render(request,'Admin/view student.html',{'data':sobj,'c':c})




def adminaddstaff(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    dpt = Department.objects.all()
    import datetime
    dty = datetime.date.today()
    dt = str(dty.year - 18) + "-" + str(dty.month) + "-" + str(dty.day)
    return render(request, 'Admin/Add staff.html', {'data': dpt,'dt':dt})


def adminaddstaff_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    name=request.POST['textfield']
    phnum=request.POST['textfield2']
    gender=request.POST['RadioGroup1']
    dept=request.POST['select']
    dd=Department.objects.get(id=dept)
    email=request.POST['textfield3']
    dob=request.POST['textfield4']
    photo=request.FILES['fileField']
    qualification=request.POST['textfield5']
    sobj=Staff()
    sobj.name=name
    sobj.phone_number=phnum
    sobj.gender=gender
    sobj.e_mail=email
    sobj.dob=dob
    sobj.qulification=qualification

    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)
    sobj.image = path

    sobj.DEPARTMENT=dd
    sobj.save()
    return HttpResponse('''<script>alert('staff added');window.location='/myapp/adminaddstaff/'</script>''')

def admineditstaff(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    data=Staff.objects.get(id=id)
    data2=Department.objects.all()
    import datetime
    dty = datetime.date.today()
    dt = str(dty.year - 18) + "-" + str(dty.month) + "-" + str(dty.day)

    return render(request,'Admin/Edit staff.html',{'dt':data,'dt2':data2, 'dt1':dt} )


def admineditstaff_POST(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    name = request.POST['textfield']
    phnum = request.POST['textfield2']
    gender = request.POST['RadioGroup1']
    dept = request.POST['select']
    dd = Department.objects.get(id=dept)
    email = request.POST['textfield3']
    dob = request.POST['textfield4']

    qualification = request.POST['textfield5']
    id=request.POST['id']
    sobj=Staff.objects.get(id=id)
    sobj.name=name
    sobj.phone_number=phnum
    sobj.gender=gender
    sobj.e_mail=email
    sobj.dob=dob
    sobj.qulification=qualification

    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']
        if photo.name!='':

            from datetime import datetime
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
            fs = FileSystemStorage()
            fs.save(date, photo)
            path = fs.url(date)
            sobj.image = path

    sobj.DEPARTMENT=dd
    sobj.save()
    return HttpResponse('''<script>alert('staff added');window.location='/myapp/adminviewstaff/'</script>''')



def adminviewstaff(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    sobj=Staff.objects.all()
    return render(request,'Admin/View staff.html',{"data":sobj})

def adminviewstaff_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    search=request.POST['textfield']
    sobj=Staff.objects.filter(name__icontains=search)
    return render(request,'Admin/View staff.html',{"data":sobj})

def admindeletestaff(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    data=Staff.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert('Successfullt deleted');windows.location='/myapp/adminviewstaff/'</script>''')


def adminaddauthority(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    import datetime
    dty = datetime.date.today()
    dt = str(dty.year - 18) + "-" + str(dty.month) + "-" + str(dty.day)
    return render(request,'Admin/Add authority.html',{"dt":dt})

def adminaddauthority_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    name=request.POST['textfield']
    Phnum=request.POST['textfield2']
    gender=request.POST['RadioGroup1']
    dob=request.POST['textfield3']
    email=request.POST['textfield4']
    # qualification=request.POST['textfield5']
    photo=request.FILES['fileField']

    if Login.objects.filter(username=email).exists():
        return HttpResponse(
            '''<script>alert('Mail Already Exists');history.back()</script>''')
    lobj=Login()
    lobj.username=email
    lobj.password=Phnum
    lobj.type='authority'
    lobj.save()


    aubj=Authority()
    aubj.name=name
    aubj.phone_number=Phnum
    aubj.age=dob
    aubj.e_mail=email
    # aubj.qulification=qualification
    aubj.gendre=gender

    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)
    aubj.image = path
    aubj.LOGIN=lobj
    aubj.save()
    return HttpResponse('''<script>alert('authority  added');window.location='/myapp/adminaddauthority/'</script>''')



def admineditauthority(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    data=Authority.objects.get(id=id)
    return render(request,'Admin/Edit authority.html',{'dt':data})

def admineditauthority_POST(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    name = request.POST['textfield']
    Phnum = request.POST['textfield2']
    gender = request.POST['RadioGroup1']
    dob = request.POST['textfield3']
    # email = request.POST['textfield4']
    # qualification = request.POST['textfield5']
    id=request.POST['id']


    aubj=Authority.objects.get(id=id)
    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']

        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)

        aubj.image = path
    aubj.name = name
    aubj.phone_number = Phnum
    aubj.age = dob
    # aubj.e_mail = email
    aubj.gendre = gender
    aubj.save()
    return HttpResponse(
        '''<script>alert('successfully edited');window.location='/myapp/adminviewauthority/'</script>''')


def admindeleteauthority(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    data=Authority.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert('successfully deleted');window.location='/myapp/adminviewauthority/'</script>''')


def adminviewauthority(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    sobj=Authority.objects.all()
    return render(request,'Admin/View authority.html',{'data':sobj})

def adminviewauthority_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    search=request.POST['textfield']
    sobj=Authority.objects.filter(name__icontains=search)
    return render(request,'Admin/View authority.html',{'data':sobj})


def adminaddincident(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    return render(request,'Admin/Add incident.html')

def adminaddincident_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    incident=request.POST['textfield']
    description=request.POST['textfield2']

    inbj=Incident()
    inbj.incident=incident
    inbj.description=description

    from datetime import datetime
    inbj.date = datetime.now()
    inbj.save()

    return HttpResponse('''<script>alert('incident added');window.location='/myapp/adminaddincident/'</script>''')


def admineditincident(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    data=Incident.objects.get(id=id)
    return render(request,'Admin/Edit incident.html',{'dt':data})

def admineditincident_POST(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    incident = request.POST['textfield']
    description = request.POST['textfield2']
    id=request.POST['id']

    inbj = Incident.objects.get(id=id)
    inbj.incident = incident
    inbj.description = description

    from datetime import datetime
    inbj.date = datetime.now()
    inbj.save()
    return HttpResponse('''<script>alert('successfully edited');window.location='/myapp/adminviewincident/'</script>''')


def admindeleteincident(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    data=Incident.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script>alert('successfully deleted');window.location='/myapp/adminviewincident/'</script>''')


def adminviewincident(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    sobj=Incident.objects.all()
    return render(request,'Admin/View incident.html',{"data":sobj})

def adminviewincident_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    search=request.POST['textfield']
    sobj=Incident.objects.filter(incident__icontains=search)
    return render(request, 'Admin/View incident.html',{'data':sobj})



def adminaddfeedback(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    return render(request,'Admin/Add feedback.html')

def adminaddfeedback_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    feedback=request.POST['textfield']

    febj=Feedback()
    febj.feedback=feedback
    from datetime import datetime
    febj.date = datetime.now()
    febj.PARENT=Student.objects.get(LOGIN_id=request.session['lid'])
    febj.save()

    return HttpResponse('''<script>alert('feedback added');window.location='/myapp/adminaddfeedback/'</script>''')


def admineditfeedback(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    return render(request,'Admin/Edit feedback.html')

def adminviewfeedback(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    febj=Feedback.objects.all()
    l=[]
    # for i in febj:
    #     l.append({"feedback":i.feedback,"date":i.date,"parentname":i.parentname})

    return render(request,'Admin/View feedback.html',{'data':febj})

def adminviewfeedback_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    febj = Feedback.objects.filter(date__range=[fromdate,todate])
    return render(request, 'Admin/View feedback.html', {'data': febj})

def adminviewcomplient(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    comj=Complaint.objects.all()
    return render(request,'Admin/view complaint.html',{'data':comj})

def adminviewcomplient_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    comj=Complaint.objects.filter(date__range=[fromdate,todate])
    return render(request,'Admin/view complaint.html',{'data':comj})


def adminSendrply(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    return render(request,'Admin/replay.html',{'id':id})

def adminsendrply_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    replay=request.POST['textarea']
    id=request.POST['id']
    robj=Complaint.objects.get(id=id)
    robj.reply=replay
    robj.status="replied"
    robj.save()
    return HttpResponse('''<script>alert('replyed');window.location='/myapp/adminviewcomplient/'</script>''')


def adminViewViolence(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    comj=Violence.objects.all()
    return render(request,'Admin/view Violence.html',{'data':comj})

def adminViewViolence_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    comj=Violence.objects.filter(date__range=[fromdate,todate])
    return render(request,'Admin/view violence.html',{'data':comj})

def adminViewIncludedFace(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    comj=violence_included_face.objects.filter(VIOLENCE_id=id)
    return render(request, 'Admin/View VIOLENCE INCLUDED FACE.html', {'data': comj, "id": id})

def adminViewIncludedFace_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    name = request.POST['textfield']
    id = request.POST['id']
    comj = violence_included_face.objects.filter(STUDENT__name__icontains=name, VIOLENCE_id=id)
    return render(request, 'Admin/View VIOLENCE INCLUDED FACE.html', {'data': comj, "id": id})

def delface(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    violence_included_face.objects.get(id=id).delete()
    return HttpResponse('''<script>window.location='/myapp/adminViewViolence/'</script>''')


##########################authority

def viewprofile(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    var=Authority.objects.get(LOGIN=request.session['lid'])
    return render(request,'authority/view_profile.html',{'data':var})


def authoritychangepassword(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    return render(request,'authority/change password.html')

def authoritychangepassword_post(request):
   currentpassword = request.POST['textfield']
   newpassword = request.POST['textfield2']
   confirmpassword=request.POST['textfield3']

   log=Login.objects.get(id=request.session['lid'],password=currentpassword)
   if newpassword==confirmpassword:
        log1 = Login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
        request.session['lid'] = ''

        return HttpResponse('''<script>alert('change success');window.location='/myapp/login/'</script>''')
   else:
        return HttpResponse('''<script>alert('password not change ');window.location='/myapp/authoritychangepassword/'</script>''')

def authorityhome(request):
    if request.session['lid'] == '':
        import datetime
        dty = datetime.date.today()
        dt = str(dty.year - 18) + "-" + str(dty.month) + "-" + str(dty.day)

        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    return render(request,'authority/authindex.html')

def authorityviewstudent(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    sobj=Student.objects.all()
    return render(request,'authority/authority_view_student.html',{"data":sobj})

def authorityviewstudent_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    search=request.POST['textfield']
    sobj=Student.objects.filter(name__icontains=search)
    return render(request,'authority/authority_view_student.html',{'data':sobj})

def viewcheckin(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    obj=checkin_chechout.objects.all()

    return render(request,'authority/view_checkin/checkout.html',{'data':obj})

def viewattendance(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    obj=Attendance.objects.all()

    return render(request,'authority/View Attendence.html',{'data':obj})


def viewattendance_post(request):

    f=request.POST['textfield']
    t=request.POST['textfield2']
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    obj=Attendance.objects.filter(date__range=[f,t])

    return render(request,'authority/View Attendence.html',{'data':obj})



def viewcheckin_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    search=request.POST['textfield']
    obj=checkin_chechout.objects.filter(STUDENT__name__icontains=search)
    return render(request,'authority/view_checkin/checkout.html',{'data':obj})

def viewalert(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    vaoj=Alert.objects.all()
    return render(request,'authority/violence_alert.html',{'data':vaoj})

def viewalert_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    search=request.POST['textfield']
    vaoj=Alert.objects.filter(title__icontains=search)
    return render(request,'authority/violence_alert.html',{'data':vaoj})


def authoritytakeaction(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    var=Student.objects.all()
    var1=Alert.objects.all()
    return render(request,'authority/taking_actionagainstthestudent.html',{'data':var,'data1':var1})

def post_authoritytakeaction(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    action=request.POST['textfield']
    name=request.POST['textfield3']
    alert=request.POST['textfield4']
    from datetime import datetime
    date=datetime.now().date().today()
    obj=Action()
    obj.action=action
    obj.date=date
    obj.STUDENT_id=name
    obj.ALERT_id=alert
    obj.save()
    return HttpResponse(  '''<script>alert('alert take action');window.location='/myapp/authoritytakeaction/'</script>''')
def authorityviewfeedback(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    febj=Feedback.objects.all()
    return render(request,'authority/View feedback.html',{'data':febj})

def authorityviewfeedback_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    febj = Feedback.objects.filter(date__range=[fromdate,todate])
    return render(request, 'authority/View feedback.html', {'data': febj})

def authoritysendnotification(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    return render(request,'authority/send_notification.html')
def authoritysendnotification_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    notification=request.POST['textfield']
    from datetime import datetime
    date = datetime.now().date().today()
    obj=Notification()
    obj.notification=notification
    obj.date=date
    obj.AUTHORITY=Authority.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse(  '''<script>alert('notification added');window.location='/myapp/authoritysendnotification/'</script>''')

def authoritysendmessage(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    return render(request,'authority/sendmessage.html')

def authoritysendmessage_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    msg=request.POST['textfield']
    from datetime import datetime
    date= datetime.now().date().today()
    obj=message()
    obj.message=msg
    obj.date=date
    obj.AUTHORITY=Authority.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse(  '''<script>alert('message added');window.location='/myapp/authoritysendmessage/'</script>''')


def auth_view_parent(request):
    res=Student.objects.all()
    l=[]
    for i in res:
        print(i.parent_e_mail_id)
        if Login.objects.filter(username=i.parent_e_mail_id).exists():
            le=Login.objects.get(username=i.parent_e_mail_id)
            if i.parent_e_mail_id == le.username:
                l.append({"lid":Login.objects.get(username=i.parent_e_mail_id),"parent_name":i.parent_name,"parent_number":i.parent_number,"parent_e_mail_id":i.parent_e_mail_id,"image":i.image,"name":i.name,"place":i.place,"city":i.city,"district":i.district,"state":i.state,"pincode":i.pincode,"phone_number":i.phone_number,"e_mail":i.e_mail,"course":i.COURSE.course})
                return render(request,"authority/authority_view_parent.html",{'data':l})
            else:
                return render(request,"authority/authority_view_parent.html",{'data':l})
        else:
            return render(request, "authority/authority_view_parent.html", {'data': l})

def authorityViewViolence(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    comj = Violence.objects.all()
    return render(request, 'Authority/view Violence.html', {'data': comj})

def authorityViewViolence_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    comj = Violence.objects.filter(date__range=[fromdate, todate])
    return render(request, 'Authority/View VIOLENCE.html', {'data': comj})

def authorityViewIncludedFace(request, id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    comj = violence_included_face.objects.filter(VIOLENCE_id=id)
    return render(request, 'Authority/View VIOLENCE INCLUDED FACE.html', {'data': comj,"id":id})

def authoritytest(request, id):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    comj = Student.objects.all()
    return render(request, 'Authority/Add Students Included.html', {'data': comj,"id":id})

def authorityViewIncludedFace_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    name = request.POST['textfield']
    id= request.POST['id']
    comj = violence_included_face.objects.filter(STUDENT__name__icontains=name,VIOLENCE_id=id)
    return render(request, 'Authority/View VIOLENCE INCLUDED FACE.html', {'data': comj,"id":id})

def searchStudent(request):
    name=request.GET['name']
    comj =Student.objects.filter(name__icontains=name).values('id', 'name', 'image')
    l = list(comj)
    return JsonResponse(l, safe=False)

    # return render(request, 'Authority/Add Students Included.html', {'data': comj,"id":id})
    # return render(request, 'Authority/View VIOLENCE INCLUDED FACE.html', {'data': comj,"id":id})


def addStudentTOIncludedFace_post(request, id,stdid):
    if violence_included_face.objects.filter(VIOLENCE_id=id, STUDENT_id=stdid).exists():
        return HttpResponse(
            "<script>alert('Student already exists in included faces');window.location='/myapp/authorityViewIncludedFace/"+id+"#abc'</script>")
    comj = violence_included_face()
    comj.STUDENT_id=stdid
    comj.VIOLENCE_id=id
    comj.save()
    return HttpResponse("<script>alert('Student added into included faces');window.location='/myapp/authorityViewIncludedFace/"+id+"#abc'</script>")


########################3

def and_login(request):
    uname = request.POST['username']
    password = request.POST['password']

    lobj = Login.objects.filter(username=uname, password=password)

    if lobj.exists():
        lobjj = Login.objects.get(username=uname, password=password)
        if lobjj.type == 'student':
            lid = lobjj.id
            return JsonResponse({'status': 'ok', 'lid': str(lid),'type':lobjj.type})

        elif lobjj.type == 'parent':
            lid = lobjj.id
            return JsonResponse({'status': 'ok', 'lid': str(lid),'type':lobjj.type})
    else:
        return JsonResponse({'status': 'no'})


def and_viewprofile(request):
    lid=request.POST['lid']
    var=Student.objects.get(LOGIN_id=lid)
    print(var)
    return  JsonResponse({'status':'ok','name':var.name,'email':var.e_mail,'phone_number':var.phone_number,'image':var.image,'gender':var.gender,'place':var.place,"city":var.city,'district':var.district,'state':var.state,'pincode':var.pincode,'parentname':var.parent_name,'parentnumber':var.parent_number,'parentemail':var.parent_e_mail_id,'dob':var.dob,'course':var.COURSE.course})


def and_changepassword(request):
    currentpassword = request.POST['currentpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    lid=request.POST['lid']

    log = Login.objects.get(id=lid, password=currentpassword)
    if newpassword == confirmpassword:
        log1 = Login.objects.filter(id=lid).update(password=confirmpassword)

        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'ok'})


def and_sendfeedback(request):
    lid=request.POST['lid']
    feedback=request.POST ['feedback']
    var=Feedback()
    var.feedback=feedback
    from datetime import datetime
    var.date=datetime.now().strftime('%Y-%m-%d')
    std=Student.objects.get(LOGIN=lid)
    var.LOGIN_id=std.id
    var.save()

    return JsonResponse({'status': 'ok'})


def view_attendance(request):
    lid=request.POST['lid']
    var=Attendance.objects.filter(STUDENT__LOGIN_id=lid)
    l=[]
    for i in var:
        l.append({'id':i.id,'date':i.date,'checkin_checkout':i.checkin_checkout,'time':i.time})
    return JsonResponse({'status':'ok','data':l})


def parent_and_changepassword(request):
    currentpassword = request.POST['currentpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    lid=request.POST['lid']

    log = Login.objects.get(id=lid, password=currentpassword)
    if newpassword == confirmpassword:
        log1 = Login.objects.filter(id=lid).update(password=confirmpassword)

        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'ok'})



def parent_view_authority(request):
    var=Authority.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'name':i. name,'phone_number':i.phone_number,'gender':i.gendre ,'dob':i.age,'image':i.image,'email':i.e_mail,'LOGIN_id':i.LOGIN.id})
    return JsonResponse({'status':'ok','data':l})


def parent_view_attendance(request):
    sid=request.POST['sid']

    var=Attendance.objects.filter(STUDENT_id=sid)
    l=[]
    for i in var:
        l.append({'id':i.id,'date':i.date,'checkin_checkout':i.checkin_checkout,'time':i.time})
    return JsonResponse({'status':'ok','data':l})


def and_sendcomplaint(request):
    lid=request.POST['lid']
    complaint=request.POST ['complaint']
    var=Complaint()
    var.complaint=complaint
    var.reply='pending'
    var.status='pending'
    from datetime import datetime
    var.date=datetime.now().strftime('%Y-%m-%d')
    # std=Student.objects.get(parent_e_mail_id=Login.objects.get(id=lid).username)
    var.PARENT_id=lid
    var.save()

    return JsonResponse({'status': 'ok'})


def parent_view_student(request):
    lid=request.POST['lid']
    res=Student.objects.filter(parent_e_mail_id=Login.objects.get(id=lid).username)
    l = []
    for var in res:
        l.append({'id': var.id,'name':var.name,'email':var.e_mail,'phone_number':var.phone_number,'image':var.image,'gender':var.gender,'place':var.place,"city":var.city,'district':var.district,'state':var.state,'pincode':var.pincode,'parentname':var.parent_name,'parentnumber':var.parent_number,'parentemail':var.parent_e_mail_id,'dob':var.dob,'course':var.COURSE.course })

    return JsonResponse({'status': 'ok', 'data': l})


def parent_view_replay(request):
    lid=request.POST['lid']
    print(Login.objects.get(id=lid).username)
    var=Complaint.objects.filter(PARENT_id=lid)
    # var=Complaint.objects.filter(PARENT__parent_e_mail_id=Login.objects.get(id=lid).username)
    l = []
    for i in var:
        l.append({'id': i.id,'date':i.date,'complaint':i.complaint,'reply':i.reply,'status':i.status})
    print(l)
    return JsonResponse({'status': 'ok', 'data': l})


def and_par_sendfeedback(request):
    lid=request.POST['lid']
    feedback=request.POST ['feedback']
    var=Feedback()
    var.feedback=feedback
    from datetime import datetime
    var.date=datetime.now().strftime('%Y-%m-%d')
    std=Student.objects.get(parent_e_mail_id=Login.objects.get(id=lid).username)
    var.LOGIN_id=std.id
    var.save()
    return JsonResponse({'status': 'ok'})

###############################

def chat1(request, id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    # qry = Student.objects.get(LOGIN=cid)

    return render(request, "authority/Chat.html", {'photo': "/static/home/image/bg.jpg", 'name': "parent", 'toid': cid})

def chat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    # qry = Student.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid)).order_by('id')
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.massege, "to": i.TOID_id, "date": i.date, "from": i.FROMID_id})

    return JsonResponse({'photo':'/static/home/web/images/bg.jpg', "data": l, 'name': "parent", 'toid': request.session["userid"]})

def chat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.massege = message
    chatobt.TOID_id = toid
    chatobt.FROMID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})

# flutter

def user_sendchat(request):
    FROM_id=request.POST['from_id']
    TOID_id=request.POST['to_id']
    msg=request.POST['massege']

    from  datetime import datetime
    c=Chat()
    c.FROMID_id=FROM_id
    c.TOID_id=TOID_id
    c.massege=msg
    c.date=datetime.now()
    c.save()
    return JsonResponse({'status':"ok"})


def user_viewchat(request):
    fromid = request.POST["from_id"]
    toid = request.POST["to_id"]
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid)).order_by('id')
    l = []

    for i in res:
        l.append({"id": i.id, "msg": i.massege, "from": i.FROMID_id, "date": i.date, "to": i.TOID_id})

    return JsonResponse({"status":"ok",'data':l})

def parent_view_notification(request):
    lid=request.POST['lid']
    var=Notification.objects.all()
    l = []
    for i in var:
        l.append({'id': i.id,'date':i.date,'notification':i.notification})
    print(l)
    return JsonResponse({'status': 'ok', 'data': l})


#
#
#
# Cam
def test(request):
    import cv2
    import face_recognition
    res=Student.objects.all()

    knownimage = []
    knownids = []

    for i in res:
        s = i.image
        s = s.replace("/", "\\")
        pth = "C:\\Users\\shahana kp\\PycharmProjects\\college_violence" + s

        picture_of_me = face_recognition.load_image_file(pth)
        # print(pth)
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
        knownimage.append(my_face_encoding)
        knownids.append(i.id)

    vid = cv2.VideoCapture(0)

    # firsthour = (8.50, 9.30)
    # lasthour = (13.30, 15.15)

    while (True):

        ret, frame = vid.read()

        cv2.imwrite(r"C:\Users\shahana kp\PycharmProjects\college_violence\media\tests\a.jpg", frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        picture_of_others = face_recognition.load_image_file(
            r"C:\Users\shahana kp\PycharmProjects\college_violence\media\tests\a.jpg")
        others_face_encoding = face_recognition.face_encodings(picture_of_others)

        totface = len(others_face_encoding)

        # from datetime import datetime

        # curh = float(str(datetime.now().time().hour) + "." + str(datetime.now().strftime('%M')))

        # print(curh, 'curh', firsthour[0], 'fh', firsthour[1], 'lh')
        # period = 0
        # if firsthour[0] < curh < firsthour[1]:
            # print('first')
            # period = 1
        # elif lasthour[0] < curh < lasthour[1]:
            # print('last')
            # period = 5
        # print(period, 'period')

        for i in range(0, totface):
            res = face_recognition.compare_faces(knownimage, others_face_encoding[i], tolerance=0.5)
            print(res)
            l = 0
            for j in res:
                if j == True:

                    import datetime
                    if not Attendance.objects.filter(STUDENT_id=knownids[l], date=datetime.date.today(), checkin_checkout='Check In').exists():
                        cv2.imwrite(r"C:\Users\shahana kp\PycharmProjects\college_violence\media\attendance\\"+str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))+".jpg", frame)
                        qry = Attendance()
                        qry.STUDENT_id = knownids[l]
                        qry.date = datetime.date.today()
                        # if period == 1:
                        qry.checkin_checkout = 'Check In'
                        # if period == 5:
                        #     qry.checkin_checkout = 'Check Out'
                        qry.time = datetime.datetime.now().strftime('%H:%M:%S')
                        qry.photo='/media/attendance/'+str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))+".jpg"
                        qry.save()
                    elif Attendance.objects.filter(STUDENT_id=knownids[l], date=datetime.date.today(), checkin_checkout='Check In').exists():
                        att = Attendance.objects.filter(STUDENT_id=knownids[l], date=datetime.date.today())
                        if len(att)==2:
                            break
                        # if att.checkin_checkout=='Check In':
                        # att = Attendance.objects.get(STUDENT_id=knownids[l], date=datetime.date.today())
                        dt = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))
                        cv2.imwrite(r"C:\Users\shahana kp\PycharmProjects\college_violence\media\attendance\\"+dt+".jpg", frame)
                        qry = Attendance()
                        qry.STUDENT_id = knownids[l]
                        qry.date = datetime.date.today()
                        # if period == 1:
                        # qry.checkin_checkout = 'Check In'
                        # if period == 5:
                        qry.checkin_checkout = 'Check Out'
                        qry.photo='/media/attendance/'+dt+".jpg"
                        qry.time = datetime.datetime.now().strftime('%H:%M:%S')
                        qry.save()

                l = l + 1
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return redirect('/myapp/login/')


def lkindex(request):
    return render(request,"Admin/index.html")


def auth_viewnotification(request):

    n=Notification.objects.all()
    return  render(request,"authority/View notification.html",{'data':n})



def auth_viewnotification_post(request):
    f=request.POST["f"]
    t=request.POST["t"]

    n=Notification.objects.filter(date__range=[f,t])
    return  render(request,"authority/View notification.html",{'data':n})


def auth_deletenotification(request,id):
    Notification.objects.filter(id=id).delete()

    return HttpResponse("<script>alert('Deleted successfully');window.location='/myapp/auth_viewnotification'</script>")

def auth_violence_subimages(request,vid):

    n=Incident_sub_images.objects.filter(VIOLENCE_id= vid)
    return  render(request,"authority/Viewviolenceimages.html",{'data':n})
def auth_assign_violence_to_student(request,vid):

    request.session['vid']=vid

    s=Student.objects.all()
    c=Course.objects.all()

    return render(request,"authority/view student_asfn.html",{'vid':vid ,'s':s,'c':c})



def assgn(request,id):
    vid= request.session['vid']
    uid=id

    v=violence_included_face()
    v.VIOLENCE_id=vid
    v.STUDENT_id=uid

    return HttpResponse("<script>alert('Added Successfully');window.location='/myapp/authorityViewViolence/'</script>")



def auth_assign_violence_to_studentpost(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>window.location='/myapp/login/'</script>''')
    if request.POST["button"]=="Go":

        crs= request.POST["select"]
        sem= request.POST["semseter"]

        sobj = Student.objects.filter(COURSE_id=crs, semester=sem)
        c = Course.objects.all()
        return render(request, "authority/view student_asfn.html", { 's': sobj, 'c': c})
    else:
        search=request.POST['textfield']
        sobj=Student.objects.filter(name__icontains=search)
        c = Course.objects.all()
        return render(request, "authority/view student_asfn.html", {'s': sobj, 'c': c})

