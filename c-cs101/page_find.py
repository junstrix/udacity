# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
start = page[start_link:].find("http://")
end = page[start_link:].find('">')
print page[start_link:][start:end]

# start_link = page.find('<a href=')
# start_quote = page.find('"',start_link)
# end_quote = page.find('"',start_link+1)
# print url=page[start_quote:end_quote]
