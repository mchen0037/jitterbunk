from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# class User(models.Model):
#     # the user's name
#     user = models.CharField(max_length=100)
#     # ?? TODO: how does this work?
#     photo = models.ImageField(upload_to=user_directory_path)
#
#     def __str__(self):
#         return self.user

class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    time = models.TimeField('time published')

    def __str__(self):
        return "%s - %s" % (self.from_user.first_name, self.to_user.first_name)
