activities = []

def add_activity(activity):
    """Add an activity to the list."""
    activities.append(activity)
    print(f"Activity '{activity}' added.")

def view_activities():
    """View all activities in the list."""
    if not activities:
        print("No activities found.")
    else:
        print("Activities:")
        for activity in activities:
            print(f"- {activity}")

def remove_activity(activity):
    """Remove an activity from the list."""
    if activity in activities:
        activities.remove(activity)
        print(f"Activity '{activity}' removed.")
    else:
        print(f"Activity '{activity}' not found in the list.")

def main():
    while True:
        print("\nActivity Tracker")
        print("1. Add Activity")
        print("2. View Activities")
        print("3. Remove Activity")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            activity = input("Enter the activity to add: ")
            add_activity(activity)
        elif choice == '2':
            view_activities()
        elif choice == '3':
            activity = input("Enter the activity to remove: ")
            remove_activity(activity)
        elif choice == '4':
            print("Exiting the Activity Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

# Make sure to call main()
main()
