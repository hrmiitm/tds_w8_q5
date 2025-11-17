# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib",
#     "numpy",
#     "pandas",
#     "seaborn",
# ]
# ///
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
import numpy as np

# Student email for verification
student_email = "22f3002460@ds.study.iitm.ac.in"

# Generate realistic employee dataset (100 employees)
np.random.seed(42)

departments = ['Sales', 'IT', 'Finance', 'HR', 'R&D', 'Marketing', 'Operations']
regions = ['North America', 'Europe', 'Asia', 'Middle East', 'Africa', 'Latin America']

# Create weighted distribution to ensure Sales department has sufficient representation
dept_weights = [0.20, 0.18, 0.15, 0.12, 0.15, 0.10, 0.10]  # 20% Sales

data = {
    'employee_id': [f'EMP{str(i+1).zfill(3)}' for i in range(100)],
    'department': np.random.choice(departments, size=100, p=dept_weights),
    'region': np.random.choice(regions, size=100),
    'performance_score': np.random.uniform(50, 100, size=100).round(2),
    'years_experience': np.random.randint(1, 20, size=100),
    'satisfaction_rating': np.random.uniform(2.5, 5.0, size=100).round(1)
}

df = pd.DataFrame(data)

# Display first 5 rows
print("=" * 80)
print("EMPLOYEE PERFORMANCE ANALYSIS")
print("=" * 80)
print(f"\nStudent Email: {student_email}\n")
print("Sample Dataset (first 5 rows):")
print(df.head().to_string())
print("\n" + "=" * 80)

# Calculate frequency count for "Sales" department
sales_count = df[df['department'] == 'Sales'].shape[0]
print(f"\nFrequency count for 'Sales' department: {sales_count}")
print("=" * 80)

# Calculate frequency for all departments
dept_counts = df['department'].value_counts().sort_index()
print("\nDepartment Distribution:")
print(dept_counts.to_string())
print("=" * 80 + "\n")

# Create histogram visualization
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")
sns.set_palette("Set2")

# Create histogram
dept_counts_sorted = df['department'].value_counts().sort_values(ascending=False)
bars = plt.bar(dept_counts_sorted.index, dept_counts_sorted.values, 
               color=sns.color_palette("Set2", len(dept_counts_sorted)),
               edgecolor='black', linewidth=1.2)

# Customize the plot
plt.title('Employee Distribution Across Departments\nTechnology Company - Workforce Analysis', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Department', fontsize=13, fontweight='bold')
plt.ylabel('Number of Employees', fontsize=13, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=11)
plt.yticks(fontsize=11)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add grid for better readability
plt.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()

# Save plot to BytesIO object and encode as base64
buffer = BytesIO()
plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
buffer.seek(0)
image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
plt.close()

# Create comprehensive HTML report
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Performance Analysis - Technology Company</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
        }}
        .container {{
            background-color: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
            border-left: 4px solid #3498db;
            padding-left: 15px;
        }}
        .email {{
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
            color: #2c3e50;
            margin: 20px 0;
        }}
        .highlight {{
            background-color: #fffbcc;
            padding: 15px;
            border-left: 4px solid #f39c12;
            margin: 20px 0;
            font-size: 18px;
            font-weight: bold;
            color: #e67e22;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        th {{
            background-color: #3498db;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: bold;
        }}
        td {{
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }}
        tr:hover {{
            background-color: #f5f5f5;
        }}
        .chart-container {{
            text-align: center;
            margin: 30px 0;
            padding: 20px;
            background-color: #fafafa;
            border-radius: 8px;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}
        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        .stat-value {{
            font-size: 32px;
            font-weight: bold;
            margin: 10px 0;
        }}
        .stat-label {{
            font-size: 14px;
            opacity: 0.9;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #ecf0f1;
            text-align: center;
            color: #7f8c8d;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Employee Performance Analysis</h1>
        <p><strong>Company:</strong> Technology Company (Multi-Regional Operations)</p>
        <p><strong>Analysis Date:</strong> November 17, 2025</p>
        
        <div class="email">
            📧 Analyst Email: {student_email}
        </div>

        <h2>📈 Executive Summary</h2>
        <p>This report presents a comprehensive analysis of employee performance data across 100 employees 
        spanning multiple departments and regions. The analysis focuses on departmental distribution patterns 
        to support strategic workforce planning and resource allocation decisions.</p>

        <h2>🎯 Key Finding: Sales Department Analysis</h2>
        <div class="highlight">
            Frequency count for 'Sales' department: {sales_count} employees
        </div>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-label">Total Employees</div>
                <div class="stat-value">{len(df)}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Departments</div>
                <div class="stat-value">{len(departments)}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Regions</div>
                <div class="stat-value">{len(regions)}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Sales Employees</div>
                <div class="stat-value">{sales_count}</div>
            </div>
        </div>

        <h2>📊 Department Distribution Visualization</h2>
        <div class="chart-container">
            <img src="data:image/png;base64,{image_base64}" alt="Department Distribution Histogram">
            <p><em>Figure 1: Employee distribution across all departments showing workforce allocation</em></p>
        </div>

        <h2>📋 Department Frequency Table</h2>
        <table>
            <thead>
                <tr>
                    <th>Department</th>
                    <th>Employee Count</th>
                    <th>Percentage</th>
                </tr>
            </thead>
            <tbody>
                {"".join([f"<tr><td>{dept}</td><td>{count}</td><td>{count/len(df)*100:.1f}%</td></tr>" 
                          for dept, count in dept_counts_sorted.items()])}
            </tbody>
        </table>

        <h2>📂 Sample Dataset (First 5 Rows)</h2>
        <table>
            <thead>
                <tr>
                    {"".join([f"<th>{col}</th>" for col in df.columns])}
                </tr>
            </thead>
            <tbody>
                {"".join([f"<tr>{''.join([f'<td>{val}</td>' for val in row])}</tr>" 
                          for row in df.head().values])}
            </tbody>
        </table>

        <h2>💡 Strategic Insights</h2>
        <ul>
            <li><strong>Sales Department:</strong> Comprises {sales_count} employees ({sales_count/len(df)*100:.1f}% of workforce)</li>
            <li><strong>Largest Department:</strong> {dept_counts_sorted.index[0]} with {dept_counts_sorted.values[0]} employees</li>
            <li><strong>Smallest Department:</strong> {dept_counts_sorted.index[-1]} with {dept_counts_sorted.values[-1]} employees</li>
            <li><strong>Workforce Balance:</strong> Distribution analysis reveals opportunities for strategic resource reallocation</li>
        </ul>

        <h2>🎯 Recommendations</h2>
        <ol>
            <li>Review Sales department capacity relative to business growth targets</li>
            <li>Assess whether current distribution aligns with strategic priorities</li>
            <li>Consider cross-training programs between over and under-represented departments</li>
            <li>Monitor performance scores and satisfaction ratings by department for retention strategies</li>
        </ol>

        <div class="footer">
            <p>Generated using Python with pandas, matplotlib, and seaborn</p>
            <p>Analyst: {student_email}</p>
            <p>© 2025 Technology Company - HR Analytics Division</p>
        </div>
    </div>
</body>
</html>
"""

# Save HTML file
with open('employee_analysis.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ HTML report generated successfully: employee_analysis.html")
print(f"✅ Sales department frequency count: {sales_count}")
print("✅ Histogram visualization created and embedded in HTML")
