import random

print("🎉 Welcome to the Mad Libs Word Game! 🎉\n")

# Loop to allow replaying
while True:
    # Randomized input prompts
    place_prompts = ["Enter a spooky place: ", "Name a place you like: ", "Where did you go today? "]
    person_prompts = ["Who did you see there? ", "Enter a famous person's name: ", "Name someone you know: "]
    object_prompts = ["Name something they were holding: ", "Enter a random object: ", "What item did they carry? "]
    another_place_prompts = ["Where did they run to? ", "Enter another place: ", "Where did they escape to? "]
    emotion_prompts = ["How were they feeling? ", "Enter an emotion: ", "What did they look like they felt? "]

    # Collect inputs with randomized prompts
    place_name = input(random.choice(place_prompts))
    person_name = input(random.choice(person_prompts))
    object_name = input(random.choice(object_prompts))
    another_place = input(random.choice(another_place_prompts))
    emotion = input(random.choice(emotion_prompts))

    # Create the story
    story = f"""
--- Your Mad Libs Story ---
Today I went to {place_name}.
While exploring, I saw {person_name} holding a {object_name}!
{person_name} looked really {emotion}, like something strange was going on.
Suddenly, they ran away toward {another_place}, but I stayed behind in {place_name}.
What a weird day!
"""

    print(story)

    # Save the story to a text file
    with open("my_story.txt", "w") as file:
        file.write(story)
    print("📝 Your story has been saved to 'my_story.txt'!\n")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break

