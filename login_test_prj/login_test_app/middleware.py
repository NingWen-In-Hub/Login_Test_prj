from django.http import HttpResponseForbidden
from django.template import Context
from django.template.loader import get_template
from login_test_app.exceptions import Http403

class ExceptionMiddleware(object):

    def _get_forbidden(self):
        t = get_template("403.html")
        context = Context()
        return HttpResponseForbidden(t.render(context))

    def process_exception(self, request, e):
        if isinstance(e, Http403):
            return self._get_forbidden()
        else:
            return None
