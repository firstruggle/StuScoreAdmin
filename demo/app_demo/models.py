from django.db import models

# Create your models here.
class adminer(models.Model):
    adminame = models.CharField(max_length=128, null=True, db_column='admin_name')
    password = models.CharField(max_length=128, null=True, db_column='admin_password')

    class Meta:
        db_table = 'adminer'
        verbose_name = '管理员账号'
        verbose_name_plural = '管理员账号'

class stuinfo(models.Model):
    stuid = models.CharField(max_length=128, null=True, db_column='学号')
    stuname = models.CharField(max_length=128, null=True, db_column='姓名')
    gender = models.CharField(max_length=128, null=True, db_column='性别')
    profession = models.CharField(max_length=128, null=True, db_column='专业')
    classid = models.IntegerField(null=True, db_column='班号')
    password = models.CharField(max_length=128, null=True, db_column='密码')

    class Meta:
        db_table = 'stuinfo'
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'

class teacherinfo(models.Model):
    tid = models.CharField(max_length=128, null=True, db_column='教工号')
    tname = models.CharField(max_length=128, null=True, db_column='姓名')
    gender = models.CharField(max_length=128, null=True, db_column='性别')
    profession = models.CharField(max_length=128, null=True, db_column='专业')
    courseid = models.CharField(max_length=128, null=True, db_column='所授课程')
    password = models.CharField(max_length=128, null=True, db_column='密码')

    class Meta:
        db_table = 'teacherinfo'
        verbose_name = '教师信息'
        verbose_name_plural = '教师信息'

class courseinfo(models.Model):
    cid = models.CharField(max_length=128, null=True, db_column='课程号')
    cname = models.CharField(max_length=128, null=True, db_column='课程名')
    ctime = models.IntegerField(null=True, db_column='学时')
    cscore = models.FloatField(null=True, db_column='学分')
    tname = models.CharField(max_length=128, null=True, db_column='授课教师')

    class Meta:
        db_table = 'courseinfo'
        verbose_name = '课程信息'
        verbose_name_plural = '课程信息'

class scoreinfo(models.Model):
    cid = models.CharField(max_length=128, null=True, db_column='课程号')
    cname = models.CharField(max_length=128, null=True, db_column='课程名')
    tname = models.CharField(max_length=128, null=True, db_column='授课教师')
    stuid = models.CharField(max_length=128, null=True, db_column='学生学号')
    classid = models.CharField(max_length=128, null=True, db_column='学生班号')
    score = models.IntegerField(null=True, db_column='学生成绩')

    class Meta:
        db_table = 'scoreinfo'
        verbose_name = '得分信息'
        verbose_name_plural = '得分信息'