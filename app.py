questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing Unit"],
        "answer": 1
    },
    {
        "question": "Which language is used for web development?",
        "options": ["HTML", "Python", "Java", "All of the above"],
        "answer": 4
    },
    {
        "question": "Which data structure uses FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": 2
    }
]

print("ONLINE EXAMINATION SYSTEM")
print("=========================")

score = 0

for q in questions:
    print("\n" + q["question"])

    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")

    ans = input("Enter answer: ")

    if ans.isdigit() and int(ans) == q["answer"]:
        score += 1

print("\nEXAM COMPLETED")
print("Score:", score, "/", len(questions))