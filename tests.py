from food_example import matching_recipe

# food_item = "chicken"
# food_allergies = "no"

def test_matching_recipe():
    result = matching_recipe("Bacon Wrapped Jalapeno Popper Stuffed Chicken")
    assert result == "http://food2fork.com/view/35120"

def test_matching_url():
    result = matching_url("Bacon Wrapped Jalapeno Popper Stuffed Chicken")
    assert result == "http://www.closetcooking.com/2012/11/bacon-wrapped-jalapeno-popper-stuffed.html"
