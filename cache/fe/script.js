let currentRecipeId = 1;

function fetchRecipe(recipeId) {
    fetch(`http://127.0.0.1:5000/recipe/${recipeId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('recipeIdResult').textContent = data.id;
            document.getElementById('recipeName').textContent = data.name;
            document.getElementById('recipeDescription').textContent = data.description;

            // Zobrazit ingredience
            const ingredientsList = document.getElementById('recipeIngredients');
            ingredientsList.innerHTML = ''; // Vymazat stávající ingredience
            data.ingredients.forEach(ingredient => {
                const li = document.createElement('li');
                li.textContent = `${ingredient[0]}: ${ingredient[1]}`;
                ingredientsList.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error fetching the recipe:', error);
        });
}

function changeRecipe(direction) {
    currentRecipeId = ((currentRecipeId + direction) % 4);
    if (currentRecipeId === 0) currentRecipeId = 1; // Aby se vyhnul ID 0
    document.getElementById('recipeId').textContent = currentRecipeId;
    fetchRecipe(currentRecipeId);
}

// Fetch the initial recipe
fetchRecipe(currentRecipeId);
