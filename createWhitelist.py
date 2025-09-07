'''
open entire theme list
open blacklist
remove blacklist items from entire list
write new list to cleanedThemedList.txt
'''


# get all theme urls from pageNames.txt
all_url_list = []
page_names_file_string = "pageNames.txt"
page_names_file = open(page_names_file_string, "r")

# use the blacklist to filter out bad theme urls
page_blacklist_file_string = "pageNamesBlacklistCleaned.txt"
page_blacklist_file = open(page_blacklist_file_string, "r")

# 2 arrays: 1 of all the themes, 1 of the blacklisted themes
all_url_list = page_names_file.read().split("\n")
url_blacklist = page_blacklist_file.read().split("\n")

url_whitelist = []

# removes all identical themes from blacklist from the theme array
# i.e. clean the theme array
def clean_theme_array():
  for url in all_url_list:
    if url not in url_blacklist:
      url_whitelist.append(url)


#puts the new, cleaned theme_url_list to cleanedThemedList.txt 
def write_to_cleaned_list():
  with open("whitelist.txt", "w") as f:
    for url in url_whitelist:
      f.write(url + "\n")


# turn the everything list array into the whitelist array
clean_theme_array()

# write the whitelist to the file
write_to_cleaned_list()