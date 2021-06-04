from django.http.response import JsonResponse


class TracerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.name = type(self).__name__
        print(f"{self.name} is initialized")

    def __call__(self, request):

        print(f"{self.name}: before", request)
        response = self.get_response(request)
        if isinstance(response, JsonResponse):
            response_value = response.getvalue()
        else:
            response_value = response
        print(f"{self.name}: after", response_value)

        return response
