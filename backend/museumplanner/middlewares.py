from urllib.parse import urlparse

from django.http import HttpRequest, HttpResponse


def cors_development_middleware(get_response):
    """
    A middleware that sets CORS response headers for local development
    """

    def middleware(request: HttpRequest):
        if request.method == "OPTIONS":
            response = HttpResponse()
        else:
            response = get_response(request)

        if "Origin" in request.headers:
            origin = urlparse(request.headers["Origin"])
            if origin.hostname.endswith("localhost") or origin.hostname == "host.docker.internal":
                response.headers["Access-Control-Allow-Origin"] = f"{origin.scheme}://{origin.hostname}:{origin.port}"
                response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
                response.headers["Access-Control-Allow-Headers"] = (
                    "Content-Type, Authorization, X-Requested-With, X-CSRFToken"
                )
                response.headers["Access-Control-Allow-Credentials"] = "true"
                # comma-separated list of headers that is accessible to the frontend code
                # response.headers["Access-Control-Expose-Headers"] = ""
                response.headers["Vary"] = "Origin"

        return response

    return middleware
