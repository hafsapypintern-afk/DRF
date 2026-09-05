from django.db import models

# Pygments provides information about supported programming languages
from pygments.lexers import get_all_lexers

# Pygments provides different syntax-highlighting styles
from pygments.styles import get_all_styles


# Get all available Pygments language lexers.
# We keep only lexers that have aliases.
LEXERS = [item for item in get_all_lexers() if item[1]]


# Convert the Pygments lexer information into choices
# that Django can use for the language field.
LANGUAGE_CHOICES = sorted([
    (item[1][0], item[0])
    for item in LEXERS
])


# Get all available Pygments syntax-highlighting styles
# and convert them into Django choices.
STYLE_CHOICES = sorted([
    (item, item)
    for item in get_all_styles()
])


class Snippet(models.Model):

    # Automatically stores the date and time
    # when the snippet is first created.
    created = models.DateTimeField(auto_now_add=True)

    # Stores the title of the snippet.
    # The title is optional because blank=True.
    # If no title is provided, the default is an empty string.
    title = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    # Stores the actual source code.
    # TextField allows us to store longer pieces of text.
    code = models.TextField()

    # Stores True or False depending on whether
    # line numbers should be displayed.
    linenos = models.BooleanField(default=False)

    # Stores the programming language of the code.
    # The value must come from LANGUAGE_CHOICES.
    # Python is used by default.
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        default="python",
        max_length=100
    )

    # Stores the syntax-highlighting style.
    # The value must come from STYLE_CHOICES.
    # Friendly is used by default.
    style = models.CharField(
        choices=STYLE_CHOICES,
        default="friendly",
        max_length=100
    )

    class Meta:
        # When snippets are retrieved, order them
        # from oldest to newest based on creation time.
        ordering = ["created"]