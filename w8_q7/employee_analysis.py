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
dept_weights = [0.20, 0.18, 0.15, 0.12, 0.15, 0.10, 0.10]

data = {
    'employee_id': [f'EMP{str(i+1).zfill(3)}' for i in range(100)],
    'department': np.random.choice(departments, size=100, p=dept_weights),
    'region': np.random.choice(regions, size=100),
    'performance_score': np.random.uniform(50, 100, size=100).round(2),
    'years_experience': np.random.randint(1, 20, size=100),
    'satisfaction_rating': np.random.uniform(2.5, 5.0, size=100).round(1)
}

df = pd.DataFrame(data)

# Calculate frequency count for "Sales" department
sales_count = df[df['department'] == 'Sales'].shape[0]
print(f"Frequency count for 'Sales' department: {sales_count}")

# Create histogram
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

dept_counts = df['department'].value_counts().sort_values(ascending=False)
bars = plt.bar(dept_counts.index, dept_counts.values, 
               color=sns.color_palette("Set2", len(dept_counts)),
               edgecolor='black', linewidth=1.2)

plt.title('Employee Distribution Across Departments', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Department', fontsize=13, fontweight='bold')
plt.ylabel('Number of Employees', fontsize=13, fontweight='bold')
plt.xticks(rotation=45, ha='right')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold')

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Convert plot to base64
buffer = BytesIO()
plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
buffer.seek(0)
image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
plt.close()

# Read this Python file to embed in HTML
with open(__file__, 'r') as f:
    python_code = f.read()

# Create HTML with embedded Python code
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Performance Analysis</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/github-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/python.min.js"></script>
    <script>hljs.highlightAll();</script>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }}
        .container {{
            background-color: white;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
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
            padding: 15px;
            border-radius: 5px;
            font-weight: bold;
            color: #2c3e50;
            margin: 20px 0;
            font-size: 16px;
        }}
        .highlight-box {{
            background-color: #fffbcc;
            padding: 20px;
            border-left: 5px solid #f39c12;
            margin: 20px 0;
            font-size: 20px;
            font-weight: bold;
            color: #e67e22;
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
        pre {{
            background-color: #1e1e1e;
            border-radius: 8px;
            padding: 20px;
            overflow-x: auto;
            margin: 20px 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }}
        code {{
            font-family: 'Courier New', Consolas, monospace;
            font-size: 14px;
            line-height: 1.5;
        }}
        .code-section {{
            background-color: #f8f9fa;
            border: 2px solid #dee2e6;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
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
            font-size: 36px;
            font-weight: bold;
            margin: 10px 0;
        }}
        .stat-label {{
            font-size: 14px;
            opacity: 0.9;
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
        }}
        td {{
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }}
        tr:hover {{
            background-color: #f5f5f5;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Employee Performance Analysis</h1>
        <p><strong>Company:</strong> Technology Company (Multi-Regional Operations)</p>
        <p><strong>Analysis Date:</strong> November 17, 2025</p>
        
        <div class="email">
            📧 Student Email: {student_email}
        </div>

        <h2>🎯 Key Finding: Sales Department Frequency Count</h2>
        <div class="highlight-box">
            Frequency count for 'Sales' department: {sales_count} employees
        </div>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-label">Total Employees</div>
                <div class="stat-value">{len(df)}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Total Departments</div>
                <div class="stat-value">{len(departments)}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Sales Employees</div>
                <div class="stat-value">{sales_count}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Sales Percentage</div>
                <div class="stat-value">{sales_count/len(df)*100:.1f}%</div>
            </div>
        </div>

        <h2>📊 Department Distribution Histogram</h2>
        <div class="chart-container">
            <img src="data:image/png;base64,{image_base64}" alt="Department Distribution Histogram">
            <p><em>Figure: Employee distribution across all departments using matplotlib histogram</em></p>
        </div>

        <h2>💻 Python Code Used for Analysis</h2>
        <div class="code-section">
            <p><strong>Below is the complete Python code used to generate this analysis:</strong></p>
            <pre>ode classss="language-python">{python_code}</code></pre>
        </div>

        <h2>📈 Analysis Summary</h2>
        <ul>
            <li><strong>Sales Department:</strong> {sales_count} employees ({sales_count/len(df)*100:.1f}% of total workforce)</li>
            <li><strong>Largest Department:</strong> {dept_counts.index[0]} with {dept_counts.values[0]} employees</li>
            <li><strong>Visualization Method:</strong> Histogram using matplotlib and seaborn</li>
            <li><strong>Data Generation:</strong> Synthetic dataset of 100 employees across 7 departments</li>
        </ul>

        <h2>🔍 Technical Details</h2>
        <p><strong>Libraries Used:</strong></p>
        <ul>
            <li>pandas - Data manipulation and analysis</li>
            <li>matplotlib - Plotting and visualization</li>
            <li>seaborn - Statistical visualization styling</li>
            <li>numpy - Numerical operations and random data generation</li>
        </ul>

        <p style="margin-top: 40px; padding-top: 20px; border-top: 2px solid #ecf0f1; text-align: center; color: #7f8c8d;">
            Generated by: {student_email} | Technology Company HR Analytics Division | 2025
        </p>
    </div>
</body>
</html>
"""

# Save HTML file
with open('employee_analysis.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ HTML report generated: employee_analysis.html")
print(f"✅ Sales department frequency count: {sales_count}")
print(f"✅ Histogram visualization embedded")
print(f"✅ Python code embedded with syntax highlighting")
