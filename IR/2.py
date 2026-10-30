
documents = {
    "D1": "Machine Learning is useful",
    "D2": "Machine Learning uses data",
    "D3": "Data Science is useful",
}

inverted_index = {}
for doc_id, text in documents.items():
    for word in text.lower().split():
        inverted_index.setdefault(word, []).append(doc_id)

print("inverted_index:")
print(inverted_index)

query = input("\nsearch: ").lower()
print("matching documents:", inverted_index.get(query, "No documents"))
