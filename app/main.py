def get_human_age(cat_age: int, dog_age: int) -> list:
    if cat_age < 15:
        human_to_cat = 0
    elif cat_age < 24:
        human_to_cat = 1
    else:
        human_to_cat = 2
        for i in range((cat_age - 24) // 4):
            human_to_cat += 1

    if dog_age < 15:
        human_to_dog = 0
    elif dog_age < 24:
        human_to_dog = 1
    else:
        human_to_dog = 2
        for i in range((dog_age - 24) // 5):
            human_to_dog += 1
    return [human_to_cat, human_to_dog]
