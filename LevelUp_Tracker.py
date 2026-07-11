import os
import logging

# 1. Create the /logs folder automatically if it doesn't exist
os.makedirs('logs', exist_ok=True)

# 2. Configure the logging system
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s — [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)

logging.info("LevelUpTracker started successfully.")

# 3. Data input with continuous validation loops
# Exercise Name Loop
while True:
    exercise_name = input("Enter exercise name: ").strip()
    if exercise_name.isdigit() or exercise_name == "":
        logging.warning("Invalid exercise name attempted.")
        print("[ERROR] Exercise name cannot be just a number or empty. Try again.")
    else:
        break # Exit the loop if the data is correct

# Exercise Type Loop
while True:
    exercise_type = input("Enter exercise type (compound / isolation): ").strip().lower()
    if exercise_type != "compound" and exercise_type != "isolation":
        logging.warning(f"Invalid exercise type attempted: {exercise_type}")
        print("[ERROR] It must be either 'compound' or 'isolation'. Try again.")
    else:
        break

# Weight Lifted Loop
while True:
    try:
        weight_lifted = float(input("Enter weight lifted (in kg): "))
        break
    except ValueError:
        logging.warning("Invalid weight input. Text entered instead of number.")
        print("[ERROR] You must enter a valid number for weight. Try again.")

# Reps Loop
while True:
    try:
        reps_completed = int(input("Enter reps completed: "))
        break
    except ValueError:
        logging.warning("Invalid reps input. Text entered instead of number.")
        print("[ERROR] You must enter a valid whole number for reps. Try again.")

# Sets Loop
while True:
    try:
        sets_completed = int(input("Enter sets completed: "))
        break
    except ValueError:
        logging.warning("Invalid sets input. Text entered instead of number.")
        print("[ERROR] You must enter a valid whole number for sets. Try again.")

# Effort Score Loop (Validates both text errors and number range)
while True:
    try:
        effort_score = int(input("Enter effort score (1-10): "))
        if effort_score < 1 or effort_score > 10:
            logging.warning(f"Effort score out of range: {effort_score}.")
            print("[ERROR] Effort score must be between 1 and 10. Try again.")
        else:
            break
    except ValueError:
        logging.warning("Invalid effort input. Text entered instead of number.")
        print("[ERROR] You must enter a valid number for effort score. Try again.")

logging.info(f"Data for exercise '{exercise_name}' entered and validated successfully.")

# 4. Total volume calculation
if weight_lifted == 0:
    total_volume = 75.0 * reps_completed * sets_completed
    logging.info("Bodyweight exercise detected (0kg). Used volume constant 75.")
else:
    total_volume = weight_lifted * reps_completed * sets_completed

# 5. Next weight calculation and feedback assignment
if effort_score == 9 or effort_score == 10:
    next_weight = weight_lifted
    feedback = "Congrats!, keep the same weight next time to practice form"
elif effort_score == 7 or effort_score == 8:
    if exercise_type == "compound":
        next_weight = weight_lifted + 2.5
    else:
        next_weight = weight_lifted + 1.25
    feedback = "Good job!, Increase the weight next session"
else:
    if exercise_type == "compound":
        next_weight = weight_lifted + 5.0
    else:
        next_weight = weight_lifted + 2.5
    feedback = "Too easy! Increase the weight next session"

print("\n" + feedback)
logging.info(f"Progress calculated successfully. Recommendation: {feedback}")

# 6. Console output summary
print('\n')
print("Exercise name:", exercise_name, "| Type:", exercise_type)
print("Weight lifted:", weight_lifted, "kg | Reps:", reps_completed, "| Sets:", sets_completed)
print("Effort score:", effort_score, "| Calculated Total Volume:", total_volume, "kg")
print("Recommended weight for next session:", next_weight, "kg")

# 7. Final successful log entry
logging.info(f"Session saved. Total Volume: {total_volume}kg | Next Weight: {next_weight}kg.")