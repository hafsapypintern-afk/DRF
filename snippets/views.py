from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(["GET", "POST"])
def snippet_list(request, format=None):
    """
    List all snippets, or create a new snippet.
    """

    # -------------------------
    # GET /snippets/
    # -------------------------
    # Get all Snippet objects from the database.
    if request.method == "GET":
        snippets = Snippet.objects.all()

        # Serialize multiple Snippet objects.
        # many=True is required because there are multiple objects.
        serializer = SnippetSerializer(snippets, many=True)

        # DRF Response handles the response format.
        return Response(serializer.data)

    # -------------------------
    # POST /snippets/
    # -------------------------
    elif request.method == "POST":

        # request.data contains the data sent by the client.
        #
        # In Tutorial 1 we used:
        # JSONParser().parse(request)
        #
        # DRF now handles the parsing for us.
        serializer = SnippetSerializer(data=request.data)

        # Validate the incoming data.
        if serializer.is_valid():

            # Save the validated data to the database.
            serializer.save()

            # HTTP_201_CREATED means a new resource was created.
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        # HTTP_400_BAD_REQUEST means the submitted data is invalid.
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a single snippet.
    """

    # Find the Snippet using its primary key.
    try:
        snippet = Snippet.objects.get(pk=pk)

    # If the snippet doesn't exist, return HTTP 404.
    except Snippet.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )

    # -------------------------
    # GET /snippets/<id>/
    # -------------------------
    if request.method == "GET":

        # Serialize one Snippet object.
        # many=True is not needed for a single object.
        serializer = SnippetSerializer(snippet)

        return Response(serializer.data)

    # -------------------------
    # PUT /snippets/<id>/
    # -------------------------
    elif request.method == "PUT":

        # Pass:
        # 1. the existing object
        # 2. the new data
        #
        # DRF has already parsed the request body,
        # so we can use request.data directly.
        serializer = SnippetSerializer(
            snippet,
            data=request.data
        )

        # Validate the new data.
        if serializer.is_valid():

            # Save the updated object.
            serializer.save()

            return Response(serializer.data)

        # Return validation errors.
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # -------------------------
    # DELETE /snippets/<id>/
    # -------------------------
    elif request.method == "DELETE":

        # Delete the Snippet from the database.
        snippet.delete()

        # HTTP 204 means successful request with no response body.
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )