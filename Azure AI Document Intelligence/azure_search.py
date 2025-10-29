from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

client = SearchClient(endpoint="https://mysearch.search.windows.net",
                      index_name="docs-index",
                      credential=AzureKeyCredential("<key>"))

results = client.search("CEO of Microsoft")
for r in results:
    print(r["content"])
