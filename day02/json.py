#json value fetching an print the value what you need
json_data = {
    "name": "Arun",
    "age": 25,
    "role": "Generative AI Developer",
    "skills": [
        "Python",
        "RAG",
        "LLM"
    ]
}
print(json_data["name"])
print(json_data["age"])
print(json_data["role"])
print(json_data["skills"])
print(json_data["skills"][0])
print(json_data["skills"][1])  