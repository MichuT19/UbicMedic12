from django.middleware.csrf import CsrfViewMiddleware

class CustomCsrfViewMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        setattr(request, '_dont_enforce_csrf_checks', True)
        return None