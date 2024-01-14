# Trendyol Shopping Analysis 🛍️📊

## Motivation 💡
Shopping has always been a significant part of my life, and after the COVID-19 pandemic restrictions limited in-person shopping, I transitioned to online shopping. Trendyol became my go-to platform for online purchases. This project aims to analyze my Trendyol shopping history, exploring patterns, preferences, and insights gained from the data.

## Data Source 📦
As Trendyol does not provide a default data export tool, I had to extract my own data. I wrote a script (`script.py`) using the Selenium library because the website was dynamically loaded. I extracted product links via this script. These links were saved to `hrefs.txt`. The subsequent script (`obtain.py`) which I wrote too opened each link, extracted product information from the HTML, and saved it to a JSON file.

## Data Analysis 📊
- **Exploratory Data Analysis (EDA):** Initial exploration included checking for null values and examining the data's structure and more.
- **Visualization:** Various visualization techniques were applied, focusing on personal interests. Additionally, a linear regression machine learning model was implemented to predict product ratings based on purchasing patterns.

## Findings 🚀
- **Qualification of Purchases:** Identified the quality of purchases based on user ratings.
- **Preferred Category:** Discovered that clothing was the most frequently purchased category.
- **Spending Patterns:** Analyzed the amount of money spent on products.
- **Preferred Brand:** Trendyol Milla emerged as the most frequently purchased brand.

## Limitations ⚠️
- **Learning Curve:** Due to limited prior experience with web scraping, a significant amount of time was spent learning through trial and error.
- **Manual Data Merge:** Information from the product pages had to be manually merged with the purchase data from the history page, as the latter lacked comprehensive details.

## Future Work 🚀
While the current scope of the project is limited, potential future enhancements include:
- Expanding the dataset by continuing to track purchases in different categories.
- Exploring and applying additional machine learning models.
