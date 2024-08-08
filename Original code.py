import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'Country': ['Country A', 'Country B', 'Country C', 'Country D', 'Country E'],
    'SDG 4 Score': [75, 80, 65, 90, 85]  # Example scores for SDG 4
}

df = pd.DataFrame(data)
# Set the style of seaborn
sns.set(style="whitegrid")

# Create a barplot
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='SDG 4 Score', data=df, palette='Blues_d')

# Adding title and labels
plt.title('Progress towards SDG 4 - Quality Education', fontsize=16)
plt.xlabel('Country', fontsize=14)
plt.ylabel('SDG 4 Score', fontsize=14)

# Display the plot
plt.show()