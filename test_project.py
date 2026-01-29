import project
import pytest


def test_display_options():
    farmer = project.Farmer()
    options = project.display_options(farmer)
    assert options[0]["key"] == "plant_wheat"
    assert options[0]["label"] == "Plant Wheat for 1 heart"
    assert options[1]["key"] == "bake_bread"
    assert options[1]["label"] == "Bake Bread for 1 heart + 10 wheat"
    assert options[2]["key"] == "unlock_chickens"
    assert options[2]["label"] == "Unlock Chickens for 1 heart + 20 wheat"
    assert options[3]["key"] == "unlock_cows"
    assert options[3]["label"] == "Unlock Cows for 1 heart + 10 eggs"
    assert options[4]["key"] == "make_cheese"
    assert options[4]["label"] == "Make Cheese for 1 heart + 3 milk"
    assert options[5]["key"] == "unlock_horses"
    assert (
        options[5]["label"] == "Unlock Horses for 1 heart + 10 eggs + 5 milk + 2 cheese"
    )

    farmer._has_chickens = True
    options = project.display_options(farmer)
    assert options[0]["key"] == "plant_wheat"
    assert options[0]["label"] == "Plant Wheat for 1 heart"
    assert options[1]["key"] == "bake_bread"
    assert options[1]["label"] == "Bake Bread for 1 heart + 10 wheat"
    assert options[2]["key"] == "feed_chickens"
    assert options[2]["label"] == "Feed Chickens for 1 heart + 2 wheat"
    assert options[3]["key"] == "unlock_cows"
    assert options[3]["label"] == "Unlock Cows for 1 heart + 10 eggs"
    assert options[4]["key"] == "make_cheese"
    assert options[4]["label"] == "Make Cheese for 1 heart + 3 milk"
    assert options[5]["key"] == "unlock_horses"
    assert (
        options[5]["label"] == "Unlock Horses for 1 heart + 10 eggs + 5 milk + 2 cheese"
    )

    farmer._has_cows = True
    options = project.display_options(farmer)
    assert options[0]["key"] == "plant_wheat"
    assert options[0]["label"] == "Plant Wheat for 1 heart"
    assert options[1]["key"] == "bake_bread"
    assert options[1]["label"] == "Bake Bread for 1 heart + 10 wheat"
    assert options[2]["key"] == "feed_chickens"
    assert options[2]["label"] == "Feed Chickens for 1 heart + 2 wheat"
    assert options[3]["key"] == "feed_cows"
    assert options[3]["label"] == "Feed Cows for 1 heart + 5 wheat"
    assert options[4]["key"] == "make_cheese"
    assert options[4]["label"] == "Make Cheese for 1 heart + 3 milk"
    assert options[5]["key"] == "unlock_horses"
    assert (
        options[5]["label"] == "Unlock Horses for 1 heart + 10 eggs + 5 milk + 2 cheese"
    )


def test_select_options():
    farmer = project.Farmer()
    assert project.select_options(farmer, "plant_wheat") == (
        "\nHearts Remaining: 2\nWheat: 10"
    )
    assert project.select_options(farmer, "plant_wheat") == (
        "\nHearts Remaining: 1\nWheat: 20"
    )
    assert project.select_options(farmer, "bake_bread") == (
        "\nHearts Remaining: 2\nWheat: 10"
    )
    assert project.select_options(farmer, "bake_bread") == (
        "\nHearts Remaining: 3\nWheat: 0"
    )
    with pytest.raises(ValueError):
        project.select_options(farmer, "bake_bread")
    with pytest.raises(ValueError):
        project.select_options(farmer, "unlock_chickens")
    with pytest.raises(ValueError):
        project.select_options(farmer, "unlock_cows")
    with pytest.raises(ValueError):
        project.select_options(farmer, "make_cheese")
    with pytest.raises(ValueError):
        project.select_options(farmer, "unlock_horses")
    farmer.hearts = 3
    farmer.wheat = 100
    assert (
        project.select_options(farmer, "unlock_chickens")
        == "\nHearts Remaining: 2\nWheat: 80"
    )
    assert (
        project.select_options(farmer, "feed_chickens")
        == "\nHearts Remaining: 1\nWheat: 78\nEggs: 2"
    )
    farmer.hearts = 3
    farmer.eggs = 50
    assert (
        project.select_options(farmer, "unlock_cows")
        == "\nHearts Remaining: 2\nEggs: 40"
    )
    assert (
        project.select_options(farmer, "feed_cows")
        == "\nHearts Remaining: 1\nWheat: 73\nMilk: 1"
    )
    farmer.milk = 11
    assert (
        project.select_options(farmer, "make_cheese")
        == "\nHearts Remaining: 0\nMilk: 8\nCheese: 1"
    )
    farmer.hearts = 3
    assert (
        project.select_options(farmer, "make_cheese")
        == "\nHearts Remaining: 2\nMilk: 5\nCheese: 2"
    )
    assert project.select_options(farmer, "unlock_horses") == "\nYou now have Horses!"


def test_inventory():
    farmer = project.Farmer()
    farmer.wheat = 10
    farmer.eggs = 15
    farmer.milk = 20
    assert (
        project.inventory(farmer)
        == "\n==========================\nINVENTORY:\nFarmer Hearts: 3 \nWheat: 10\nEggs: 15\nMilk: 20\nCheese: 0\n==========================\n"
    )
