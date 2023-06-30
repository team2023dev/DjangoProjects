from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination

# class MyPageNumberPaginations(PageNumberPagination):
#     page_size=5
#     page_query_param='p'
#     page_size_query_param='records'
#     max_page_size=10
#     last_page_strings='end'

# class MyLimitOffsetPaginations(LimitOffsetPagination):
#     default_limit=5
#     limit_query_param='mylimit'
#     offset_query_param='myoffset'
#     max_limit=6

class MyCursorPaginations(CursorPagination):
    page_size=10
    ordering='name'
    cursor_query_param='cu'