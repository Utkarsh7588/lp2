# Define evaluation criteria and weights
criteria = {
    'sales': 0.5,
    'quality': 0.3,
    'attendance': 0.1,
    'teamwork': 0.1
}

# Define rules for each criteria
sales_rule = {
    'high': lambda x: x >= 80,
    'medium': lambda x: 60 <= x < 80,
    'low': lambda x: x < 60
}

quality_rule = {
    'high': lambda x: x >= 90,
    'medium': lambda x: 70 <= x < 90,
    'low': lambda x: x < 70
}

attendance_rule = {
    'high': lambda x: x >= 95,
    'medium': lambda x: 90 <= x < 95,
    'low': lambda x: x < 90
}

teamwork_rule = {
    'high': lambda x: x >= 80,
    'medium': lambda x: 60 <= x < 80,
    'low': lambda x: x < 60
}

# Define a function to calculate the score for each criterion
def calculate_score(rule, value):
    for k, v in rule.items():
        if v(value):
            return k

# Define a function to evaluate an employee's performance
def evaluate_performance():
    # Prompt the user for input
    sales = float(input("Enter the sales score (0-100): "))
    quality = float(input("Enter the quality score (0-100): "))
    attendance = float(input("Enter the attendance score (0-100): "))
    teamwork = float(input("Enter the teamwork score (0-100): "))

    # Calculate scores for each criterion
    sales_score = calculate_score(sales_rule, sales)
    quality_score = calculate_score(quality_rule, quality)
    attendance_score = calculate_score(attendance_rule, attendance)
    teamwork_score = calculate_score(teamwork_rule, teamwork)

    # Calculate overall performance score
    performance_score = (
        criteria['sales'] * (sales_score == 'high') +
        criteria['quality'] * (quality_score == 'high') +
        criteria['attendance'] * (attendance_score == 'high') +
        criteria['teamwork'] * (teamwork_score == 'high')
    )

    # Determine the employee's evaluation based on the performance score
    if performance_score >= 0.8:
        evaluation = 'Excellent'
    elif performance_score >= 0.7:
        evaluation = 'Very Good'
    elif performance_score >= 0.6:
        evaluation = 'Good'
    elif performance_score >= 0.5:
        evaluation = 'Average'
    else:
        evaluation = 'Poor'

    return evaluation



# Evaluate an employee's performance
evaluation = evaluate_performance()
print(f"Employee's evaluation is: {evaluation}")
