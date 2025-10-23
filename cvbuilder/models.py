from django.db import models

class CV(models.Model):
    # Personal
    full_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)

    # Education
    institution = models.CharField(max_length=200, blank=True)
    degree = models.CharField(max_length=200, blank=True)
    passing_year = models.CharField(max_length=20, blank=True)

    # Experience
    company = models.CharField(max_length=200, blank=True)
    role = models.CharField(max_length=200, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    # Skills
    skills = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


