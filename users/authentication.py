from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_modal = get_user_model()
        try:
            user = user_modal.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (user_modal.DoesNotExist, user_modal.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        user_modal = get_user_model()
        try:
            return user_modal.objects.get(pk=user_id)
        except user_modal.DoesNotExist:
            return None
