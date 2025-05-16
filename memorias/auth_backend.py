from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class PhoneNumberBackend(BaseBackend):
    def authenticate(self, request, phone_number=None, pin=None):
        if phone_number is None or pin is None:
            return None

        try:
            user = CustomUser.objects.get(phone_number=phone_number)
            if user.check_password(pin):  # usa check_password para validar PIN
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None