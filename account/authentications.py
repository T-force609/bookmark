from django.contrib.auth.models import User

class EmailAuthBackend(object):
    def authenticate(self, request, usernam=None, password=None):
        try:
            user = User.objects.get(email=usernam)
            if user.check_password(password):
                return user
            return None
        except user.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        try:
            User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        