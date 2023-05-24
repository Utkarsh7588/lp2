# Define the rules for the medical expert system
rules = [
    {"symptom": "fever", "condition": "infection", "recommendation": "Take antibiotics"},
    {"symptom": "cough", "condition": "respiratory infection", "recommendation": "Rest and drink fluids"},
    {"symptom": "headache", "condition": "migraine", "recommendation": "Take pain relievers and rest"},
]

# Function to process user input and provide recommendations
def process_input(symptoms):
    matching_rules = []
    for rule in rules:
        if rule["symptom"] in symptoms:
            matching_rules.append(rule)

    if len(matching_rules) == 0:
        return "No matching condition found."

    # Display recommendations for matched conditions
    recommendations = []
    for rule in matching_rules:
        recommendations.append(rule["recommendation"])

    # recommendations = [rule["recommendation"] for rule in matching_rules]
    return ", ".join(recommendations)

# User input example
user_symptoms = input("Enter symptom : ").split(" ")

# Process the user input and get recommendations
output = process_input(user_symptoms)
print(output)