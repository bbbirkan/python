"""
Description:

1. Open Google Chrome and go to the Chrome Web Store. You can search for the OneTab extension by typing "OneTab" in the search bar, or you can click on this link: https://chrome.google.com/webstore/detail/onetab/chphlpgkkbolifaimnlloiipkdnihall
2. On the OneTab extension's details page, click on the "Add to Chrome" button to download and install the extension.
3. After the extension has been installed, click on the extension icon in the top-right corner of the Chrome window.
4. In the drop-down menu, click on the "Pin" option to pin the OneTab extension to the Chrome toolbar.
5. Open a few web pages on new tabs to test the extension.
6. Click on the OneTab icon to see all the saved web pages, which will be organized in the left tab corner.
7. When you click on the extension icon in the left corner, you will see the "share as web page" section.
8. Copy the link from this section, as we will use it in the code.

"""

import requests
import re

def find_custom_webpages_links(custom_web_page_name,url):
  """
  Check the link and find oll links inside
  print filter web page name only
  """
  # make a GET request to the specified URL
  response = requests.get(url)
  # get the text of the response
  html = response.text
  # use a regular expression to find custom_web_page_name.com links in the response text
  link_check=r"https?://"+custom_web_page_name+"\.com[^\s]*"
  custom_web_page_name = re.findall(link_check, html)
  # create an empty list to store the corrected links
  custom_web_page_name_corrected = []
  # iterate over the links
  for link in custom_web_page_name:
    # skip any links that contain "size=32"
    if "size=32" in link:
      continue
    # remove the part of the link after the '">' characters
    link = link.split('">')[0]
    # add the corrected link to the list
    custom_web_page_name_corrected.append(link)
  # return the list of corrected links
  return custom_web_page_name_corrected
## test the function by passing it a URL
#custom_web_page_name = find_custom_webpages_links("medium","https://www.one-tab.com/page/JPF7z5dARfSzUgE43tS5TQ")
## print the links
# for i, link in enumerate(custom_web_page_name):
#   print(f"{i + 1}: {link}")
#*--------------------------------------------------------------------------------------------------------------*#
def find_all_links(url):
  # make a GET request to the specified URL
  response = requests.get(url)
  # get the text of the response
  html = response.text
  # use a regular expression to find all links in the response text
  all_links = re.findall(r"https?://[^\s]*", html)
  # create an empty list to store the corrected links
  all_links_corrected = []
  # iterate over the links
  for link in all_links:
    # skip any links that contain "size=32" or any of the other unwanted URLs
    if "size=32" in link or "http://www.w3.org" in link or "https://ssl" in link or "http://www" in link or "https://www.one-tab.com" in link:
      continue
    # remove the part of the link after the '">' characters
    link = link.split('">')[0]
    # add the corrected link to the list
    all_links_corrected.append(link)

  # return the list of corrected links
  return all_links_corrected

# test the function by passing it a URL
all_links = find_all_links("https://www.one-tab.com/page/bX_-XRTZRiGdsiRdHbhUxw")
# print the links
for i, link in enumerate(all_links):
  print(f"{i + 1}: {link}")
#*--------------------------------------------------------------------------------------------------------------*#
