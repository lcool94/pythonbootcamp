import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(fun=player.up, key="Up")
screen.onkeypress(fun=player.down, key="Down")

game_is_on = True


# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     car_manager.create_car()
#     car_manager.move()
#     for car in car_manager.cars:
#         if car.distance(player) < 20:
#             print("Game Over")
#             game_is_on = False
#         if player.is_goal():
#             player.go_to_start()
#             car_manager.level_up()
def game_loop():
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            print("Game Over")
            screen.bye()
        if player.is_goal():
            player.go_to_start()
            car_manager.level_up()
    screen.ontimer(game_loop, 100)


game_loop()
screen.exitonclick()
