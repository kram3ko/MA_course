def message_people(people: list) -> callable:
    def print_message(message: str) -> None:
        if message == "hello":
            print(f"Hello, {', '.join(people)}, nice to see you!")
        elif message == "meeting":
            print(f"{', '.join(people)}, we have a meeting in an hour, don't be late!")
        elif message == "bye":
            print(f"Bye {', '.join(people)}, see you tomorrow!")

    return print_message


mes_people = message_people(["Alex", "Robert", "Tom", "Ivan"])
mes_people("hello")
