# Trendyol Shopping Analysis 🛍️📊

## Motivation 💡
Shopping has always been a significant part of my life, and after the COVID-19 pandemic restrictions limited in-person shopping, I found solace in the world of online shopping. Trendyol quickly became my go-to platform for all my online purchases. This project stems from a deep-seated curiosity to delve into the patterns, preferences, and insights embedded within my Trendyol shopping history.

## Data Source 📦
As Trendyol doesn't offer a default data export tool, I took matters into my own hands. I wrote a script (`script.py`) utilizing the Selenium library, crucial for navigating through the dynamically loaded website. This script was crafted to extract product links systematically, and these links were meticulously stored in `hrefs.txt`. The subsequent script (`obtain.py`), also my creation, traversed each link, gracefully plucking product information from the HTML, and neatly archiving it into a JSON file.

## Data Analysis 📊
- **Exploratory Data Analysis (EDA):** My journey with the data began with a thorough exploration. I meticulously checked for null values, scrutinized the data's structure, and conducted a comprehensive overview of various statistics.
- **Visualization:** Employing various visualization techniques, I unearthed insights aligned with my personal interests. The journey didn't stop there; a linear regression machine learning model was woven into the analysis, predicting product ratings based on purchasing patterns.

## Findings 🚀
- **Qualification of Purchases:** My exploration unveiled the intricate quality of my purchases, gauged through user ratings.
- **Preferred Category:** A notable revelation was the dominance of clothing as the most frequently purchased category.
- **Spending Patterns:** Diving deeper, I unraveled the monetary tapestry, understanding the financial investment in my product choices.
- **Preferred Brand:** The standout brand in my shopping escapades was Trendyol Milla, emerging as a consistent favorite.

## Limitations ⚠️
- **Learning Curve:** Navigating through the realms of web scraping presented a formidable learning curve. Hours were spent in the school of trial and error, forging a path through the complexities.
- **Manual Data Merge:** A significant challenge arose due to the limited information available in the purchase history page. This necessitated a manual merge of product details from individual pages, a meticulous task undertaken by hand.

## Future Work 🚀
While the current scope of the project is limited, the road ahead holds exciting possibilities. Future enhancements may include:
- Expanding the dataset by perpetuating the tracking of purchases across diverse categories.
- Venturing into the realm of diverse machine learning models, unraveling deeper insights from the evolving shopping journey.

