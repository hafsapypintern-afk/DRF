from django.urls import path
from snippets import views


urlpatterns = [

    # /snippets/
    # Sends the request to the snippet_list view.
    path("snippets/", views.snippet_list),

    # /snippets/<id>/
    # <int:pk> captures the snippet ID from the URL
    # and passes it to snippet_detail().
    path("snippets/<int:pk>/", views.snippet_detail),
]