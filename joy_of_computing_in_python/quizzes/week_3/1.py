# Riya is building an Order Processing System for an online grocery store.
# She uses a Python list because it maintains order and allows items to be added, removed, or updated dynamically.

# 1. Creating the Order List (Initialization)
# At the start of the day, the system has some confirmed orders.
orders = ["Milk", "Bread", "Eggs"]
print(orders)
# How this works:
# [] creates a list
# Items are stored in order
# Indexing starts from 0
# Output:
# ['Milk', 'Bread', 'Eggs']

# 2. Adding a New Order at the End (append)
# A customer orders Butter, which must be added last. 
orders.append("Butter")
print(orders)
# How this works:
# append() adds one item at the end
# Existing order remains unchanged
# Output:
# ['Milk', 'Bread', 'Eggs', 'Butter']

# 3. Adding a Priority Order at a Specific Position (insert)
# A priority customer orders Fruits, which must come early.
orders.insert(1, "Fruits")
print(orders)
# How this works:
# insert(index, value) places the value at that index
# Elements from that position shift right
# Output:
# ['Milk', 'Fruits', 'Bread', 'Eggs', 'Butter']

# 4. Adding Multiple Orders Together (extend)
# A partner store sends additional orders.
partner_orders = ["Rice", "Oil"]
orders.extend(partner_orders)
print(orders)
# How this works:
# extend() adds elements one by one
# No nested list is created
# Output:
# ['Milk', 'Fruits', 'Bread', 'Eggs', 'Butter', 'Rice', 'Oil']

# 5. Accessing a Specific Order (Indexing)
# The system checks the first order received.
print(orders[0])
# How this works:
# Index 0 always refers to the first element
# Output:
# Milk

# 6. Processing Orders in Batches (Slicing)
# The packaging team processes the first three orders together.
batch_orders = orders[0:3]
print(batch_orders)
# How this works:
# Start index included 
# End index excluded 
# Creates a new list
# Output:
# ['Milk', 'Fruits', 'Bread']

# 7. Updating an Incorrect Order (Assignment)
# A customer ordered Milk but wanted Almond Milk.
orders[orders.index("Milk")] = "Almond Milk"
print(orders)
# How this works:
# index() finds the position of "Milk"
# Assignment replaces the value at that index
# Output:
# ['Almond Milk', 'Fruits', 'Bread', 'Eggs', 'Butter', 'Rice', 'Oil'] 

# 8. Removing a Cancelled Order by Name (remove)
# The Bread order is cancelled. 
orders.remove("Bread")
print(orders)
# How this works:
# remove() deletes the first matching element
# Remaining items shift lef
# Output:
# ['Almond Milk', 'Fruits', 'Eggs', 'Butter', 'Rice', 'Oil']

# 9. Sorting Orders Alphabetically (sort)
# For warehouse efficiency, orders are sorted.
orders.sort()
print(orders)
# How this works:
# sort() rearranges items alphabetically
# Sorting happens in-place
# Output:
# ['Almond Milk', 'Butter', 'Eggs', 'Fruits', 'Oil', 'Rice']

# 10. Clearing All Orders at End of Day (clear)
# After delivery, the system resets for the next day. 
orders.clear()
print(orders)
# How this works:
# Removes all elements
# List still exists but becomes empty
# Output:
# []


# What will be displayed after execution?
orders = ["Milk", "Bread", "Eggs"]
orders.append("Butter")
print(orders)
#  ['Milk', 'Bread', 'Eggs']
#  ['Butter', 'Milk', 'Bread', 'Eggs']
#  Error
#  ['Milk', 'Bread', 'Eggs', 'Butter']  (Right Answer)

# Which sequence is produced?
orders = ["Milk", "Bread", "Eggs"]
orders.insert(1, "Fruits")
print(orders)
#  ['Milk', 'Bread', 'Eggs', 'Fruits']
#  Error
#  ['Milk', 'Fruits', 'Bread', 'Eggs']   (Right Answer)
#  ['Fruits', 'Milk', 'Bread', 'Eggs']

# Which list is printed?
orders = ["Milk", "Bread", "Eggs"]
orders.extend(["Rice", "Oil"])
print(orders)
#  ['Milk', 'Bread', 'Eggs', ['Rice', 'Oil']]
#  Error
#  ['Rice', 'Oil', 'Milk', 'Bread', 'Eggs']
#  ['Milk', 'Bread', 'Eggs', 'Rice', 'Oil']   (Right Answer)

# Which value appears on the screen?
orders = ["Milk", "Bread", "Eggs"]
print(orders[0])
#  Error
#  Bread
#  Milk  (Right Answer)
#  Fruits

# Which option correctly represents the printed list?
orders = ["Milk", "Fruits", "Bread", "Eggs"]
print(orders[1:3])
#  ['Milk', 'Fruits']
#  ['Bread', 'Eggs']
#  ['Fruits', 'Bread', 'Eggs']
#  ['Fruits', 'Bread']   (Right Answer)

# After execution, which arrangement is obtained?
orders = ["Milk", "Bread", "Eggs"]
orders.append("Butter")
orders.sort()
print(orders)
#  ['Butter', 'Bread', 'Eggs', 'Milk']
#  ['Bread', 'Butter', 'Eggs', 'Milk']  (Right Answer)
#  Error
#  ['Milk', 'Bread', 'Eggs', 'Butter']

# What does the list finally contain?
orders = ["Milk", "Bread", "Eggs"]
orders.insert(1, "Fruits")
orders.remove("Bread")
print(orders)
#  ['Milk', 'Eggs']
#  Error
#  ['Fruits', 'Milk', 'Eggs']
#  ['Milk', 'Fruits', 'Eggs']   (Right Answer)

# Which elements are shown?
orders = ["Milk", "Bread"]
orders.extend(["Eggs", "Butter", "Rice"])
print(orders[1:4])
#  ['Bread', 'Eggs', 'Butter']   (Right Answer)
#  ['Eggs', 'Butter', 'Rice']
#  Error
#  ['Milk', 'Bread', 'Eggs']

# Which list is displayed?
orders = ["Milk", "Bread", "Eggs"]
orders[orders.index("Milk")] = "Almond Milk"
orders.sort()
print(orders)
#  ['Bread', 'Eggs', 'Almond Milk']
#  Error
#  ['Almond Milk', 'Bread', 'Eggs']   (Right Answer)
#  ['Milk', 'Bread', 'Eggs']

# Which option correctly matches the program behavior?
orders = ["Milk", "Bread", "Eggs"]
orders.insert(0, "Rice")
orders.sort()
print(orders[1:4])
#  ['Bread', 'Eggs']
#  ['Milk', 'Rice']
#  Error
#  ['Eggs', 'Milk']  (Right Answer)