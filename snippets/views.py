from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all snippets, or create a new snippet.
    """

    # -------------------------
    # GET /snippets/
    # -------------------------
    # Get all Snippet objects from the database.
    if request.method == "GET":
        snippets = Snippet.objects.all()

        # Convert multiple Snippet model objects
        # into Python data that can be returned as JSON.
        # many=True is required because we have multiple objects.
        serializer = SnippetSerializer(snippets, many=True)

        # Return the serialized data as a JSON response.
        # safe=False is required because serializer.data
        # is a list rather than a dictionary.
        return JsonResponse(serializer.data, safe=False)

    # -------------------------
    # POST /snippets/
    # -------------------------
    # Create a new Snippet.
    elif request.method == "POST":

        # Read the JSON body sent by the client
        # and convert it into Python data.
        data = JSONParser().parse(request)

        # Pass the incoming data to the serializer
        # so DRF can validate it.
        serializer = SnippetSerializer(data=data)

        # Check whether the submitted data is valid.
        if serializer.is_valid():

            # Save the validated data to the database.
            # ModelSerializer automatically creates
            # the Snippet object for us.
            serializer.save()

            # Return the newly created snippet as JSON.
            # 201 means "Created".
            return JsonResponse(serializer.data, status=201)

        # If validation fails, return the validation errors.
        # 400 means "Bad Request".
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a single snippet.
    """

    # Try to find the requested Snippet by its primary key.
    try:
        snippet = Snippet.objects.get(pk=pk)

    # If no Snippet exists with that ID,
    # return a 404 Not Found response.
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    # -------------------------
    # GET /snippets/<id>/
    # -------------------------
    if request.method == "GET":

        # Serialize one Snippet object.
        # We don't use many=True because this is only one object.
        serializer = SnippetSerializer(snippet)

        # Return that snippet as JSON.
        return JsonResponse(serializer.data)

    # -------------------------
    # PUT /snippets/<id>/
    # -------------------------
    elif request.method == "PUT":

        # Read the JSON request body.
        data = JSONParser().parse(request)

        # Give the serializer:
        # 1. the existing object to update
        # 2. the new data
        serializer = SnippetSerializer(snippet, data=data)

        # Validate the new data.
        if serializer.is_valid():

            # Save the updated Snippet.
            # ModelSerializer handles the update for us.
            serializer.save()

            # Return the updated object as JSON.
            return JsonResponse(serializer.data)

        # Return validation errors if the data is invalid.
        return JsonResponse(serializer.errors, status=400)

    # -------------------------
    # DELETE /snippets/<id>/
    # -------------------------
    elif request.method == "DELETE":

        # Delete the Snippet from the database.
        snippet.delete()

        # 204 means the request succeeded
        # but there is no response body.
        return HttpResponse(status=204)