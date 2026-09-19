document = [("doc1", "Python basics"),
             ("doc2", "What is RAG?"),
             ("doc3", "What is an LLM?"),
             ("doc1", "Python basics"),
             ("doc2", "What is RAG?")]
def get_unique_documents(document):
    unique_documents = []
    for doc in document:
        if doc not in unique_documents:
            unique_documents.append(doc)
    return unique_documents

print(get_unique_documents(document))
