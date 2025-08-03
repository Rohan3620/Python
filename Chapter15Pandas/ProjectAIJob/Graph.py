import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a dummy DataFrame
data = {
    'job_id': range(20),
    'job_title': ['Data Scientist', 'Software Engineer', 'Data Analyst', 'ML Engineer'] * 5,
    'salary_usd': np.random.randint(50000, 200000, 20),
    'salary_currency': ['USD'] * 20,
    'experience_level': ['Entry', 'Mid', 'Senior', 'Executive'] * 5,
    'employment_type': ['Full-time', 'Part-time', 'Contract'] * 6 + ['Full-time', 'Part-time'],
    'company_location': ['USA', 'India', 'UK', 'Canada'] * 5,
    'company_size': ['Small', 'Medium', 'Large'] * 6 + ['Small', 'Medium'],
    'employee_residence': ['USA', 'India', 'UK', 'Canada'] * 5,
    'remote_ratio': np.random.randint(0, 101, 20),
    'required_skills': ['Python', 'SQL', 'ML', 'Cloud'] * 5,
    'education_required': ['Bachelors', 'Masters', 'PhD'] * 6 + ['Bachelors', 'Masters'],
    'years_experience': np.random.randint(1, 20, 20),
    'industry': ['Tech', 'Finance', 'Healthcare'] * 6 + ['Tech', 'Finance'],
    'posting_date': pd.to_datetime(['2024-01-01'] * 20),
    'application_deadline': pd.to_datetime(['2024-03-01'] * 20),
    'job_description_length': np.random.randint(100, 500, 20),
    'benefits_score': np.random.randint(50, 100, 20),
    'company_name': ['Google', 'Amazon', 'Microsoft', 'Apple'] * 5
}
df = pd.DataFrame(data)

# Create subplots
plt.figure(figsize=(15, 10))

# Plot 1: Histogram of salary_usd
ax1 = plt.subplot(2, 2, 1)
ax1.set_title("Distribution of Salary (USD)")
ax1.set_xlabel("Salary (USD)")
ax1.set_ylabel("Count")
ax1.hist(df['salary_usd'], bins=10, color='skyblue', edgecolor='black')

# Plot 2: Bar chart of average salary per experience level
ax2 = plt.subplot(2, 2, 2)
avg_salary_experience = df.groupby('experience_level')['salary_usd'].mean().reindex(['Entry', 'Mid', 'Senior', 'Executive'])
ax2.set_title("Average Salary by Experience Level")
ax2.set_xlabel("Experience Level")
ax2.set_ylabel("Average Salary (USD)")
ax2.bar(avg_salary_experience.index, avg_salary_experience.values, color='lightcoral')
plt.xticks(rotation=45, ha='right')

# Plot 3: Bar chart of average salary per company location
ax3 = plt.subplot(2, 2, 3)
avg_salary_location = df.groupby('company_location')['salary_usd'].mean().sort_values(ascending=False)
ax3.set_title("Average Salary by Company Location")
ax3.set_xlabel("Company Location")
ax3.set_ylabel("Average Salary (USD)")
ax3.bar(avg_salary_location.index, avg_salary_location.values, color='lightgreen')
plt.xticks(rotation=45, ha='right')

# Plot 4: Pie chart of employment type distribution
ax4 = plt.subplot(2, 2, 4)
employment_type_counts = df['employment_type'].value_counts()
ax4.set_title("Distribution of Employment Types")
ax4.pie(employment_type_counts, labels=employment_type_counts.index, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightskyblue', 'lightpink'])
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()