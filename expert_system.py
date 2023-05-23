import pandas as pd


df = pd.read_csv('employee_performance_dataset.csv')

evaluation_rules = {
    'Productivity': {
        'High': 9,
        'Medium': 6,
        'Low': 3
    },
    'Quality of Work': {
        'High': 9,
        'Medium': 6,
        'Low': 3
    },
    'Communication Skills': {
        'Excellent': 9,
        'Average':7,
        'Good': 5,
        'Poor': 3
    },
    'Teamwork': {
         'Excellent': 9,
        'Average':7,
        'Good': 5,
        'Poor': 3
    },
    'Adherence to Deadlines': {
        'Excellent': 10,
        'Poor': 5
    }
}

for index, row in df.iterrows():
    performance = {}

    for metric, score_mapping in evaluation_rules.items():
        value = row[metric]

        if value in score_mapping:
            score = score_mapping[value]
            performance[metric] = score

    overall_score = sum(performance.values()) / len(performance)

    if overall_score >= 8:
        performance['Overall Score'] = overall_score
        performance['Performance Rating'] = 'Excellent'
    elif overall_score >= 5:
        performance['Overall Score'] = overall_score
        performance['Performance Rating'] = 'Good'
    elif overall_score >=3:
        performance['Overall Score'] = overall_score
        performance['Performance Rating'] = 'Average'

    df.at[index, 'Performance Evaluation'] = performance['Performance Rating']
    df.at[index, 'Overall Score'] = performance['Overall Score']

print(df)
