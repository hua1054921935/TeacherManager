from django.contrib.auth.decorators import login_required
class LoginRequirdMixin(object):
    @classmethod
    def as_view(cls,**inikwargs):

        view=super(LoginRequirdMixin,cls).as_view(**inikwargs)
        return login_required(view)