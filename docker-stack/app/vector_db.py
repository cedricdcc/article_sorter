# Vector database utilities for storing and retrieving data

import weaviate  # type: ignore
from typing import Optional

client: Optional[weaviate.Client] = None


def connect_to_vector_db():
    """
    Establishes a connection to the vector database.
    :return: Connection object or None if connection fails
    """
    global client
    try:
        client = weaviate.Client("http://vector-db:8080")
        print("Connected to the vector database.")
        return True
    except Exception as e:
        print(f"Error connecting to the vector database: {e}")
        return None


def store_data_in_vector_db(data):
    """
    Stores data in the vector database.
    :param data: The data to store (e.g., abstract, metadata)
    :return: Success status
    """
    try:
        assert client is not None, "Database client not connected"
        class_name = "Article"
        current_schema = client.schema.get()
        classes = [cls.get("class") for cls in current_schema.get("classes", [])]
        if class_name not in classes:
            schema = {
                "class": class_name,
                "properties": [
                    {"name": "url", "dataType": ["string"]},
                    {"name": "collection", "dataType": ["string"]},
                    {"name": "abstract", "dataType": ["string"]},
                ],
            }
            client.schema.create_class(schema)
            print(f"Created class: {class_name}")

        # Insert data into the class
        client.data_object.create(
            {
                "url": data.get("url"),
                "collection": data.get("collection"),
                "abstract": data.get("abstract"),
            },
            class_name=class_name,
        )
        print(f"Data inserted into class: {data}")
        return True
    except Exception as e:
        print(f"Error storing data in the vector database: {e}")
        return False


def query_vector_db(query):
    """
    Queries the vector database.
    :param query: The query to execute
    :return: Query results
    """
    try:
        assert client is not None, "Database client not connected"
        class_name = "Article"
        results = (
            client.query.get(class_name, ["url", "collection", "abstract"])
            .with_where(query)
            .do()
        )
        return results.get("data", {}).get("Get", {}).get(class_name, [])
    except Exception as e:
        print(f"Error querying the vector database: {e}")
        return []
