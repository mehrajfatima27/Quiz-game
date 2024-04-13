def quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"],
            "answer": "William Shakespeare"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "CO2", "O2", "H2SO4"],
            "answer": "H2O"
        }
    ]

    score = 0

    for question in questions:
        print(question["question"])
        for idx, option in enumerate(question["options"]):
            print(f"{idx + 1}. {option}")

        user_answer = input("Enter your answer (1, 2, 3, or 4): ")
        user_answer = int(user_answer) - 1

        if question["options"][user_answer] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print(f"You got {score} out of {len(questions)} questions correct.")

if _name_ == "_main_":
    quiz()