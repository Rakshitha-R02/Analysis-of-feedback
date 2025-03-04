def get_user_feedback():
    """
    Gets feedback from the user.
    """

    print("Please provide your feedback. We appreciate your input!")

    feedback = input("Your feedback: ")

    # Optional: Add validation or further processing here.
    if not feedback: #check if the feedback is empty
        print("No feedback provided.")
        
        return None #or return ""

    # Optional: Categorize feedback (e.g., positive, negative, neutral)
    # Optional: Store feedback in a file or database.
    # Optional: Add a rating system (e.g., 1-5 stars).

    return feedback

def get_user_feedback_with_rating():
    """
    Gets feedback from the user, including a rating.
    """
    print("Please provide your feedback and a rating (1-5 stars).")

    feedback = input("Your feedback: ")
    while True: #loop until valid input is received
        try:
            rating = int(input("Your rating (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return feedback, rating

def get_multiple_lines_feedback():
    """
    Gets feedback from the user, allowing for multiple lines of input.
    """

    print("Please provide your feedback. Press Ctrl+D (or Ctrl+Z on Windows) when finished.")
    feedback_lines = []
    try:
        while True:
            line = input()
            feedback_lines.append(line)
    except EOFError:
        pass  # End of input

    feedback = "\n".join(feedback_lines)

    if not feedback:
        print("No feedback provided.")
        return None

    return feedback

def main():
    """
    Demonstrates the feedback functions.
    """
    print("Choose a feedback method:")
    print("1. Simple feedback")
    print("2. Feedback with rating")
    print("3. Multi-line feedback")

    while True:
        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice == 1:
        feedback = get_user_feedback()
        if feedback:
            print("\nThank you for your feedback:\n", feedback)
    elif choice == 2:
        feedback, rating = get_user_feedback_with_rating()
        print("\nThank you for your feedback:\n", feedback)
        print("Your rating:", rating, "stars")
    elif choice == 3:
        feedback = get_multiple_lines_feedback()
        if feedback:
            print("\nThank you for your feedback:\n", feedback)

if __name__ == "__main__":
    main()