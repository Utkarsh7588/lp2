rules = [
    {
        "indicator": "RSI",
        "condition": "High",
        "threshold": 70,
        "recommendation": "Consider selling the stock."
    },
    {
        "indicator": "RSI",
        "condition": "Low",
        "threshold": 30,
        "recommendation": "Consider buying the stock."
    },
    {
        "indicator": "MACD",
        "condition": "Positive",
        "histogram_threshold": 0,
        "recommendation": "Consider buying the stock."
    },
    {
        "indicator": "MACD",
        "condition": "Negative",
        "histogram_threshold": 0,
        "recommendation": "Consider selling the stock."
    },
    {
        "indicator": "Moving Average",
        "condition": "Upward",
        "period": "50-day",
        "recommendation": "Consider buying the stock."
    },
    {
        "indicator": "Moving Average",
        "condition": "Downward",
        "period": "50-day",
        "recommendation": "Consider selling the stock."
    }
]

def process_input(indicator, condition):
    matching_rules = []
    for rule in rules:
        if rule["indicator"] == indicator and rule["condition"] == condition:
            matching_rules.append(rule)

    if len(matching_rules) == 0:
        return "No recommendation found for the given indicator and condition."

    recommendations = []
    for rule in matching_rules:
        recommendations.append(rule["recommendation"])

    return ", ".join(recommendations)

user_indicator = input("Enter the trading indicator (RSI, MACD, Moving Average): ")
user_condition = input("Enter the condition (High, Low, Positive, Negative, Upward, Downward): ")

output = process_input(user_indicator, user_condition)
print(output)
