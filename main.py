import os

# File to store data
FILE_NAME = "dangerous_areas.txt"

# Load existing areas from file
def load_areas():
    areas = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                if " - " in line:
                    area, description = line.strip().split(" - ", 1)
                    areas[area] = description
    return areas

# Save areas to file
def save_areas(areas):
    with open(FILE_NAME, "w") as file:
        for area, description in areas.items():
            file.write(f"{area} - {description}\n")

# View all dangerous areas
def view_areas(areas):
    if not areas:
        print("\n⚠️ No dangerous areas recorded yet.")
    else:
        print("\n--- Dangerous Areas in Johannesburg ---")
        for area, description in areas.items():
            print(f"- {area}: {description}")

# Add a new dangerous area
def add_area(areas):
    area = input("\nEnter area name: ").strip().title()
    description = input("Enter description of danger: ").strip()
    if area in areas:
        print("⚠️ This area is already listed. Updating description...")
    areas[area] = description
    save_areas(areas)
    print("✅ Area saved successfully!")

# Main program
def main():
    areas = load_areas()

    while True:
        print("\n--- Johannesburg Dangerous Areas ---")
        print("1. View dangerous areas")
        print("2. Add a dangerous area")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            view_areas(areas)
        elif choice == "2":
            add_area(areas)
        elif choice == "3":
            print("👋 Exiting program. Stay safe!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Run program
if __name__ == "__main__":
    main()

