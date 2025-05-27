while True:
    path = input("Which path do you choose? (left/right): ").lower()
    if path == "left":
        print("You found a hidden tunnel! You're safe.")
        break
    elif path == "right":
        print("Oh no! The Glitch’s trap was here! Try again.")
        break
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")