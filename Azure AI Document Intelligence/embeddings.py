from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="<key>",
    api_version="2024-02-15-preview",
    azure_endpoint="https://myopenai.openai.azure.com/"
)

embedding = client.embeddings.create(
    model="text-embedding-ada-002",
    input="Azure AI Search enables semantic search"
)
print(embedding.data[0].embedding)
