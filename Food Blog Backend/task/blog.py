import sqlite3

database = r'C:\Python\Projects\Food Blog Backend\Food Blog Backend\task\food_blog.db'

conn = sqlite3.connect(database)
c = conn.cursor()

result = c.execute('''CREATE TABLE if not exists meals (meal_id integer PRIMARY KEY, 
                                        meal_name VARCHAR (20) NOT NULL UNIQUE);''')

c.execute('''DELETE FROM meals''')
c.execute('''CREATE TABLE if not exists ingredients (ingredient_id integer PRIMARY KEY, 
                                                         ingredient_name VARCHAR (20) NOT NULL UNIQUE);''')
c.execute('''DELETE FROM ingredients''')
c.execute('''CREATE TABLE if not exists measures (measure_id integer PRIMARY KEY, 
                                                      measure_name VARCHAR (40) UNIQUE);''')

c.execute('''DELETE FROM measures''')
c.execute('''CREATE TABLE  if not exists recipes(recipe_id int PRIMARY KEY,
                                                 recipe_name VARCHAR(20) NOT NULL,
                                                 recipe_description VARCHAR(50));''')
c.execute('''DELETE FROM recipes''')

c.execute('''PRAGMA foreign_keys = ON;''')

c.execute('''CREATE TABLE if not exists serve(
             serve_id INTEGER PRIMARY KEY,
             recipe_id INTEGER NOT NULL,
             meal_id INTEGER NOT NULL,
             FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id),
             FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
             )''')

conn.commit()


data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
        "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
        "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}


for table in data:
    for row in data[table]:
        c.execute(f"""INSERT INTO {table} ({table[:-1]}_name) Values ('{row}')""")

conn.commit()


print('Pass the empty recipe name to exit.')

n = 0
while True:
    name = input('Meal name?')
    if name == '':
        break
    else:
        description = input('Recipe description')
        new_recipe_id = c.execute(f"""INSERT INTO recipes (recipe_name, recipe_description)
                                      VALUES ('{name}', '{description}')
                                   """).lastrowid
        conn.commit()

        c.execute(f"""SELECT meal_id, meal_name FROM meals
                        """)
        meals = c.fetchall()
        conn.commit()

        for meal in meals:
            print(f"{meal[0]}) {meal[1]}", end=" ") # print('1) breakfast  2) brunch  3) lunch  4) supper')

        when = input("\nWhen the dish can be served: ").split()

        for w in when:
            c.execute(f"""INSERT INTO serve (recipe_id, meal_id)
                               VALUES ('{new_recipe_id}', '{w}')
                               """)
        conn.commit()

conn.close()
