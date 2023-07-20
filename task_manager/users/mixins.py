from django.contrib import messages
from django.shortcuts import redirect

class UserPermissionMixin:
    permission_message = ''
    permission_url = ''

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object != request.user:
            messages.error(request, self.permission_message)
            return redirect(self.permission_url)
        return super().dispatch(request, *args, **kwargs)
