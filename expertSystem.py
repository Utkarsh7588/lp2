
import pandas as pd


df = pd.read_csv('employee_performance_dataset.csv')


evaluation_rules = {
    'Productivity': {
        'High': lambda x: x > 7,
        'Medium': lambda x: 4 <= x <= 7,
        'Low': lambda x: x < 4
    },
    'Quality of Work': {
        'High': ['High'],
        'Medium': ['Medium'],
        'Low': ['Low']
    },
    'Communication Skills': {
        'Excellent': ['Excellent'],
        'Good': ['Good'],
        'Poor': ['Poor']
    },
    'Teamwork': {
        'Excellent': ['Excellent'],
        'Good': ['Good', 'Average'],
        'Poor': []
    },
    'Adherence to Deadlines': {
        'Excellent': lambda x: x == 1,
        'Poor': lambda x: x == 0
    }
}


for index, row in df.iterrows():
    performance = {}

    for metric, rules in evaluation_rules.items():
        value = row[metric]
        for level, rule in rules.items():
            if callable(rule):
                if rule(value):
                    performance[metric] = level
            elif value in rule:
                performance[metric] = level
    

    df.at[index, 'Performance Evaluation'] = max(performance.values())


print(df)
