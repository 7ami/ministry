from django.contrib.auth.backends import ModelBackend
from . import models


class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        return self.downcast_usertype(super().authenticate(request, username, password, **kwargs))

    def get_user(self, user_id):
        return self.downcast_usertype(super().get_user(user_id))

    def downcast_usertype(self, user):
        if user:
            try:
                customUser = models.AdminUser.objects.get(pk=user.pk)
                return customUser
            except models.AdminUser.DoesNotExist:
                pass

            try:
                customUser = models.OrganizationUser.objects.get(pk=user.pk)
                return customUser
            except models.OrganizationUser.DoesNotExist:
                pass

            try:
                customUser = models.VolunteerUser.objects.get(pk=user.pk)
                return customUser
            except models.VolunteerUser.DoesNotExist:
                pass

        return user