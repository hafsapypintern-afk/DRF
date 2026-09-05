from rest_framework import serializers
from snippets.models import Snippet


# ModelSerializer automatically creates serializer fields
# based on the fields defined in the Snippet model.
class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        # Tell DRF which Django model this serializer is connected to.
        model = Snippet

        # Tell DRF which model fields should be included
        # in the API representation.
        fields = [
            "id",
            "title",
            "code",
            "linenos",
            "language",
            "style",
        ]