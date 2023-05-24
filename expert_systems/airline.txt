rules = [
    {"location": "New York", "type": "Passenger", "recommendation": "Flight XYZ123 is available from New York."},
    {"location": "London", "type": "Passenger", "recommendation": "Flight ABC456 is available from London."},
    {"location": "Paris", "type": "Passenger", "recommendation": "Flight DEF789 is available from Paris."},
    {"location": "New York", "type": "Cargo", "recommendation": "Cargo shipment options available from New York."},
    {"location": "London", "type": "Cargo", "recommendation": "Cargo shipment options available from London."},
    {"location": "Paris", "type": "Cargo", "recommendation": "Cargo shipment options available from Paris."},
]

def process_input(location, type):
    matching_rules = []
    for rule in rules:
        if rule["location"] == location and rule["type"] == type:
            matching_rules.append(rule)

    if len(matching_rules) == 0:
        return "No matching options found."

    recommendations = []
    for rule in matching_rules:
        recommendations.append(rule["recommendation"])

    return ", ".join(recommendations)

user_location = input("Enter location: ")
user_type = input("Enter type (Passenger or Cargo): ")

output = process_input(user_location, user_type)
print(output)
