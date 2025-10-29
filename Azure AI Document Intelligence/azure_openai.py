from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="<key>",
    api_version="2024-02-15-preview",
    azure_endpoint="https://myopenai.openai.azure.com/"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Explain Azure AI Search"}]
)
print(response.choices[0].message.content)
