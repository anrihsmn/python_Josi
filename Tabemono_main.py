
from Tabemono import Food

food_data = Food()

food_data.set_food_name("Okonomiyaki")
food_data.set_food_price("100")
food_data.set_serve_time(200)

print(food_data.get_food_name(),food_data.get_food_price(),food_data.get_serve_time())