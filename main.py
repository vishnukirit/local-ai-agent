from tools import generate_users, save_users

while True:
    query = input("\nAsk agent: ").lower()

    if query in ["exit", "quit"]:
        break

    # Generate users
    if "generate" in query:
        users = generate_users(["John", "Jane", "Mike"])

        print("\nGenerated Users:\n")
        print(users)

    # Save users
    elif "save" in query:
        users = generate_users(["John", "Jane", "Mike"])

        path = save_users(users)

        print(f"\nSaved to {path}")

    else:
        print("\nI can only generate or save users.")