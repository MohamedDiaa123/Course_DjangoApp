from django.db import models

class Teacher(models.Model):
    
    teacher_id=models.CharField('Teacher ID',max_length=20,null=True)
    teacher_name=models.CharField('Teacher Name',max_length=120)
    teacher_email=models.EmailField('Email Address')
    
    def __str__(self):
        return self.teacher_id


class Student(models.Model):
    
    student_id=models.CharField('Student ID',max_length=20,null=True)
    student_name=models.CharField('Student Name',max_length=120)
    
    def __str__(self):
        return self.student_name


class Course(models.Model):
    
    course_id=models.CharField('Course ID',max_length=20,null=True)
    course_name=models.CharField('Course Name',max_length=120)
    teacher_id=models.ForeignKey(Teacher,blank=True,null=True,on_delete=models.CASCADE)
    student=models.ManyToManyField(Student,blank=True)
    
    def __str__(self):
        return self.course_name
