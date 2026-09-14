from product_data import products


# Step 1 - Print the products to examine the data.
for product in products:
    print(product)


# Step 2 - Collect the customer's preferences in a list.
customer_preferences = []

response = ""
while response != "N":
    preference = input("\nInput a preference: ").strip().lower()

    if preference != "":
        customer_preferences.append(preference)

    response = input(
        "Do you want to add another preference? (Y/N): "
    ).strip().upper()


# Step 3 - Convert the preference list to a set.
# This removes duplicate preferences.
customer_preferences = set(customer_preferences)


# Step 4 - Convert each product's tags to a set.
converted_products = []

for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }

    converted_products.append(converted_product)


# Step 5 - Calculate the number of matching tags.
def count_matches(product_tags, customer_tags):
    matching_tags = product_tags.intersection(customer_tags)
    return len(matching_tags)


# Step 6 - Find and sort the matching products.
def recommend_products(products, customer_tags):
    recommendations = []

    for product in products:
        number_of_matches = count_matches(
            product["tags"],
            customer_tags
        )

        if number_of_matches > 0:
            # The number is stored first so Python can sort by it.
            recommendations.append(
                [number_of_matches, product["name"]]
            )

    recommendations.sort(reverse=True)

    return recommendations


# Step 7 - Call the function and print the results.
recommendations = recommend_products(
    converted_products,
    customer_preferences
)

print("\nRecommended products:")

if len(recommendations) == 0:
    print("No matching products were found.")
else:
    for recommendation in recommendations:
        match_count = recommendation[0]
        product_name = recommendation[1]

        print(f"- {product_name} ({match_count} match(es))")


# DESIGN MEMO:
# 1. The program uses lists to collect and store data. It converts the
#    tags to sets so that intersection() can efficiently find tags that
#    the product and customer have in common. Loops process the products.

# Ideas to look for
#   A list collects the customer’s input.
#   Converting the list to a set removes duplicates.
#   Product tags are converted to sets.
#   Set intersection finds tags appearing in both sets.
#   len() counts the matching tags.
#   A loop examines each product.
#   A list accumulates the recommendations.
#   .sort() ranks the results.
#   Functions separate the matching and recommendation tasks.

# ******  A strong response should explain at least one important design choice, such as:

# ******  Sets were used because intersection makes it easy to find shared tags.

# ******   A response that merely lists operations without explaining why they were used demonstrates less understanding.
#
# 2. With 1000+ products, the same solution would still work. Sets make
#    the tag comparisons faster than searching through lists. For a much
#    larger catalog, the products could be organized by tag so the program
#    would not need to examine every product.

# Ideas to look for
#   The current program would still work with 1,000 products.
#   More products would require more comparisons and therefore more time.
#   The program currently loops through every product.
#   Sets continue to make tag comparisons efficient.
#   Products could be loaded from a file or database instead of being written directly in the program.
#   Products could be indexed or organized by tag.
#   An index would allow the program to examine only relevant products.
#   The program might return only the highest-ranked results rather than displaying every match.

# ****  I would not expect beginners to propose a complete database or indexing design. A perfectly acceptable response might simply be:

# ****  With 1,000 products, the program would take longer because it must check every product. Sets would still help make the tag comparisons faster.

# ****  That demonstrates the essential insight the question is likely assessing.