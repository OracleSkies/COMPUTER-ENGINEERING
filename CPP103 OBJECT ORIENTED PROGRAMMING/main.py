from Character import Character

hero = Character("hero", 2, 10)+
goblin = Character("goblin",1,5)

while True:
    action = input("Please select action: ")
    match action:
        case "attack":
            hero.attack(goblin)
            print(f"goblin HP {goblin.health}")
            goblin.attack(hero)
            print(f"hero HP {hero.health}")

            if hero.health <=0:
                print("Hero died")
                break
            elif goblin.health <=0:
                print("Goblin died")
                break
            else:
                pass
        case "exit":
            break
        case _:
            print("Invalid Input")