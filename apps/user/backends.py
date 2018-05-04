# coding=utf-8
from apps.user.models import User

class UsernumBackend(object):
    def authenticate(self, usernum,password):
        # 要注意登录表单中用户输入的用户名或者邮箱的 field 名均为 username
        # usernum = credentials.get('usernum', credentials.get('usernum'))
        usernum = usernum

        try:
            user = User.objects.get(username=usernum)

        except User.DoesNotExist:
            pass
        else:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        """
        该方法是必须的
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None