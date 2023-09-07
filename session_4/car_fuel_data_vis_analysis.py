import pandas as pd 
import matplotlib.pyplot as plt

fuel_dist_type = pd.read_csv("vw_fuel_dis.csv")


# let's create a bar chart, showing the author with the most amount of best-selling titles in the given years

# then create a pie chart showing the distribution between fiction and the non-fiction books. 



fuel_dists = fuel_dist_type.groupby("fuel_Type")[["model"]].count().sort_values("model").reset_index()



plt.pie(fuel_dists.model, labels=fuel_dists.fuel_type, 
autopct="%1.1f%%")
plt.show()