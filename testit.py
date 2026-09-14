from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

i = 0
for product in products:
    print(f"Product {i + 1}: {product}")
    i += 1

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    customer_preferences.append(preference)
    print(f"Your preference list includes: {customer_preferences}")

    response = input("Do you want to add another preference? (Y/N): ").upper()
  
# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
set_preferences = set(customer_preferences) #Elimates duplicates from the list and converts it to a set.
print(f"Set preferences: {set_preferences}")

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    user_entry = {'name': product['name'], 'tags': set(product['tags'])}
    #if product in customer_preferences: #If the product is in the customer preference, add it to the user entry list.
    converted_products.append(user_entry)

print(converted_products)

# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    count = 0

    print("in step 5")
    print( customer_tags)
    for product in product_tags:
        print(product)
        if product in customer_tags:
            print("Found a match...")
            count+=1

    return count

# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_preferences):
    reccomendations = []
    for product in products:
        print("in step 6")
        print( product)
        count_of_matches = count_matches( product["tags"], customer_preferences)
        if count_of_matches > 0:
            print("Reccomended Products:\n")
            print(f"-{{'name': '{product['name']}', 'matches': {count_of_matches}}}\n")
            #return reccomendations

       
        
    if len(reccomendations)== 0:
        return "No products match your preferences."
    
    #Args:
        #products (list): A list of product dictionaries.
        #customer_tags (set): A set of tags associated with the customer.
    #Returns:
        #list: A list of products containing product names and their match counts.
    


# TODO: Step 7 - Call your function and print the results
recommend_products(converted_products, set_preferences)



# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?