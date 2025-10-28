import random

# Some common English words
words = ["data", "compression", "algorithm", "python", "encoding", "decode",
         "tree", "graph", "machine", "learning", "huffman", "test", "system",
         "analysis", "network", "model", "performance", "byte", "string", "code"]

# Generate about 5 MB text
target_size = 5 * 1024 * 1024  # 5 MB in bytes
text = ""

while len(text.encode('utf-8')) < target_size:
    text += " ".join(random.choices(words, k=50)) + "\n"

with open("large_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Generated large_text.txt (~5MB)")
