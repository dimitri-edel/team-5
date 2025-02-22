from rest_framework.pagination import PageNumberPagination

class UserProfilePagination(PageNumberPagination):
    page_size = 10  # Default number of objects per page
    page_size_query_param = 'page_size'
    max_page_size = 100
