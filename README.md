# Steam web scrapping with lxml

### Creating a virtual enviroment
- `python -m venv myenv`

### Instaling the packages
```python
pip install requests
pip install lxml
```

### Explaning the xpath() function
`new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]`
- `//` - indicates that we want to search in all the tags in our HTML document.
- `div` - indicated that we are looking for divs in our HTML.
- `[@id="div_id"]` - indicates to lxml what id we are looking for.

`titles = new_releases.xpath(".//div[@class='tab_item_name']/text()")`
- `.` - indicates that we are looking for only children of new_releases
- `[@class="class_name"]` - indicates that we are filtering classes based on his name
- `/text()` - indicates that we only want the text contained in the specified class

`temp = game.xpath('.//span[contains(@class, "platform_img")]')`
- `[contains(@class,"platform_img")]` - indicates that we are looking for a element that has the specified class, but it could has more aditional classes

##### These proyect is completely based on the [Yasoob Khalid´s youtube tutorial](https://www.youtube.com/watch?v=5N066ISH8og&t=222s&ab_channel=YasoobKhalid). I just added the pandas dataframe creation
