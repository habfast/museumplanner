from django.utils.http import urlencode
from rest_framework.pagination import PageNumberPagination, _positive_int
from rest_framework.response import Response


class HarvardArtsMuseumApiPagination(PageNumberPagination):
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'info': {
                'totalrecordsperquery': self.page.paginator.per_page,
                'totalrecords': self.page.paginator.count,
                'pages': self.page.paginator.num_pages,
                'page': self.page.number,
                'next': self.get_next_link(),
                'responsetime': 'N/A'  # This would typically come from the API response
            },
            'records': data
        })

    def get_next_link(self):
        if not self.page.has_next():
            return None
        url = self.request.build_absolute_uri()
        page_number = self.page.next_page_number()
        return self.replace_query_param(url, self.page_query_param, page_number)

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        url = self.request.build_absolute_uri()
        page_number = self.page.previous_page_number()
        return self.replace_query_param(url, self.page_query_param, page_number)

    def replace_query_param(self, url, key, val):
        query_params = self.request.query_params.copy()
        query_params[key] = val
        return '{}?{}'.format(self.request.path, urlencode(query_params))

    def get_page_size(self, request):
        if self.page_size_query_param:
            try:
                return _positive_int(
                    request.query_params[self.page_size_query_param],
                    strict=True,
                    cutoff=self.max_page_size
                )
            except (KeyError, ValueError):
                pass

        return 10

    def get_page_number(self, request, paginator):
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            return paginator.num_pages
        try:
            page_number = int(page_number)
        except ValueError:
            page_number = 1
        if page_number < 1:
            page_number = 1
        return page_number
