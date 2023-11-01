from database_connector import get_pg_connection

conn = get_pg_connection()
cursor = conn.cursor()

# Sample data for the recipes table
recipes_data = [
    ("Beef Stroganoff", "A classic Russian dish of sautéed pieces of beef served in a sauce with smetana (sour cream)."),
    ("Goulash", "A traditional Hungarian dish of stewed meat, seasoned with paprika and other spices."),
    ("Tomato Sauce with Ground Beef", "A simple tomato sauce with ground beef, perfect for pasta.")
]

# Inserting data into the recipes table
for recipe in recipes_data:
    cursor.execute("INSERT INTO recipes (name, description) VALUES (%s, %s)", recipe)

# Sample data for the ingredients table
ingredients_data = [
    ("Beef", "500g", 1),
    ("Sour cream", "200ml", 1),
    ("Onions", "2 pcs", 2),
    ("Paprika", "1 teaspoon", 2),
    ("Beef", "500g", 2),
    ("Tomatoes", "5 pcs", 3),
    ("Ground beef", "300g", 3)
]

# Inserting data into the ingredients table
for ingredient in ingredients_data:
    cursor.execute("INSERT INTO ingredients (name, quantity, recipe_id) VALUES (%s, %s, %s)", ingredient)

conn.commit()
cursor.close()
conn.close()