from django.db import models
from django.contrib.auth.models import User

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

class Bunk(models.Model):
    # So if Andy deletes his account, then all of Mighty's bunks to Andy would also
    # be deleted. MSet from_user to null instead.
    from_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='+')
    to_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='+')
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.from_user.first_name, self.to_user.first_name)
