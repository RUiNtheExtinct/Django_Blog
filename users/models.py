from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        w, h = img.width, img.height
        if w > h:
            lr = (w - h) // 2
            ud = 0
        else:
            ud = (h - w) // 2
            lr = 0
        img1 = img.crop((lr, ud, w - lr, h - ud))
        if img1.height > 300 or img1.width > 300:
            output_size = (300, 300)
            img1.thumbnail(output_size)
            img1.save(self.image.path)
