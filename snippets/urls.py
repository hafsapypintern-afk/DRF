from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views


urlpatterns = [

    # /snippets/
    #
    # SnippetList is a class-based view.
    # .as_view() converts the class into a view
    # that Django can use for this URL.
    #
    # GET  → SnippetList.get()
    # POST → SnippetList.post()
    path(
        "snippets/",
        views.SnippetList.as_view()
    ),

    # /snippets/<id>/
    #
    # GET    → SnippetDetail.get()
    # PUT    → SnippetDetail.put()
    # DELETE → SnippetDetail.delete()
    path(
        "snippets/<int:pk>/",
        views.SnippetDetail.as_view()
    ),
]


# Add optional format suffixes.
#
# This allows URLs such as:
#
# /snippets/
# /snippets.json
# /snippets.api
#
# And:
#
# /snippets/1/
# /snippets/1.json
# /snippets/1.api
urlpatterns = format_suffix_patterns(urlpatterns)
