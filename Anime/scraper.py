# scrap https://myanimelist.net/users.php for usernames

import os  # for file and directory
import requests
from bs4 import BeautifulSoup  # parse html

URL = "https://myanimelist.net/users.php"
""" 
    The page we are scraping only contains 20 users at a time.
    So, we need to scrap the website every second to get new users.
    We will save the usernames that we have scrapped in a text file.
"""
USER_PER_PAGE = 20
USERNAME_NEEDED = 20000
USERNAME_FILENAME = "MAL_info/usernames.txt"
current_usernames_count = 0

if not os.path.exists(USERNAME_FILENAME):
    f = open(USERNAME_FILENAME, 'w')
    f.close()

# get the length of the current usernames that we have collected in the past
with open(USERNAME_FILENAME, 'r') as f:
    content = f.read()
    current_usernames_count = len(content.split('\n')) - 1

print(f"Current number of usernames = {current_usernames_count}")

with open(USERNAME_FILENAME, 'a') as f:
    usernames = []

    for i in range(current_usernames_count, USERNAME_NEEDED, USER_PER_PAGE):
        try:
            # get the html content
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")

            # the usernames are stored in a table and in links
            table_result = soup.find("table")
            links_result = table_result.find_all("a")

            for link in links_result:
                if not link.find_all():
                    # only get the username
                    # since the user profile image contains a child element, but the username doesn't
                    usernames.append(link.text.strip())
            print("Total usernames scrapped:", len(usernames))
        except Exception as e:
            print("An error has occured while scrapping!")
            print(e)

    print("Scrapping stopped")

    # save usernames to file
    for username in usernames:
        f.write(username + "\n")
    print(f"{len(usernames)} usernames saved")

unique_usernames = None
# remove duplicate usernames if any
with open(USERNAME_FILENAME, 'r') as f:
    content = f.read()
    unique_usernames = set(content.split('\n'))
    try:
        # remove empty usernames
        unique_usernames.remove('')
    except KeyError:
        pass
    print("Number of unique usernames:", len(unique_usernames))

with open(USERNAME_FILENAME, 'w') as f:
    for username in unique_usernames:
        f.write(f"{username}\n")