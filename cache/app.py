from flask import Flask, jsonify
from flask_cors import CORS

from database_connector import get_pg_connection
from database_connector import get_redis_connection

import json

app = Flask(__name__)
CORS(app)

@app.route('/recipe/<int:recipe_id>')
def get_recipe(recipe_id):
    # Try get recipe from cache
    redis_conn = get_redis_connection()
    cached_data = redis_conn.get(f"recipe:{recipe_id}")

    if cached_data:
        return json.loads(cached_data)

    # If recipe is not in cache, query it from postgresql database
    conn = get_pg_connection()
    cursor = conn.cursor()

    # Get recipes
    cursor.execute("SELECT * FROM recipes WHERE id = %s", (recipe_id,))
    recipe_tuple = cursor.fetchone()
    recipe_dict = {
        "id": recipe_tuple[0],
        "name": recipe_tuple[1],
        "description": recipe_tuple[2]
    }

    # Get ingredients
    cursor.execute("SELECT name, quantity FROM ingredients WHERE recipe_id = %s", (recipe_id,))
    ingredients = cursor.fetchall()

    # Add ingredients to recipe
    recipe_dict["ingredients"] = ingredients
    print(ingredients)

    cursor.close()
    conn.close()

    # Save recipe into cache for later usage
    redis_conn.setex(f"recipe:{recipe_id}", 3600, json.dumps(recipe_dict))

    return jsonify(recipe_dict)



if __name__ == '__main__':
    app.run(debug=True)
