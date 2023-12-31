import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

url = "https://www.amazon.com/KitchenAid-Cream-Maker-Stand-Attachment/dp/B09Q6YX6CW?ref_=Oct_DLandingS_D_688f6870_3"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)


# title = soup.find(id="productTitle").get_text().strip()
# print(title)
#
# BUY_PRICE = 200
#
# if price_as_float < BUY_PRICE:
#     message = f"{title} is now {price}"
#
#     with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
#         connection.starttls()
#         result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
#         connection.sendmail(
#             from_addr=YOUR_EMAIL,
#             to_addrs=YOUR_EMAIL,
#             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
#         )




#
# from bs4 import BeautifulSoup
# import requests
#
#
# desired_date = input("What date would you like to go back to? Type date in this format: YYYY-MM-DD ")
#
# response = requests.get(f"https://www.billboard.com/charts/hot-100/{desired_date}")
# music_data = response.text
#
# soup = BeautifulSoup(music_data,"html.parser")
# songs = soup.select("li ul li h3")
# songs_titles = [song.getText().strip() for song in songs]
# print(songs_titles)
# for song in songs_titles:
#     print(song)
#
# # contents = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# # yc_webpage = contents.text
# # soup = BeautifulSoup(yc_webpage, "html.parser")
# # data = soup.find_all(name="h3", class_="title")
# # article_tag =[]
# # for article in data:
# #  article_tag.append(article.getText())
# # #
# # if article_tag is not None:
# #  print(f"Article Text: {article_tag}")
# # # article_text = article_tag.get_text()
# # #     article_link = article_tag["href"]
# # #
# # #     print(f"Article Link: {article_link}")
# # #
# # #
# # else:
# #     print("No article found with the specified criteria.")
# #
# #
# # # with open("website.html", "r", encoding='utf-8') as file:
# # #     contents = file.read()
# # #
# # # soup = BeautifulSoup(contents, "html.parser")
# # # print(soup.prettify())
# #
# # def search_string_in_list(search_string, string_list):
# #     # Initialize an empty list to store indices where the search string is found
# #     indices_found = []
# #
# #     # Iterate through the list of strings
# #     for index, string in enumerate(string_list):
# #         # Check if the search string is present in the current string
# #         if search_string in string:
# #             indices_found.append(index)
# #
# #     return indices_found
# #
# # # Example usage
# #
# # search_term = "1"
# #
# # result_indices = search_string_in_list(search_term, article_tag)
# #
# # for result_index in result_indices:
# #     print(article_tag[result_index])
# #
