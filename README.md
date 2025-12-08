# realms-of-pythonia

Python practice project demonstrating dictionaries, nested data, file I/O with JSON, and menu-driven programs in a fantasy realm setting

This project was originally developed for my Software Workshop 1 module at the University of Birmingham MSc Computer Science course as part of learning core Python programming concepts.
With a bit of cleanup and tweaking from my original submission, I have completed the program to fit the spec and here it is!

## Project Overview

The program models a world called Pythonia, where each realm contains creatures with powers, inventories, and quests. Users can:

- Display all realms and creatures, including their type, power level, and inventory totals. 
- Add new creatures to a realm, creating the realm if it does not yet exist. 
- Collect all incomplete quests for every creature and write them to a JSON file. 
- Generate a quest report for a specific creature showing their remaining quests. 

The application runs in a simple text menu loop and is implemented in a single Python file, `realms_pythonia.py`.

## What this project demonstrates

This assessment was used to practice fundamental Python skills, including:

- Working with dictionaries and nested data structures to represent realms, creatures, inventories, and quests.
- Looping over complex data (nested dictionaries and lists) to compute totals and extract specific information.
- Writing and reading structured data using the `json` module
- Designing and calling functions with clear responsibilities (`display_realms`, `add_creature`, `gather_incomplete_quests`, `quest_report`).
- Building a menu-driven console interface to interact with the data.

## Main features

- **Display realms**: Shows each creature’s realm, type, power, and maintains a running total of all inventory items across Pythonia. 
- **Add creature to realm**: Adds a new creature to a specified realm, creating the realm if needed and confirming the operation to the user. 
- **Gather incomplete quests**: Checks all creatures, finds quests marked as incomplete, and stores them in an `allincompletequests.json` file.
- **Quest report**: Prints a numbered list of a chosen creature’s incomplete quests using the data.
