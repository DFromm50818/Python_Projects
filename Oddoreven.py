def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    try:
        # Benutzereingabe lesen
        user_input = int(input("Gib eine Zahl ein: "))

        # Überprüfen, ob die Zahl gerade oder ungerade ist
        result = check_even_odd(user_input)

        # Ergebnis ausgeben
        print(f"Die Zahl {user_input} ist {result}.")
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")

if __name__ == "__main__":
    main()