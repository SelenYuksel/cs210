import json
import requests
from bs4 import BeautifulSoup
import time

def extract_data_from_link(link):
    try:
        response = requests.get(link)
        response.raise_for_status() 


        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').get_text().encode().decode('unicode_escape')
        category_span = soup.find('span', class_='product-detail-breadcrumb-item')
        category = category_span.get_text().encode().decode('unicode_escape') if category_span else None
        sender_span = soup.find('span', class_=  "product-description-market-place")
        sender = sender_span.get_text().encode().decode('unicode_escape') if sender_span else None
        price_span = soup.find('span', class_ = "prc-dsc")
        price = price_span.get_text().encode().decode('unicode_escape') if price_span else None
        rating_span = soup.find('div', class_ = "rating-line-count")
        rating = rating_span.get_text().encode().decode('unicode_escape') if rating_span else None
        data = {
            'title': title,
            'category' : category,
            'sender' : sender,
            'price' : price,
            'rating' : rating,
            'purchase_date' : "",
        }
        return data

    except requests.exceptions.HTTPError as e:
        print(f"Error processing link: {link}, Status Code: {e.response.status_code}")
        return None

def main():
    with open('hrefs.txt', 'r') as file:
        links = [line.strip() for line in file]
    extracted_data_list = []
    for link in links:
        extracted_data = extract_data_from_link(link)
        if extracted_data is not None:
            extracted_data_list.append(extracted_data)
            time.sleep(1)

    with open('extracted_data.json', 'w') as json_file:
        json.dump(extracted_data_list, json_file, indent=2)

if __name__ == "__main__":
    main()
