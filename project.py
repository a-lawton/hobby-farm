import cowsay
import getpass
import time
import random


class Farmer:
    def __init__(self, hearts=3):
        self._hearts = hearts
        self._max_hearts = hearts
        self._wheat = 0
        self._has_chickens = False
        self._eggs = 0
        self._has_cows = False
        self._milk = 0
        self._cheese = 0
        self._has_horses = False

    def update_hearts(self, n):
        if (self.hearts + n) < 0:
            raise ValueError("Too tired to do that today (not enough hearts)!")
        elif (self.hearts + n) > self.max_hearts:
            raise ValueError("Already at max hearts!")
        else:
            if n > 0:
                print(f"nom nom nom, hearts increased by {n}!")
            self._hearts += n

    def increase_max_hearts(self, n):
        self._max_hearts += n

    def sleep(self):
        print(
            "\nAll out of hearts, time to catch some z's\nZZZZzzzzz\n\n----------------------------------------------------------------------\n\n"
        )
        time.sleep(4)
        if random_event():
            self._hearts = self.max_hearts // 2
            print(
                "A terrible storm kept you up all night and you barely got a few hours of sleep...\nEven after 3 cups of coffee, you only have half the energy you'd normally have!\n\n----------------------------------------------------------------------\n\n"
            )
            time.sleep(3)
        else:
            self._hearts = self.max_hearts

        self.change_wheat(5)

    def change_wheat(self, amount):
        if self.wheat + amount < 0:
            raise ValueError("\nToo few wheat, can't do that!")
        else:
            self._wheat += amount

    def bake_bread(self):
        self.change_wheat(-10)
        self.update_hearts(1)

    def unlock_chickens(self):
        self.update_hearts(-1)
        self.change_wheat(-20)
        self._has_chickens = True
        cowsay.pig("\nYou now have Chickens!")

    def feed_chickens(self):
        self.update_hearts(-1)
        self.change_wheat(-2)
        self._eggs += 2

    def use_eggs(self, n):
        if self.eggs < n:
            raise ValueError("\nYou don't have enough eggs to do that!")
        else:
            self._eggs -= n

    def unlock_cows(self):
        self.update_hearts(-1)
        self.use_eggs(10)
        self._has_cows = True
        cowsay.cow("\nMOOOOOOOOO")

    def feed_cows(self):
        self.update_hearts(-1)
        self.change_wheat(-5)
        self._milk += 1

    def use_milk(self, n):
        if self.milk < n:
            raise ValueError("\nYou don't have enough milk to do that!")
        else:
            self._milk -= n

    def make_cheese(self):
        self.update_hearts(-1)
        self.use_milk(3)
        self._cheese += 1

    def unlock_horses(self):
        self.update_hearts(-1)
        self.use_eggs(10)
        self.use_milk(5)
        if self.cheese < 2:
            raise ValueError("\nYou don't have enough cheese to do that!")
        else:
            self._cheese -= 2

        self._has_horses = True
        self.hearts = 0

    @property
    def hearts(self):
        return self._hearts

    @hearts.setter
    def hearts(self, n):
        self._hearts = n

    @property
    def max_hearts(self):
        return self._max_hearts

    @property
    def wheat(self):
        return self._wheat

    @wheat.setter
    def wheat(self, n):
        self._wheat = n

    @property
    def has_chickens(self):
        return self._has_chickens

    @property
    def eggs(self):
        return self._eggs

    @eggs.setter
    def eggs(self, n):
        self._eggs = n

    @property
    def has_cows(self):
        return self._has_cows

    @property
    def milk(self):
        return self._milk

    @milk.setter
    def milk(self, n):
        self._milk = n

    @property
    def cheese(self):
        return self._cheese

    @property
    def has_horses(self):
        return self._has_horses


def main():
    farmer = Farmer()
    days = 0

    while True:
        if days == 0:
            cowsay.pig(
                f"Welcome, Hobby Farmer!\nThe goal of the game is to build a successful\n hobby farm. You win by unlocking all animals and taking your horse on a ride into the sunset.\nYou currently have {farmer.max_hearts} maximum hearts.\nThis represents the energy you can spend each day and resets after 8 hours of sleep.\nLet’s start the day by planting some wheat."
            )
            print(
                "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n----------------------------------------------------------------------"
            )
        else:
            print(f"Cockadoodledoo, time to rise and shine!\nDay: {days}\n")
            cowsay.pig(inventory(farmer))

        while farmer.hearts > 0:
            options = display_options(farmer)
            options_str = ""
            for i in range(len(options)):
                options_str += f"\n{i+1}. {options[i]['label']}"
            options_str += "\n"
            print("\nDaily To Do's:")
            try:
                selection = int(getpass.getpass(options_str))

                if selection < 1 or selection > len(options):
                    raise IndexError
                action = options[selection - 1]["key"]
                label = options[selection - 1]["label"]
                print(f'\nYou\'ve selected "{label}"!')
                print(select_options(farmer, action))
                print(
                    "\n\n----------------------------------------------------------------------"
                )
            except ValueError as e:
                print(
                    e,
                    "\n\n----------------------------------------------------------------------",
                )
                continue
            except IndexError:
                print(f"\nInvalid selection of {selection}, please try again!")

        days += 1

        if farmer.has_horses:
            time.sleep(2)
            cowsay.pig(
                f"\nAnd the day comes to an end as you ride off into the sunset... a true hobby farmer\n.....and it only took you {days} days!\n\n"
            )
            break
        else:
            if farmer.has_chickens and farmer.eggs > 0 and random_event():
                cowsay.fox(
                    "Uh oh, a fox got into your chicken coop and stole all your eggs!"
                )
                farmer.eggs = 0
                time.sleep(3)
            elif farmer.has_cows and farmer.milk > 0 and random_event():
                cowsay.cow("One of your cows had a baby!\nYour milk has doubled!")
                farmer.milk = farmer.milk * 2
            elif random_event():
                print(
                    "A locust swarm got into your wheat stores and ate all of your wheat!"
                )
                farmer.wheat = 0
                time.sleep(3)
            elif random_event():
                print(
                    "You're full of energy and crushing the farm life- maximum hearts has increased by 1!"
                )
                time.sleep(3)
                farmer.increase_max_hearts(1)

            farmer.sleep()


def display_options(farmer):
    options = []
    options.append({"key": "plant_wheat", "label": "Plant Wheat for 1 heart"})
    options.append({"key": "bake_bread", "label": "Bake Bread for 1 heart + 10 wheat"})

    if farmer.has_chickens:
        options.append(
            {"key": "feed_chickens", "label": "Feed Chickens for 1 heart + 2 wheat"}
        )
    else:
        options.append(
            {
                "key": "unlock_chickens",
                "label": "Unlock Chickens for 1 heart + 20 wheat",
            }
        )

    if farmer.has_cows:
        options.append({"key": "feed_cows", "label": "Feed Cows for 1 heart + 5 wheat"})
    else:
        options.append(
            {"key": "unlock_cows", "label": "Unlock Cows for 1 heart + 10 eggs"}
        )

    options.append({"key": "make_cheese", "label": "Make Cheese for 1 heart + 3 milk"})
    options.append(
        {
            "key": "unlock_horses",
            "label": "Unlock Horses for 1 heart + 10 eggs + 5 milk + 2 cheese",
        }
    )

    return options


def select_options(farmer, action):
    match action:
        case "plant_wheat":
            farmer.update_hearts(-1)
            farmer.change_wheat(10)
            return f"\nHearts Remaining: {farmer.hearts}\nWheat: {farmer.wheat}"
        case "bake_bread":
            if farmer.hearts > 0 and farmer.wheat >= 10:
                farmer.bake_bread()
                return f"\nHearts Remaining: {farmer.hearts}\nWheat: {farmer.wheat}"
            else:
                raise ValueError("...But you don't have the resources to Bake Bread!")
        case "feed_chickens":
            if farmer.hearts > 0 and farmer.wheat >= 2:
                farmer.feed_chickens()
                return f"\nHearts Remaining: {farmer.hearts}\nWheat: {farmer.wheat}\nEggs: {farmer.eggs}"
            else:
                raise ValueError(
                    "...But you don't have the resources to Feed Chickens!"
                )
        case "unlock_chickens":
            if farmer.hearts > 0 and farmer.wheat >= 20:
                farmer.unlock_chickens()
                return f"\nHearts Remaining: {farmer.hearts}\nWheat: {farmer.wheat}"
            else:
                raise ValueError(
                    "...But you don't have the resoures to unlock Chickens yet!"
                )
        case "feed_cows":
            if farmer.hearts > 0 and farmer.wheat >= 5:
                farmer.feed_cows()
                return f"\nHearts Remaining: {farmer.hearts}\nWheat: {farmer.wheat}\nMilk: {farmer.milk}"
            else:
                raise ValueError("...But you don't have the resources to Feed Cows!")
        case "unlock_cows":
            if farmer.hearts > 0 and farmer.eggs >= 10:
                farmer.unlock_cows()
                return f"\nHearts Remaining: {farmer.hearts}\nEggs: {farmer.eggs}"
            else:
                raise ValueError(
                    "... But you don't have the resoures to unlock Cows yet!"
                )
        case "make_cheese":
            if farmer.hearts > 0 and farmer.milk >= 3:
                farmer.make_cheese()
                return f"\nHearts Remaining: {farmer.hearts}\nMilk: {farmer.milk}\nCheese: {farmer.cheese}"
            else:
                raise ValueError(
                    "...But you don't have the resources to Make Cheese yet!"
                )
        case "unlock_horses":
            if (
                farmer.hearts > 0
                and farmer.eggs >= 10
                and farmer.milk >= 5
                and farmer.cheese >= 2
            ):
                farmer.unlock_horses()
                return "\nYou now have Horses!"
            else:
                raise ValueError(
                    "...But you don't have the resoures to unlock Horses yet!"
                )
        case _:
            raise ValueError("Invalid choice, please try again!")


def random_event():
    rand = random.randint(0, 7)
    return rand == 3


def inventory(farmer):
    return f"\n==========================\nINVENTORY:\nFarmer Hearts: {farmer.hearts} \nWheat: {farmer.wheat}\nEggs: {farmer.eggs}\nMilk: {farmer.milk}\nCheese: {farmer.cheese}\n==========================\n"


if __name__ == "__main__":
    main()
