import json

import meilisearch
import requests

client = meilisearch.Client(
    "http://localhost:7700", "--add--token--here--"
)

URL = "https://portal.merisehat.pk/portal/api/v2/filter-find-doctor?page=1&city_id=1"


def add_data():
    response = requests.get(URL)
    doctors_data = json.loads(response.text)
    client.create_index("merisehat_doc", {"primaryKey": "id"})
    index = client.index("merisehat_doc")
    status = index.add_documents(doctors_data["data"]["data"])
    print(f"client status: {status}")


def search_data(query):
    search_result = client.index("merisehat_doc").search(query)
    return search_result
