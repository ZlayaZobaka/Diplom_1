class DefaultIngredients:
    BUNS_NAMES = ['black bun', 'white bun', 'red bun']
    BUNS_PRICES = [100, 200, 300]
    INGREDIENTS_TYPES = {'SAUCE', 'FILLING'}
    INGREDIENTS_NAMES = ['hot sauce', 'sour cream', 'chili sauce', 'cutlet', 'dinosaur', 'sausage']
    INGREDIENTS_PRICES = {100, 200, 300}


class Recipes:
    RECIPE_1 = {
        'bun': ['test bun', 20],
        'ingredients': [
            ['test sauce', 'sauce', 10],
            ['test meat', 'meat', 50],
            ['test vegetables', 'vegetables', 30]
        ],
        'text': ('(==== test bun ====)\n= test sauce sauce =\n= test meat meat ='
                 '\n= test vegetables vegetables =\n(==== test bun ====)\n\nPrice: 130')
    }

    RECIPE_2 = {
        'bun': ['rye bread', 42],
        'ingredients': [
            ['mayonnaise', 'sauce', 23],
            ['ostankino sausage', 'meat', 32],
            ['gherkins', 'vegetables', 11]
        ],
        'text': ('(==== rye bread ====)\n= mayonnaise sauce =\n= ostankino sausage meat ='
                 '\n= gherkins vegetables =\n(==== rye bread ====)\n\nPrice: 150')
    }
