rules = [
    {
        "issue": "Password Reset",
        "category": "Account",
        "recommendation": "Verify user's identity and reset the password."
    },
    {
        "issue": "Software Installation",
        "category": "Software",
        "recommendation": "Provide instructions for software installation or assist remotely if required."
    },
    {
        "issue": "Network Connectivity",
        "category": "Network",
        "recommendation": "Troubleshoot network connection issues and assist in resolving them."
    },
    {
        "issue": "Hardware Failure",
        "category": "Hardware",
        "recommendation": "Diagnose hardware problem and coordinate repair or replacement."
    },
    {
        "issue": "Email Configuration",
        "category": "Email",
        "recommendation": "Guide user through email configuration steps or update settings remotely."
    }
]

def process_input(issue):
    matching_rules = []
    for rule in rules:
        if rule["issue"] == issue:
            matching_rules.append(rule)

    if len(matching_rules) == 0:
        return "No recommendation found for the given issue."

    recommendations = []
    for rule in matching_rules:
        recommendations.append(rule["recommendation"])

    return ", ".join(recommendations)

user_issue = input("Enter the help desk issue: ")

output = process_input(user_issue)
print(output)
