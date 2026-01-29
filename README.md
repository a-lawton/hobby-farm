# Hobby Farm
### Video Demo:  <https://youtu.be/hiDGYX5EMK8>
### Description:
    Hobby Farm is a game written in Python, to simulate the journey of establishing a hobby farm. The user has a maximum amount of hearts that they can expend during the day. Hearts are used by selecting actions, such as planting wheat or unlocking cows. Available options change dynamically depending on the farmers choices, such as whether the player has unlocked chickens or cows.

    Once all of the hearts have been used for the day, there are 5 random events that could be triggered that add a level of variability to the game:
        - A locust swarm steals all of your wheat stores, which sets the wheat balance to 0.
        - A fox steal all of your eggs which sets the egg balance to 0.
        - One of your cows has a baby, which doubled your milk balance.
        - Your maximum hearts increase by 1
        - You have a terrible night sleep which gives you half of your daily hearts. If you have 3 hearts, you will only have 1 heart remaining for the day.
        
    These random events are triggered by the `random_event()` function that utilizes a python library `random` to get a random integer between 0 and 7 inclusive. It then returns a True if that random integer is equal to 3. I decided to call this function for each random event, to increase the chance of a random event occuring and to minimize impact of order of operations of the if statements in the `main()` function.

    As the farmer sleeps, their daily hearts are set back to the maximum (unless the random sleep event is triggered), they are given 5 wheat and the day count is incremented.

    The game continues until the user is able to unlock horses. I made the decision to immediately trigger the horse ride to minimize unnecessary additional time to complete the game.

    I wanted this project to not just function well but also be enoyable to play. This was a fun challenge, and I enjoyed how it brought the game to the next level (ie/ time.sleep(), cowsay, strategically placed print() lines). I toyed with global variables as well as multiple classes for each animal, before I settled with using one Farmer class, but it still challenged my understanding (particularly surrounding getters and setters).

#### Design Decisions:
    I didn't love the look of the user's selection displaying in the console and wanted to print out something a little more user friendly instead which is why I ended up using the python library getpass instead of input.

    Additionally, I added in some separator lines, a python library "time" for small periods of delay and a pip-installable library "cowsay" for some graphics. I wanted it to feel as user-friendly as I could, while still using the terminal for the game. In the future, I would love to learn more about graphic, UI and how to beautify the game more.

### Files:
    This project consists of the following files and key functions.
#### **project.py**
  This is the file that runs the game. It contains the following custom functions:
  - __main()__ : Handles the user input/selections and keeps track of the days that it takes to "win" the game. It contains two while loops, one to signify game duration and the other to signifiy one day (the time that it takes for the user to expend maximum daily energy). It calls `display_options()` as well as `select_options()` and uses that information  It also includes several helper functions that manage game logic, such as displaying available actions, updating the player’s resources, and unlocking animals.

   - __display_options(farmer)__ :
   - __select_options(farmer, action)__ :
   - __random_event()__ :
   - __inventory(farmer)__ :

#### **test_project.py**
  This file contains pytest tests for 3 essential functions used in `project.py`, all prepended with "test" for readability.
  - __test_display_options()__ : asserts whether the `display_options()` function accurately returns the correct options, depending on if the farmer has chickens and/or cows unlocked.
   - __test_select_options()__ : asserts whether the `select_options()` function accurately returns the correct selection, depending on what the farmer has unlocked, and if they have the resources to perform said action. It will also determine if the expected `ValueError` is raised when the farmer does not have the resources required to perform the selected action.
   - __test_inventory()__ : asserts whether the correct values and format is returned when the `inventory()` function is called.

  The tests verify that the fundamental functions in `project.py` behave as expected, such as accessing a farmer's wheat stash or selecting a restricted action.

#### **requirements.txt**
  This file includes all pip-installable libraries that are required in order to run `project.py` and `test_projet.py`

#### **README.md**
  This file breaks down what Hobby Farm is, how it works, what all of the files are for and some of the design decisions.
