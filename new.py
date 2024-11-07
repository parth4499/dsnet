from bs4 import BeautifulSoup

with open('New Account Number List.html', 'r', encoding='utf-8') as file:
    html = file.read()


soup = BeautifulSoup(html, 'html.parser')

a_element = soup.find('a', class_='gage-link')

# Extract the text (value) of the <a> element
value = a_element.text

# Print the extracted value
print(value)
