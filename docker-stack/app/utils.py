# Helper functions for the Docker stack

import re


def validate_url(url):
    """
    Validates the given URL.
    :param url: The URL to validate
    :return: True if valid, False otherwise
    """
    regex = re.compile(
        r"^(?:http|https)://"  # http:// or https://
        r"(?:\S+(?::\S*)?@)?"  # optional username:password@
        r"(?:(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])"  # IP address exclusion
        r"(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}"  # IP address exclusion
        r"(?:\.(?:[0-9]\d?|1\d\d|2[0-4]\d|25[0-5]))|"  # IP address exclusion
        r"(?:(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}))"  # domain...
        r"(?::\d{2,5})?"  # optional port
        r"(?:/\S*)?$"  # resource path
    )
    return re.match(regex, url) is not None


def categorize_article(collection, text):
    """
    Categorizes an article into a predefined collection.
    :param collection: The provided collection or None
    :param text: The text of the article
    :return: The determined collection
    """
    predefined_categories = ["Science", "Technology", "Health", "Education"]
    if collection:
        return collection
    for category in predefined_categories:
        if category.lower() in text.lower():
            return category
    return "Uncategorized"
