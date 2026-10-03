import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("all_products.csv")

# 2. Display first 5 rows
print("\n--- FIRST 5 ROWS ---")
print(df.head())

# 3. Dataset information
print("\n--- DATASET INFO ---")
print(df.info())

# 4. Count products by category
print("\n--- PRODUCTS BY CATEGORY ---")
print(df["category"].value_counts())

# 5. Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- RANDOM SAMPLE ---")
print(df.sample(5))

# 6. Overall average price
print("\n--- AVERAGE PRICE ---")
print(df["price_eur"].mean())

# 7. Average price by category
print("\n--- AVERAGE PRICE BY CATEGORY ---")
average_price = df.groupby("category")["price_eur"].mean()
print(average_price)

# 8. Cheapest products
print("\n--- 10 CHEAPEST PRODUCTS ---")
print(df.sort_values("price_eur").head(10)[["product_name", "category", "price_eur"]])

# 9. Most expensive products
print("\n--- 10 MOST EXPENSIVE PRODUCTS ---")
print(df.sort_values("price_eur", ascending=False).head(10)[["product_name", "category", "price_eur"]])

# 10. Bar chart: average price by category
average_price.plot(kind="bar")
plt.title("Average Price by Beverage Category")
plt.xlabel("Category")
plt.ylabel("Average Price (\u20ac)")
plt.tight_layout()
plt.savefig("avg_price_by_category.png")
plt.close()

# ---------------------------------------------------------
# NEW: extensions using only columns actually present
# ---------------------------------------------------------

# 11. Pie chart: share of products by category
category_counts = df["category"].value_counts()
plt.figure()
plt.pie(category_counts, labels=category_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Share of Products by Category")
plt.tight_layout()
plt.savefig("category_share_pie.png")
plt.close()

# 12. Extract liter volume from package_size so prices are comparable across pack sizes
df["volume_l"] = df["package_size"].str.extract(r"([\d.]+)").astype(float)
df["price_per_l"] = df["price_eur"] / df["volume_l"]

print("\n--- PRICE PER LITER BY CATEGORY (avg) ---")
price_per_l_avg = df.groupby("category")["price_per_l"].mean()
print(price_per_l_avg)

price_per_l_avg.plot(kind="bar", color="teal")
plt.title("Average Price per Liter by Category")
plt.xlabel("Category")
plt.ylabel("Price per Liter (\u20ac)")
plt.tight_layout()
plt.savefig("price_per_liter_by_category.png")
plt.close()

# 13. Deposit (Pfand) analysis - how much of the price is deposit, by category
df["deposit_share_pct"] = (df["deposit_eur"] / df["price_eur"]) * 100
print("\n--- AVERAGE DEPOSIT SHARE OF PRICE BY CATEGORY (%) ---")
print(df.groupby("category")["deposit_share_pct"].mean())

# 14. Alcohol vs non-alcohol price comparison
print("\n--- AVERAGE PRICE: ALCOHOLIC VS NON-ALCOHOLIC ---")
print(df.groupby("contains_alcohol")["price_eur"].mean())

# 15. Price distribution (histogram)
plt.figure()
df["price_eur"].plot(kind="hist", bins=15, edgecolor="black")
plt.title("Distribution of Product Prices")
plt.xlabel("Price (\u20ac)")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.close()

print("\nAll charts saved as PNG files in the current folder.")
