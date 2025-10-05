# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Student(models.Model):

    #__Student_FIELDS__
    full_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)

    #__Student_FIELDS__END

    class Meta:
        verbose_name        = _("Student")
        verbose_name_plural = _("Student")


class Teacher(models.Model):

    #__Teacher_FIELDS__
    full_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)

    #__Teacher_FIELDS__END

    class Meta:
        verbose_name        = _("Teacher")
        verbose_name_plural = _("Teacher")


class Level(models.Model):

    #__Level_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Level_FIELDS__END

    class Meta:
        verbose_name        = _("Level")
        verbose_name_plural = _("Level")


class Subject(models.Model):

    #__Subject_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Subject_FIELDS__END

    class Meta:
        verbose_name        = _("Subject")
        verbose_name_plural = _("Subject")


class Group(models.Model):

    #__Group_FIELDS__
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    #__Group_FIELDS__END

    class Meta:
        verbose_name        = _("Group")
        verbose_name_plural = _("Group")



#__MODELS__END
