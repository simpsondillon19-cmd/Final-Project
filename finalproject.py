# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 15:28:33 2025

@author: simps
"""

# choice survival game- you can go either to the woods, river, castle or desert 



class Player:
    def __init__(self):
        self.health = 100

    def lose_health(self, amount):
        self.health -= amount
        print(f" You lost {amount} health! Current health: {self.health}")
        if self.health <= 0:
            print("You have died, You're terrible.")
            return True
        return False


class Room:
    def __init__(self, name, description, actions):
        self.name = name
        self.description = description
        self.actions = actions

    def enter(self):
        print(f"\n=== {self.name} ===")
        print(self.description)
        print("\nActions:")
        for i, action in enumerate(self.actions.keys(), start=1):
            print(f"{i}. {action}")

    def choose_action(self):
        while True:
            try:
                choice = int(input("\nChoose an action: "))
                if 1 <= choice <= len(self.actions):
                    action_name = list(self.actions.keys())[choice - 1]
                    return self.actions[action_name]
                else:
                    print(" Invalid number.")
            except ValueError:
                print(" Enter a number.")


def puzzle_math(player):
    print("\nPuzzle: Solve this to continue!")
    a, b = 10, 3
    answer = a * b
    guess = int(input(f"What is {a} x {b}? "))

    if guess == answer:
        print("Correct!")
        return True
    else:
        print("Wrong!")
        player.lose_health(100)
        return False


def create_rooms(player):
    return {
        "Woods": Room(
            "Woods",
            "You're stuck in the woods. What is the first thing you will do?",
            {
                "Start a fire": lambda: player.lose_health(100, "Bandits found you and killed you"),
                "Tame the horse": "river",
            },
        ),

        "river": Room(
            "Calamus River",
            "You reach a wide river guarded by a troll.",
            {
                "Solve the math problem to get past the troll": lambda: puzzle_math(player),
                "Go to the left to the castle": "castle",
                "Go to the right to the desert": "desert",
            },
        ),

        "castle": Room(
            "King Dillon Castle",
            "An old castle full of danger.",
            {
                "Search the room": lambda: player.lose_health(100, "A Dragon found you and ate you"),
                "Save the princess and head to the desert": "desert",
            },
        ),

        "desert": Room(
            "Sandhills Desert",
            "A burning desert stretches endlessly.",
            {
                "Ride a camel": "exit",
                "Ride a horse": lambda: player.lose_health(100, "Your horse ran out of gas and died of thirst"),
                "Turn around and go to the tundra": "tundra",
            },
        ),

        "tundra": Room(
            "Tundra of Frostbite",
            "Freezing cold winds whip across the land.",
            {
                "Go to the igloo": lambda: player.lose_health(100,"You froze to death"),
                "Try to go through the tundra to paradise": lambda: player.lose_health(100,"You froze to death"),
            },
        ),

        "exit": Room(
            "City in the Distance",
            "You see a city far ahead.",
            {
                "Go to the city": "victory",
            },
        ),
    }


def game():
    player = Player()
    rooms = create_rooms(player)

    # FIXED: start in Woods, not entrance
    current_room_key = "Woods"

    while True:
        if player.health <= 0:
            print("\n GAME OVER — You did not survive.")
            break

        room = rooms[current_room_key]
        room.enter()
        result = room.choose_action()

        # String = next room
        if isinstance(result, str):
            current_room_key = result

        # Function = run it
        elif callable(result):
            result()

            if player.health <= 0:
                print("\n GAME OVER — You did not survive.")
                break
            continue

        # Victory check
        if current_room_key == "victory":
            print("\nYou win! Nice job!")
            break


if __name__ == "__main__":
    game()

    
   
    