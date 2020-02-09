from common import settings
from Student.models import Logger
from time import time


class LoggerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info
        method = request.method
        start_time = time()
        response = self.get_response(request)
        time_delta = time() - start_time
        user_id = request.user.id

        if path.startswith('/admin/'):
            logger = Logger.objects.create(
                path=path,
                method=settings.MCR[method],
                time_delta=time_delta,
                user_id=user_id,
            )

            logger.save()

        return response