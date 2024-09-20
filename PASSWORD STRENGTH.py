import re

def passwordStrength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate strength score
    score = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    # Provide feedback based on the score
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

def main():
    password = input("Enter your password: ")
    strength = passwordStrength(password)
    print(f"Your password strength is: {strength}")

if __name__ == "__main__":
    main()
