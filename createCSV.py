import pandas as pd
data = {
    'Employee ID': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Productivity': [8, 6, 7, 9, 5, 6, 7, 9, 5],
    'Quality of Work': ['High', 'Medium', 'Low', 'High', 'Medium', 'Medium', 'Low', 'High', 'Medium'],
    'Communication Skills': ['Excellent', 'Good', 'Poor', 'Good', 'Excellent', 'Good', 'Poor', 'Good', 'Excellent'],
    'Teamwork': ['Excellent', 'Good', 'Poor', 'Good', 'Good', 'Good', 'Poor', 'Good', 'Good'],
    'Adherence to Deadlines': [1, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
df.to_csv('employee_data.csv', index=False)
