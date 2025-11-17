# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib",
#     "numpy",
#     "pandas",
#     "seaborn",
# ]
# ///
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic data for customer support response times
# Different channels have different response time characteristics

# Email: Slower response times (mean ~120 minutes, higher variance)
email_times = np.random.gamma(shape=2.5, scale=48, size=300)

# Chat: Fast response times (mean ~15 minutes, moderate variance)
chat_times = np.random.gamma(shape=3, scale=5, size=350)

# Phone: Very fast response times (mean ~5 minutes, low variance)
phone_times = np.random.gamma(shape=4, scale=1.25, size=280)

# Social Media: Medium response times (mean ~45 minutes, high variance)
social_times = np.random.gamma(shape=2, scale=22.5, size=270)

# Create DataFrame
data = pd.DataFrame({
    'Channel': ['Email'] * len(email_times) + 
               ['Chat'] * len(chat_times) + 
               ['Phone'] * len(phone_times) +
               ['Social Media'] * len(social_times),
    'Response Time (minutes)': np.concatenate([email_times, chat_times, phone_times, social_times])
})

# Set professional styling
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.0)

# Create figure with 8x8 inch size for 512x512 output at 64 DPI
fig, ax = plt.subplots(figsize=(8, 8))

# Create violinplot with professional styling
sns.violinplot(
    data=data,
    x='Channel',
    y='Response Time (minutes)',
    palette='Set2',
    inner='box',
    linewidth=1.5,
    ax=ax
)

# Customize the plot
ax.set_title('Customer Support Response Time Distribution\nby Support Channel', 
             fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Support Channel', fontsize=11, fontweight='bold')
ax.set_ylabel('Response Time (minutes)', fontsize=11, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=0, ha='center')

# Add grid for better readability
ax.yaxis.grid(True, alpha=0.3)
ax.set_axisbelow(True)

# Adjust layout to prevent label cutoff but maintain size
plt.subplots_adjust(left=0.12, right=0.95, top=0.92, bottom=0.10)

# Save the chart as PNG with exactly 512x512 pixels
# Remove bbox_inches='tight' to maintain exact dimensions
plt.savefig('chart.png', dpi=64)
print("Chart saved successfully as chart.png (512x512 pixels)")

# Verify the image size
from PIL import Image
img = Image.open('chart.png')
print(f"Image dimensions: {img.size[0]}x{img.size[1]} pixels")

plt.close()
