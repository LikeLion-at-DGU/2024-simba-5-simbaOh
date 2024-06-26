from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return self.name

class Mentor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mentor_company = models.CharField(max_length=50)
    mentor_dept = models.CharField(max_length=50)
    mentor_work = models.CharField(max_length=50)
    
    mentor_summary = models.CharField(max_length=50)
    mentor_info = models.TextField(max_length=300)
    mentor_career = models.CharField(max_length=50)

    mentor_certificate = models.CharField(max_length=100, null=True, blank=True)
    mentor_id_card = models.ImageField(upload_to="mentor_1/")
    mentor_name_card = models.ImageField(upload_to="mentor_2/")

    # follow = models.ManyToManyField(User, related_name='follow', blank=True)
    # follow_count = models.PositiveIntegerField(default=0)
    
    mentor_at = models.DateTimeField()
    followers = models.ManyToManyField(User, related_name='mentor_followings', blank=True)

    categories = models.ManyToManyField(Category, related_name='mentors', blank=True)
    mentor_ship = models.ManyToManyField(User, related_name='menti_ship', symmetrical=False, blank=True)
    def __str__(self):
        return self.user

class Menti(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    summary = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    state = models.CharField(max_length=30, null=True, blank=True)
    mentoring_at = models.DateField(blank=True, null=True)

class Relation_mentor(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    menti = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.menti
