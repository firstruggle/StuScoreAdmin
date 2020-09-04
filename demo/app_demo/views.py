import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app_demo.models import adminer, stuinfo, teacherinfo, courseinfo, scoreinfo

Admin_name = ""
Pro_name = ""

def login(request):
    return render(request, "index.html")


def login1(request):
    return render(request, "index1.html")


def login2(request):
    return render(request, "index2.html")


def admin(request):
    judge = request.POST['hid']
    global Admin_name
    if judge == 'createstu':
        id = request.POST['a']
        students = stuinfo.objects.filter(stuid=id)
        student = stuinfo()
        if len(students) != 0:
            student = students[0]
        student.stuid = request.POST['a']
        student.stuname = request.POST['b']
        student.gender = request.POST['c']
        student.profession = request.POST['d']
        student.classid = request.POST['e']
        student.password = request.POST['f']
        student.save()
    elif judge == 'createteacher':
        id = request.POST['a']
        teachers = teacherinfo.objects.filter(tid=id)
        t = teacherinfo()
        if len(teachers) != 0:
            t = teachers[0]
        t.tid = request.POST['a']
        t.tname = request.POST['b']
        t.gender = request.POST['c']
        t.profession = request.POST['d']
        t.courseid = request.POST['e']
        t.password = request.POST['f']
        t.save()
    elif judge == 'createcourse':
        id = request.POST['a']
        courses = courseinfo.objects.filter(cid=id)
        c = courseinfo()
        if len(courses) != 0:
            c = courses[0]
        c.cid = request.POST['a']
        c.cname = request.POST['b']
        c.ctime = request.POST['c']
        c.cscore = request.POST['d']
        c.tname = request.POST['e']
        c.save()
    elif judge == 'delstu':
        id = request.POST['id']
        stuinfo.objects.filter(stuid=id).delete()
    elif judge == 'delteacher':
        id = request.POST['id']
        teacherinfo.objects.filter(tid=id).delete()
    elif judge == 'delcourse':
        id = request.POST['id']
        courseinfo.objects.filter(cid=id).delete()

    if Admin_name == "":
        Admin_name = request.POST['username']
    context = {'adname': Admin_name}
    return render(request, 'admin.html', context)

def pro(request):
    global Pro_name
    judge = request.POST['hid']
    context = {}
    if judge == 'index1':
        Pro_name = request.POST['username']
        id = request.POST['password']

        nts = teacherinfo.objects.filter(tid=Pro_name)
        if len(nts) == 0:
            return HttpResponse('无此用户')
        nt = nts[0]
        rid = nt.password
        courses = []
        for i in nts:
            courses.append(i.courseid)
        if id != rid:
            return HttpResponse('用户密码错误')
        context = {'adname': Pro_name,
                   'a': nt.tid,
                   'b': nt.tname,
                   'c': nt.gender,
                   'd': nt.profession,
                   'e': nt.courseid,
                   'f': json.dumps(courses)}
    elif judge == 'pro':
        courseid = request.POST['cid']
        stuid = request.POST['stu']
        stuscore = request.POST['score']
        ss = scoreinfo.objects.filter(cid=courseid, stuid=stuid)
        s = scoreinfo()
        if len(ss) != 0:
            s = ss[0]
        s.cid = courseid
        courses = courseinfo.objects.filter(cid=courseid)
        if len(courses) == 0:
            return HttpResponse('此课还未录入')
        tmpcourse = courses[0]
        s.cname = tmpcourse.cname
        s.tname = tmpcourse.tname
        tmpstu = stuinfo.objects.filter(stuid=stuid)[0]
        s.stuid = tmpstu.stuid
        s.classid = tmpstu.classid
        s.score = stuscore
        s.save()
        context = {
            'adname': Pro_name,
            'a': request.POST['a'],
            'b': request.POST['b'],
            'c': request.POST['c'],
            'd': request.POST['d'],
            'e': request.POST['e'],
            'f': request.POST['f']
        }
    return render(request, 'professor.html', context)

def allscore(request):
    cid = request.POST['e']
    cs = scoreinfo.objects.filter(cid=cid);
    if len(cs) == 0:
        return HttpResponse('无人选修此课')
    t = []
    s = []
    for i in cs:
        t.append(i.stuid)
        s.append(i.score)
    context = {'t': json.dumps(t),
               's': json.dumps(s)}
    return render(request, 'allscore.html', context)

def stu(request):
    stuid = request.POST['username']
    password = request.POST['password']
    stus = stuinfo.objects.filter(stuid=stuid)
    if len(stus) == 0:
        return HttpResponse('无此用户')
    stu = stus[0]
    if password != stu.password:
        return HttpResponse('用户密码错误')
    scores = scoreinfo.objects.filter(stuid=stuid)
    s = []
    for i in scores:
        s.append({i.cname: i.score})
    context = {
        'adname': stuid,
        'a': stu.stuid,
        'b': stu.stuname,
        'c': stu.gender,
        'd': stu.profession,
        'e': stu.classid,
        'f': s
    }
    return render(request, "student.html", context)

def createstu(request):
    global Admin_name
    context = {'adname': Admin_name}
    return render(request, "createstu.html", context)


def createteacher(request):
    global Admin_name
    context = {'adname': Admin_name}
    return render(request, "createteacher.html", context)

def createcourse(request):
    global Admin_name
    context = {'adname': Admin_name}
    return render(request, "createcourse.html", context)

def retrievestu(request):
    global Admin_name
    id = request.POST['id']
    students = stuinfo.objects.filter(stuid=id)
    if len(students) == 0:
        context = {'adname': Admin_name,
                   'a': '查无此人',
                   'b': '查无此人',
                   'c': '查无此人',
                   'd': '查无此人',
                   'e': '查无此人',
                   'f': '查无此人'
                   }
    else:
        stu = students[0]
        context = {'adname': Admin_name,
                   'a': stu.stuid,
                   'b': stu.stuname,
                   'c': stu.gender,
                   'd': stu.profession,
                   'e': stu.classid,
                   'f': stu.password}
    return render(request, "retrievestu.html", context)

def retrieveteacher(request):
    global Admin_name
    id = request.POST['id']
    teachers = teacherinfo.objects.filter(tid=id)
    if len(teachers) == 0:
        context = {'adname': Admin_name,
                   'a': '查无此人',
                   'b': '查无此人',
                   'c': '查无此人',
                   'd': '查无此人',
                   'e': '查无此人',
                   'f': '查无此人'
                   }
    else:
        t = teachers[0]
        tt = []
        for i in teachers:
            tt.append(i.courseid)
        context = {'adname': Admin_name,
                   'a': t.tid,
                   'b': t.tname,
                   'c': t.gender,
                   'd': t.profession,
                   'e': tt,
                   'f': t.password}
    return render(request, "retrieveteacher.html", context)

def retrievecourse(request):
    global Admin_name
    id = request.POST['id']
    courses = courseinfo.objects.filter(cid=id)
    if len(courses) == 0:
        context = {'adname': Admin_name,
                   'a': '查无此课',
                   'b': '查无此课',
                   'c': '查无此课',
                   'd': '查无此课',
                   'e': '查无此课'
                   }
    else:
        c = courses[0]
        context = {'adname': Admin_name,
                   'a': c.cid,
                   'b': c.cname,
                   'c': c.ctime,
                   'd': c.cscore,
                   'e': c.tname}
    return render(request, "retrievecourse.html", context)

def updatestu(request):
    global Admin_name
    id = request.POST['id']
    students = stuinfo.objects.filter(stuid=id)
    stu = students[0]
    context = {'adname': Admin_name,
               'a': stu.stuid,
               'b': stu.stuname,
               'c': stu.gender,
               'd': stu.profession,
               'e': stu.classid,
               'f': stu.password}
    return render(request, 'updatestu.html', context)

def updateteacher(request):
    global Admin_name
    id = request.POST['id']
    teachers = teacherinfo.objects.filter(tid=id)
    t = teachers[0]
    context = {'adname': Admin_name,
               'a': t.tid,
               'b': t.tname,
               'c': t.gender,
               'd': t.profession,
               'e': t.courseid,
               'f': t.password}
    return render(request, 'updateteacher.html', context)

def updatecourse(request):
    global Admin_name
    id = request.POST['id']
    courses = courseinfo.objects.filter(cid=id)
    c = courses[0]
    context = {'adname': Admin_name,
               'a': c.cid,
               'b': c.cname,
               'c': c.ctime,
               'd': c.cscore,
               'e': c.tname}
    return render(request, 'updatecourse.html', context)

def stat(request):
    id = request.POST['id']
    info = scoreinfo.objects.filter(cid=id)
    if len(info) == 0:
        return HttpResponse('无人选修此课')
    num = [0, 0, 0, 0, 0]
    for i in info:
        sc = i.score
        if sc < 60:
            num[0] += 1
        elif sc < 70:
            num[1] += 1
        elif sc < 80:
            num[2] += 1
        elif sc < 90:
            num[3] += 1
        else:
            num[4] += 1
    sum = 0
    for i in range(5):
        sum += num[i]
    fl = num.copy()
    for i in range(5):
        fl[i] /= sum
    global Admin_name
    Admin_name = request.POST['Ad']
    context = {
        'adname': Admin_name,
        'arraynum': json.dumps(num),
        'arrayfl': json.dumps(fl)
    }
    return render(request, 'statistic.html', context)

def test(request):
    context = {'adname': Admin_name}
    return render(request, 'createstu.html', context)
