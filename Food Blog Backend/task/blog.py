import sqlite3

database = r'C:\Python\Projects\Food Blog Backend\Food Blog Backend\task\food_blog.db'

conn = sqlite3.connect(database)
cursor_1 = conn.cursor()

result = cursor_1.execute('''CREATE TABLE meals (meal_id integer PRIMARY KEY, 
                                        meal_name VARCHAR (20) NOT NULL UNIQUE);''')

result_2 = cursor_1.execute('''CREATE TABLE ingredients (ingredient_id integer PRIMARY KEY, 
                                                         ingredient_name VARCHAR (20) NOT NULL UNIQUE);''')

result_3 = cursor_1.execute('''CREATE TABLE measures (measure_id integer PRIMARY KEY, 
                                                      measure_name VARCHAR (40) UNIQUE);''')

result_4 = cursor_1.execute('''INSERT INTO meals VALUES (1, 'breakfast'), 
                                                        (2, 'brunch'),
                                                        (3, 'lunch'),
                                                        (4, 'supper')''')


result_5 = cursor_1.execute('''INSERT INTO ingredients VALUES   (1, 'milk'), 
                                                                (2, 'cacao'),
                                                                (3, 'strawberry'),
                                                                (4, 'blueberry'),
                                                                (5, 'blackberry'),
                                                                (6, 'sugar')''')


result_6 = cursor_1.execute('''INSERT INTO measures (measure_id, measure_name) VALUES  (1,'ml'), 
                                                            (2,'g'),
                                                            (3,'l'),
                                                            (4,'cup'),
                                                            (5,'tbsp'),
                                                            (6,'tsp'),
                                                            (7,'dsp'),
                                                            (8,'')''')
conn.commit()

result_7 = cursor_1.execute('''CREATE TABLE recipes(recipe_id int PRIMARY KEY,
                                                    recipe_name VARCHAR(20) NOT NULL,
                                                    recipe_description VARCHAR(50));''')

ask_on = True
n = 0
while ask_on:
    recipe_n = input('What is meal name?')
    if not recipe_n:
        ask_on = False
        continue
    cooking_directions = input('What is cooking directions?')
    sql = '''INSERT INTO recipes VALUES (?,?,?)'''
    n += 1
    result_8 = cursor_1.execute(sql, (n, recipe_n, cooking_directions))



conn.commit()
conn.close()
