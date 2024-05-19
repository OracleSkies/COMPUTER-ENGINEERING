from Character import Character

player = Character("player",2,10)
goblin = Character("goblin",1,5)


while True:
    action = input("action: ")
    match action:
        case "attack":
            player.attack(goblin)
            print("goblin HP: ",goblin.health)
            goblin.attack(player)
            print("player HP: ",player.health)

            if player.health <= 0:
                print("Player died")
                break
            elif goblin.health <= 0:
                print("Goblin died")
                break
            else:
                pass
        case "exit":
            break
        case _:
            print("invalid")