import random

def create_avatar():
    """
    Prompts user to create an avatar by entering a name.
    Returns the name of the avatar.
    """
    print("Welcome to the Barbell Blueprint! \nWe are excited that you have chosen us to help guide you through your strength jounrey")
    name = input("Please enter your name: ")
    print(f"Welcome to the Powerlifting World, {name}!")
    return name

def choose_lift():
    """
    Allows the user to choose a lift from a predefined list.
    Returns the chosen lift.
    """
    print("Choose your lift:")
    lifts = {1: 'Bench Press', 2: 'Squat', 3: 'Deadlift'}
    for key, value in lifts.items():
        print(f"{key}. {value}")
    while True:
        try:
            choice = int(input('Enter your choice (1-3): '))
            if 1 <= choice <= 3:
                return lifts[choice]
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def round_to_nearest_five(number):
    """
    Rounds a number to the nearest multiple of five.
    """
    return round(number / 5) * 5

def calculate_percentage(weight, reference_1rm):
    """
    Calculates the weight as a percentage of the reference 1RM.
    """
    return round((weight / reference_1rm) * 100)

def get_user_input(prompt, input_type=float):
    """
    Generic function to get user input and handle errors.
    """
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def periodize_training(starting_1rm, goal_1rm):
    """
    Creates a periodized training plan based on starting and goal 1RM.
    """
    weekly_schedule = {}
    for week in range(1, 9):
        if week <= 4:
            percentage = 0.70 + 0.05 * (week - 1)
        elif week <= 7:
            percentage = 0.85 + 0.05 * (week - 5)
        else:
            percentage = 1.00

        training_weight = round_to_nearest_five(goal_1rm * percentage)
        reps = 10 - 2 * week if week <= 4 else (8 - week if week <= 7 else 1)
        sets = 4 if week <= 7 else 1
        percent_of_1rm = calculate_percentage(training_weight, goal_1rm)

        weekly_schedule[week] = {
            'Weight': training_weight,
            'Reps': reps,
            'Sets': sets,
            'PercentOf1RM': percent_of_1rm
        }

    return weekly_schedule

def create_program(starting_1rm, goal_1rm, lift_choice):
    """
    Generates the training program and prints it out.
    """
    if goal_1rm <= starting_1rm:
        print("Goal 1RM must be higher than current 1RM. Please set a realistic target.")
        return None

    training_plan = periodize_training(starting_1rm, goal_1rm)
    print(f"\n{lift_choice} 8-Week Training Program:")
    for week, plan in training_plan.items():
        print(f"Week {week}: {plan['Sets']} sets of {plan['Reps']} reps at {plan['Weight']} lbs ({plan['PercentOf1RM']}% of 1RM)")
    
    return training_plan

def get_feedback():
    """
    Gets feedback from the user at the end of the program.
    """
    feedback = input("How was your experience with the program? (Good/Bad): ")
    print("Thank you for your feedback!" if feedback.lower() == "good" else "We'll strive to improve!")

def main():
    """
    Main function to run the powerlifting simulator game.
    """
    avatar_name = create_avatar()
    lift_choice = choose_lift()
    starting_1rm = get_user_input(f"Enter your current {lift_choice} 1RM (lbs): ")
    goal_1rm = get_user_input(f"Enter your goal {lift_choice} 1RM after 8 weeks (lbs): ")

    program = create_program(starting_1rm, goal_1rm, lift_choice)
    if program is None:
        print("Unable to create program. Exiting game.")
        return

    get_feedback()

if __name__ == "__main__":
    main()