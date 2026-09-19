#json date using print student marks and name
json_data=  {
    "students": [
        {"name": "Arun", "marks": 85},
        {"name": "Ravi", "marks": 90},
        {"name": "John", "marks": 75}
    ]
}
print(f"Name: {json_data['students'][0]['name']} Marks: {json_data['students'][0]['marks']}")
print(f"Name: {json_data['students'][1]['name']} Marks: {json_data['students'][1]['marks']}")