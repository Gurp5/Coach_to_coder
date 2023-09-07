import pandas as pd 
import matplotlib.pyplot as plt

car_vis = pd.read_csv("vehicle_analysis_data.csv")

# # Extension: Using pandas and matplotlib , create the following:
# 1. A pie chart showing the distribution between fuel types. (You can use the model column to count occurances!)
# 2. A bar chart showing the average mileage for each model. (You need to research hpow can you calculate average using pandas!)

# Ex - Question 1

fuel_dists = car_vis.groupby("fuel_Type")[["model"]].count().sort_values("model").reset_index()

plt.pie(fuel_dists.model, labels=fuel_dists.fuel_Type, 
autopct="%1.1f%%")
plt.show()

# Ex - Question 2

number_bestsellers_written = bestsellers.groupby("Author")[["Name"]].count().sort_values("Name", ascending=False).head(10).reset_index()

# plt.bar(
# number_bestsellers_written.Author, 
# number_bestsellers_written.Name,
# color="maroon",
# width=0.4
# )
# plt.xlabel("Authors")
# plt.ylabel("Number of best selling books")
# plt.title("Mt first chart") 
# plt.show()

car_ave_miles = car_vis.groupby("fuel_Type")[["model"]].count().sort_values("model").reset_index()