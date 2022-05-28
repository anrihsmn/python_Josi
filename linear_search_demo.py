
search_keyword = "Beach"

list_items = ["Clock","Book","Beach"]
item_found = False

for item in list_items:
  if item == search_keyword:
    item_found = True
    # item_found: false -> trueにしてbreakする
    break


if item_found:
  # if item_found: true -> match! 
  print("item found!")
else:
  print("Item not present.")
  # didnt match