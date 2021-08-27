from book.views import createbook
from django.urls import path


urlpatterns = [
    path('create/', createbook),
]
