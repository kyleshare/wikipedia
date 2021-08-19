from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # title of any encyclopedia entry
    path("search", views.search_entry, name="search_entry"),
    path("create", views.create_page, name="create"),
    path("<str:entry>", views.display_entry, name="display_entry"),
]

