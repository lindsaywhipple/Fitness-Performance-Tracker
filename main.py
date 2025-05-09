import csv
import os
from workout import Workout
from datetime import datetime

workouts = []
file_name = "workouts.csv"

def add_workout():      
    while True: 
        try:
            while True:     # Ensure user enters correct date format
                date_input = input("Date (MM-DD-YYYY): ")
                try:
                    datetime.strptime(date_input, "%m-%d-%Y")
                    break
                except ValueError:
                    print("Invalid Input. Use MM-DD-YYYY")

            workout_type = input("Workout Name: ")

            while True:     # Ensures valid duration input
                try:
                    duration = int(input("Duration (minutes): "))
                    break
                except ValueError:
                    print("Not a valid number. Try again.")
            
            while True:     # Ensures valid intensity input (only 1-10)
                try:
                    intensity = int(input("Intensity (1-10): "))
                    if 1 <= intensity <= 10:
                        break
                    else:
                        print("Error. Enter a number between 1 and 10.")
                except ValueError:
                    print("Error. Enter a number between 1 and 10.")

            while True:     # ensures calories burned input is a valid number
                try:
                    calories = int(input("Calories Burned: "))
                    break
                except ValueError:
                    print("Error. Enter a valid number. ")
            
            while True:         # ensures sets, reps, and weight are valid numbers
                try:
                    sets = int(input("Sets: "))
                    reps = int(input("Reps: "))
                    weight = float(input("Weight (lbs): "))
                    break
                except ValueError:
                    print("Error. Try Again.")

            w = Workout(workout_type, date_input, duration, intensity, calories, sets, reps, weight)
            workouts.append(w)
            print("Workout Added!")
            break
        except Exception as e:
            print(f"Error: {e}")

def view_workouts():
    if not workouts:
        print("No Workouts Found.")
        return
    for w in sorted(workouts, key = lambda x: x._date):
        print(w)

def save_workouts():
    with open(file_name, 'w', newline = '') as f:  
        writer = csv.writer(f)
        for w in workouts:
            s = w.get_summary()
            writer.writerow([s['date'], s['type'], s['duration'], w.sets, w.reps, w.weight, s['intensity'], s['calories']])
    print("Workouts Saved!")

def load_workouts():
    try:
        if not os.path.exists(file_name):
            print("No Workouts Found.")
            return
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                w = Workout(row[1], row[0], int(row[2]), int(row[6]), int(row[7]), int(row[3]), int(row[4]), float(row[5])) 
                workouts.append(w)
        print("Workouts Loaded!")
    except FileNotFoundError:
        print("No Workouts Found.")

def show_summary():   
    longest = max(workouts, key = lambda w: w.duration, default = None)
    if longest:
        summary = {
            "total_workouts": len(workouts),
            "total_time": sum(w.duration for w in workouts),
            'average_intensity': round(sum(w.intensity for w in workouts) / len(workouts), 2),
            'longest_workout':  (longest.workout_type, longest.duration)
        }
    print(f"\n--- Workout Summary ---")
    for k, v in summary.items():
        print(f"{k.replace('_', ' ').capitalize()}: {v}")
    print()

def unique_workout_types():
    types = set(w.workout_type for w in workouts)
    print("Unique Workout Types: ", ", ".join(types))

def main_menu():
    load_workouts()
    while True:
        print("\n--- Fitness Tracker ---\n1. Add Workout\n2. View All Workouts\n3. Save Workouts\n4. Show Summary Statistics\n5. Show Unique Workout Types \n6. Exit")
        choice = input("Chose an Option: ")

        if choice == '1':
            add_workout()
        elif choice == '2':
            view_workouts()
        elif choice == '3':
            save_workouts()
        elif choice == '4':
            show_summary()
        elif choice == '5':
            unique_workout_types()
        elif choice == '6':
            print("Goodbye.")
            break
        else: 
            print("Invalid Choice. Try Again.")

if __name__ == '__main__':
    main_menu()