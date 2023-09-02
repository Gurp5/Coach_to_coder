import pandas as pd 
import matplotlib.pyplot as plt

bestsellers = pd.read_csv("bestsellers_british_book_price.csv")
bestsellers = bestsellers.drop_duplicates(subset="Name", keep="last")

# let's create a bar chart, showing the author with the most amount of best-selling titles in the given years

# then create a pie chart showing the distribution between fiction and the non-fiction books. 

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

number_books_genre = bestsellers.groupby("Genre")[["Name"]].count().sort_values("Name", ascending=False).reset_index()

plt.pie(number_books_genre.Name, labels=number_books_genre.Genre, 
autopct="%1.1f%%")
plt.show()