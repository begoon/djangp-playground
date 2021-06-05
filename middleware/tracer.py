class TracerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.name = type(self).__name__
        print(f"{self.name} is initialized")

    def __call__(self, request):

        print(f"{self.name}: before", request)
        response = self.get_response(request)
        print(f"{self.name}: after", response)

        return response
