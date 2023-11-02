from database_connector import get_pg_connection
from database_connector import get_redis_connection
import json

def get_recipe(recipe_id):
    # Try get recipe from cache
    recipe = redis_conn.get(f"recipe:{recipe_id}")

    if recipe:
        print("return recipe from cache")
        return json.loads(recipe)

    # If recipe is not in cache, query it from postgresql database
    conn = get_pg_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes WHERE id = %s", (recipe_id,))
    recipe = cursor.fetchone()
    cursor.close()
    conn.close()
    # save recipe into cache for later usage
    redis_conn.setex(f"recipe:{recipe_id}", 3600, json.dumps(recipe))
    return recipe

if __name__ == '__main__':
    redis_conn = get_redis_connection()
    recipe = get_recipe(1)
    print(recipe)