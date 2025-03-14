# Vector database utilities for storing and retrieving data

from pymilvus import connections, Collection, utility


def connect_to_vector_db():
    """
    Establishes a connection to the vector database.
    :return: Connection object or None if connection fails
    """
    try:
        connections.connect(alias="default", host="localhost", port="19530")
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
        collection_name = "articles"
        if not utility.has_collection(collection_name):
            # Define schema and create collection if it doesn't exist
            from pymilvus import FieldSchema, CollectionSchema, DataType

            fields = [
                FieldSchema(
                    name="id", dtype=DataType.INT64, is_primary=True, auto_id=True
                ),
                FieldSchema(name="url", dtype=DataType.VARCHAR, max_length=500),
                FieldSchema(name="collection", dtype=DataType.VARCHAR, max_length=100),
                FieldSchema(name="abstract", dtype=DataType.VARCHAR, max_length=2000),
            ]
            schema = CollectionSchema(fields, description="Article collection")
            Collection(name=collection_name, schema=schema)
            print(f"Created collection: {collection_name}")

        # Insert data into the collection
        collection = Collection(collection_name)
        entities = [
            [data.get("url")],
            [data.get("collection")],
            [data.get("abstract")],
        ]
        collection.insert(entities)
        print(f"Data inserted into collection: {data}")
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
        collection_name = "articles"
        collection = Collection(collection_name)
        results = collection.query(expr=query)
        return results
    except Exception as e:
        print(f"Error querying the vector database: {e}")
        return []
