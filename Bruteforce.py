import concurrent.futures
import itertools
import hashlib


# Funktion zum Überprüfen des Passworts mit einem Hash
def check_password(password):
    # Simuliere hier die Passwortüberprüfung mit einem Hash (z.B. SHA-256)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Hier könnte die Überprüfung mit dem tatsächlichen gehashten Passwort erfolgen
    target_hashed_password = '6bbc9e9511954e128d5e6d07f6f43c4c63262a59f4b1c0c9f9c0d623016326d5'  # Hier das tatsächliche gehashte Passwort einfügen

    if hashed_password == target_hashed_password:
        return password


# Funktion für parallelen Brute-Force-Angriff
def parallel_brute_force(possible_chars, max_length):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        for length in range(1, max_length + 1):
            combinations = itertools.product(possible_chars, repeat=length)
            for combination in combinations:
                password_attempt = ''.join(combination)
                futures.append(executor.submit(check_password, password_attempt))

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                return f"Passwort gefunden: {result}"

    return "Passwort nicht gefunden"


# Beispielaufruf der Funktion für parallelisierten Brute-Force-Angriff
possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
max_password_length = 25  # Maximale Länge des Passworts

result = parallel_brute_force(possible_characters, max_password_length)
print(result)
