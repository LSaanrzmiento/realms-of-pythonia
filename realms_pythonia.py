import json

def display_realms(realms: dict):
    """ Display each creature, its realm, type, power, and total inventory count. """
    inventory_count = 0

    # Loops through each realm in the realms dictionary
    for realm_name, realm_data in realms.items():
        creatures = realm_data.get('creatures', {}) # Gets the creatures dictionary at each realm, or empty if none

        # Loops through each creature at the current realm
        for creature_name, details in creatures.items():
            creature_type = details['type']
            power = details['power']
            inventory = details.get('inventory' , [])

            # Print out information about the creature
            print(f'{creature_name} is {creature_type} in the realm {realm_name}. They have the power of {power}')
            inventory_count += len(inventory)   # This adds to the running total for any creature that has inventory

    print(f'The total inventory count for all creatures is: {inventory_count}\n')

    return


def add_creature(realm_name: str, creature_name: str, creature_data: dict, realms: dict):
    """ Add a creature to a realm, create a realm if it doesn't exist. """

    # If the realm is not in the realms dictionary, add in a new one
    if realm_name not in realms:
        print(f'Realm {realm_name} does not exist, let me create it!')
        print(f'Added realm {realm_name} to Pythonia.')
        realms.setdefault(realm_name, {'creatures' : {}})

    # Get the dictionary for this realm
    realm = realms[realm_name]

    # Get the creatures dictionary for this realm
    creatures = realm['creatures']

    # If the creature already exists in this realm, do not add it again
    if creature_name in creatures:
        print('Creature already in list of creatures')
        return

    # Otherwise, get the input attributes to the creature dictionary
    name = creature_name
    ctype = creature_data['type']
    power = creature_data['power']
    inventory = creature_data['inventory']
    quests = creature_data['quests']

    # Add the new creature with its details into the creatures dictionary
    creatures[name] = {
        'type' : ctype,
        'power' : power,
        'inventory' : inventory,
        'quests' : quests
    }

    print(f'Added {name} to realm {realm_name}.\n')
    return

def gather_incomplete_quests(realms: dict, incomplete_quests: dict):
    """
    Gather all incomplete quests for all creatures and write them to all_incomplete_quests.json
    The json will have structure { creature_name : [incomplete_quests, ...]
    """

    # Reset incomplete quest data
    incomplete_quests.clear()

    # Loop through each realm
    for realm_data in realms.values():
        # Get the creatures from the current realm
        creatures = realm_data.get('creatures', {})
        # Loop through the quests from each creature if they have
        for creature_name, details in creatures.items():
            for quest in details.get('quests', []):
                # Find the attributes from each quest
                quest_name, difficulty, points, status = quest
                # If the quest is incomplete, we add the creature to the incomplete quests and add the corresponding quest
                if status == 'incomplete':
                    # If creature name not added yet, creature name is created with empty list, otherwise list is retrieved
                    # quest name is added to the list regardless
                    incomplete_quests.setdefault(creature_name, []).append(quest_name)

    # Save the incomplete quests to a JSON file with dictionary formatting
    with open('all_incomplete_quests.json', 'w') as f:
        json.dump(incomplete_quests, f, indent=4)

def quest_report(incomplete_quests: dict, creature_name: str):
    """ Generate a report for a given creature, showing how many quests they still need to complete. """

    print(f'{creature_name} has the following quests to complete:')

    # Loop and print out each quest in numbered order using enumerate
    for i, quest in enumerate(incomplete_quests[creature_name], start=1):
        print(f'{i}. {quest}')


def menu():
    choice = input("Welcome to the Realms of Pythonia:\nEnter your choice (1–4 or 5):\n"
                       "1. Display a realm\n"
                       "2. Add a creature to a realm\n"
                       "3. Gather incomplete quests from each creature\n"
                       "4. Generate a quest report\n"
                       "5. Exit\n")
    return choice

def main():
    realms = {
        "Whispering Woods": {
            "creatures": {
                "Elara": {
                    "type": "fairy",
                    "power": 87,
                    "inventory": [
                        {"item": "wand", "power_bonus": 10, "origin": ("Elder Tree", "ancient")},
                        {"item": "moon dust", "power_bonus": 5, "origin": ("Lunar Caves", "rare")}
                    ],
                    "quests": [
                        ("Deliver moon dust", "easy", 20, "incomplete"),
                        ("Deliver fairy dust", "medium", 40, "incomplete")
                        ]
                },
                "Grimble": {
                    "type": "goblin",
                    "power": 42,
                    "inventory": [
                        {"item": "dagger", "power_bonus": 4, "origin": ("Iron Mines", "common")}
                    ],
                    "quests": []
                }
            }
        },
        "Crimson Mountains": {
            "creatures": {
                "Blorg": {
                    "type": "orc",
                    "power": 63,
                    "inventory": [
                        {"item": "battle axe", "power_bonus": 12, "origin": ("Forge of Flames", "rare")}
                    ],
                    "quests": [
                        ("Slay the dragon", "hard", 70, "incomplete")
                    ]
                }
            },
            "resources": ["ore", "crystal", "firestone"]
        },
        "Azure Shores": {
            "creatures": {},
            "resources": ["pearls", "salt", "coral"]
        },
        "Obsidian Peaks": {
            "creatures": {
                "Noctara": {
                    "type": "shadow wraith",
                    "power": 95,
                    "inventory": [
                        {"item": "shadow gem", "power_bonus": 12, "origin": ("Cavern of Echoes", "rare")}
                    ],
                    "quests": [
                        ("Guard the Obsidian Gate", "hard", 50, "incomplete")
                    ]
                }
            },
            "artifacts": ["cloak of silence", "midnight shard"]
        }
    }

    incomplete_quests = {}
    while True:
        choice = menu()
        match choice:
            case "1":
                display_realms(realms)

            case "2":

                realm_name = input('Enter realm name: ').strip()
                creature_name = input('Enter creature name: ').strip()
                ctype = input('Type: ').strip()
                power = int(input('Power (Enter an integer): '))

                creature_data = {
                    "type": ctype,
                    "power": power,
                    "inventory": [
                        {"item": [],
                        "power_bonus": 0,
                        "origin": ()}],
                    "quests": []
                }
                # the creature_data above is associated with Mugwort
                add_creature(realm_name, creature_name, creature_data, realms)


            case "3":
                gather_incomplete_quests(realms, incomplete_quests)

            case "4":
                creature_name = input('Which creature would you like a report for? ').strip()
                if creature_name in incomplete_quests:
                    quest_report(incomplete_quests, creature_name)
                else:
                    print('Creature not found or has no incomplete quests')

            case "5":
                print("Exiting the realms...")
                break

            case _:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    main()