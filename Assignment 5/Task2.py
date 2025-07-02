list_num = [1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {list}")

five = list_num[:5]
print(f"Extracted first five elements: {five}")

reversed_five = list(reversed(five))
print(f"Reversed extracted elements: {reversed_five}")
