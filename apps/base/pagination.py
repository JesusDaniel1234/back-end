from rest_framework.pagination import PageNumberPagination

class SmallPaginationClass(PageNumberPagination):
    page_size = 6
    page_query_param = "page"
    page_size_query_param = "limit"
    max_page_size = 10


class MediumPaginationClass(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "limit"
    max_page_size = 18


class LargePaginationClass(PageNumberPagination):
    page_size = 18
    page_query_param = "page"
    page_size_query_param = "limit"
    max_page_size = 30