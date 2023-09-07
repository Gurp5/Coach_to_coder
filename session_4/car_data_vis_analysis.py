import pandas as pd 
import matplotlib.pyplot as plt

car_vis = pd.read_csv("vehicle_analysis_data.csv")

# # Extension: Using pandas and matplotlib , create the following:
# 1. A pie chart showing the distribution between fuel types. (You can use the model column to count occurances!)
# 2. A bar chart showing the average mileage for each model. (You need to research hpow can you calculate average using pandas!)

# Ex - Question 1

# fuel_dists = car_vis.groupby("fuel_Type")[["model"]].count().sort_values("model").reset_index()

# plt.pie(fuel_dists.model, labels=fuel_dists.fuel_Type, 
# autopct="%1.1f%%")
# plt.show()

# Ex - Question 2

average_mileage_by_model = car_vis.groupby("model")["mileage"].mean().reset_index()

# Sort the resulting DataFrame by average mileage in descending order
models_by_mileage = average_mileage_by_model.sort_values("mileage", ascending=False)

# Create a bar chart
plt.figure(figsize=(10, 6))  # Optional: Adjust the figure size
plt.bar(models_by_mileage["model"], models_by_mileage["mileage"], color="maroon", width=0.4)
plt.xlabel("Car Model")
plt.ylabel("Average Mileage")
plt.title("Car Models with Average Mileage")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()  # Adjust the layout
plt.show()