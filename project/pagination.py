from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


### pagepagination 
class BookPageNumberpagination(PageNumberPagination):
    page_size = 2
    