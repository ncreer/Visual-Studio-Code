import textwrap

print("Please enter the following:")
print(" ")

adj = input("adjective: ")
animal = input("animal: ")
verb = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
print(" ")

print("Your story is:")
story = (f'The other day, I was really in trouble. It all started when I saw a very {adj} {animal} {verb} down the hallway. "{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.')

wrapped = textwrap.wrap(story, width=85)
for line in wrapped:
    print(line) 