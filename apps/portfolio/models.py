from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)  # masalan: Backend Developer
    about = models.TextField()  # qisqacha bio
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(default=0)  # foizda: 80%

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class Experience(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='experiences')
    company = models.CharField(max_length=128)
    role = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.company} - {self.role}"


class Education(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='educations')
    institution = models.CharField(max_length=128)
    degree = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.institution} - {self.degree}"


class Project(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=128)
    description = models.TextField()
    technologies = models.CharField(max_length=256)  # masalan: Django, DRF, PostgreSQL
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
