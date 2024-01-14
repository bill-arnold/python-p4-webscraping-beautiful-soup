# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Set user-agent in headers to avoid 403 Forbidden error (anti-bot measure)
headers = {'user-agent': 'my-app/0.0.1'}

# Specify the URL you want to scrape
url = "https://moringaschool.com/"

# Make an HTTP request to the URL and retrieve the HTML content
html = requests.get(url, headers=headers)

# Create a BeautifulSoup object to parse the HTML
doc = BeautifulSoup(html.text, 'html.parser')

# Example 1: Extracting text using CSS selectors
# Extract the text content of an element with class 'heading-financier'
elements = doc.select('.heading-financier')
if elements:
    heading_text = elements[0].contents[0].strip()
    print(f"Example 1: {heading_text}\n")
else:
    print("No elements found with the class 'heading-financier'.")


# Example 2: Iterating over elements and extracting text
# Extract the titles of all elements with classes 'heading-60-black', 'color-black', and 'mb-20'
courses = doc.select('.heading-60-black.color-black.mb-20')

print("Example 2:")
if courses:
    for course in courses:
        course_title = course.contents[0].strip()
        print(course_title)
else:
    print("No elements found with the classes 'heading-60-black', 'color-black', and 'mb-20'.")


# Example 3: Extracting tag name and attributes
# Extract the tag name and attributes of the first element with class 'heading-60-black'
first_course = doc.select('.heading-60-black')[0]
tag_name = first_course.name
attributes = first_course.attrs

print(f"\nExample 3:\nTag Name: {tag_name}\nAttributes: {attributes}")
