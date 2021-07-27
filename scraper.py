import requests
import lxml.html

# Obtaning the content from the website
html = requests.get("https://store.steampowered.com/explore/new/")
doc = lxml.html.fromstring(html.content)

# Finding the div where the new releases are
new_releases = doc.xpath("//div[@id='tab_newreleases_content']")[0]

# Finding the new releases titles and prices
titles = new_releases.xpath(".//div[@class='tab_item_name']/text()")
prices = new_releases.xpath(".//div[@class='discount_final_price']/text()")

# Extracting the tags
# # As a game has multiple tags, we have to extract the divs first
# tags_divs = new_releases.xpath(".//div[@class='tab_item_top_tags']")

# # Each game´s tags is gonna be saved in a list 
# tags = []

# for div in tags_divs:
#     tags.append(div.text_content())

# A pythonic way to do the above procedure
tags = [[tag.text_content()] 
        for tag in new_releases.xpath(".//div[@class='tab_item_top_tags']")]


# Extracting the platform where each game is avaliable
platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)

# Making a a list with all the information together
output = []
for info in zip(titles, prices, tags, total_platforms):
    resp = {}
    resp["title"] = info[0]
    resp["price"] = info[1]
    resp["tags"] = info[2]
    resp["platforms"] = info[3]
    output.append(resp)

print(output)