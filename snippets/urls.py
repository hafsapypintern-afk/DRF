from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views


urlpatterns = [

    # /snippets/
    #
    # GET  → list all snippets
    # POST → create a new snippet
    path("snippets/", views.snippet_list),

    # /snippets/<id>/
    #
    # GET    → retrieve one snippet
    # PUT    → update one snippet
    # DELETE → delete one snippet
    path("snippets/<int:pk>/", views.snippet_detail),
]


# Add optional format suffixes to our API URLs.
# This allows:
# /snippets/
# /snippets.json
# /snippets.api
# And for individual snippets:
# /snippets/1/
# /snippets/1.json
# /snippets/1.api
urlpatterns = format_suffix_patterns(urlpatterns)