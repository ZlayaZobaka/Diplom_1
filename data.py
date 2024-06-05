class Recipes:
    DEFAULT_DB = {
        'buns': [
            ['black bun', 100],
            ['white bun', 200],
            ['red bun', 300]
        ],
        'ingredients': [
            ['SAUCE', 'hot sauce', 100],
            ['SAUCE', 'sour cream', 200],
            ['SAUCE', 'chili sauce', 300],
            ['FILLING', "cutlet", 100],
            ['FILLING', "dinosaur", 200],
            ['FILLING', "sausage", 300],

        ]
    }

    RECIPE_1 = {
        'buns': [
            ['test bun', 20]
        ],
        'ingredients': [
            ['test sauce', 'sauce', 10],
            ['test meat', 'meat', 50],
            ['test vegetables', 'vegetables', 30]
        ],
        'text': ('(==== test bun ====)\n= test sauce sauce =\n= test meat meat ='
                 '\n= test vegetables vegetables =\n(==== test bun ====)\n\nPrice: 130')
    }

    RECIPE_2 = {
        'buns': [
            ['rye bread', 42]
        ],
        'ingredients': [
            ['mayonnaise', 'sauce', 23],
            ['ostankino sausage', 'meat', 32],
            ['gherkins', 'vegetables', 11]
        ],
        'text': ('(==== rye bread ====)\n= mayonnaise sauce =\n= ostankino sausage meat ='
                 '\n= gherkins vegetables =\n(==== rye bread ====)\n\nPrice: 150')
    }
