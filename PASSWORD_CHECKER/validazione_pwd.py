import re

def validazione_password(password):
    """
    Questa funzione verifica se la password rispetta i seguenti criteri:
    - deve avere almeno 8 caratteri
    - deve avere almeno una lettera maiuscola
    - deve avere almeno una lettera minuscola
    - deve avere almeno un numero
    - deve avere almeno un carattere speciale
    :param password: stringa, password da validare
    :return: boolean, True se la password è valida, False altrimenti
    """
    # Verifica se la password ha almeno 8 caratteri
    if len(password) < 8 or len(password) > 20:
        return False

    # Verifica se la password ha almeno una lettera maiuscola
    if not any(letter.isupper() for letter in password):
        return False

    # Verifica se la password ha almeno una lettera minuscola
    if not any(letter.islower() for letter in password):
        return False

    # Verifica se la password ha almeno un numero
    if not any(letter.isdigit() for letter in password):
        return False

    # Verifica se la password ha almeno un carattere speciale
    if not any(letter in "!@#$%^&*()-+" for letter in password):
        return False

    return True

def validazione_password_con_regex(password):
    """
    Valida una password utilizzando pattern regex e solleva ValueError con messaggi specifici per ogni fallimento nella validazione.
    La password deve soddisfare i seguenti criteri:
    - Lunghezza tra 8 e 20 caratteri
    - Almeno una lettera maiuscola
    - Almeno una lettera minuscola
    - Almeno un numero
    - Almeno un carattere speciale tra: !@#$%^&*()-+
    Args:
        password (str): La stringa della password da validare
    Raises:
        ValueError: Se un qualsiasi criterio di validazione non è soddisfatto, con un messaggio di errore specifico per ogni caso:
            - "La password deve essere tra 8 e 20 caratteri"
            - "La password deve contenere almeno una lettera maiuscola" 
            - "La password deve contenere almeno una lettera minuscola"
            - "La password deve contenere almeno un numero"
            - "La password deve contenere almeno un carattere speciale (!@#$%^&*()-+)"
    Returns:
        None: La funzione solo valida e solleva eccezioni se la validazione fallisce
    """
    # Verifica lunghezza
    if not re.match(r'^.{8,20}$', password):
        raise ValueError("La password deve essere tra 8 e 20 caratteri")

    # Verifica maiuscola
    if not re.search(r'[A-Z]', password):
        raise ValueError("La password deve contenere almeno una lettera maiuscola")

    # Verifica minuscola
    if not re.search(r'[a-z]', password):
        raise ValueError("La password deve contenere almeno una lettera minuscola")

    # Verifica numero
    if not re.search(r'\d', password):
        raise ValueError("La password deve contenere almeno un numero")

    # Verifica carattere speciale
    if not re.search(r'[!@#$%^&*()-+]', password):
        raise ValueError("La password deve contenere almeno un carattere speciale (!@#$%^&*()-+)")




def validazione_password_con_messaggio_di_errore(password):
    """
    Questa funzione verifica se la password rispetta i criteri e solleva eccezioni per errori specifici
    :param password: stringa, password da validare
    :raises ValueError: se la password non rispetta i criteri
    :return: True se la password è valida
    """
    # Verifica se la password ha almeno 8 caratteri
    if len(password) < 8 or len(password) > 20:
        raise ValueError("La password deve essere tra 8 e 20 caratteri")

    # Verifica se la password ha almeno una lettera maiuscola
    if not any(letter.isupper() for letter in password):
        raise ValueError("La password deve contenere almeno una lettera maiuscola")

    # Verifica se la password ha almeno una lettera minuscola
    if not any(letter.islower() for letter in password):
        raise ValueError("La password deve contenere almeno una lettera minuscola")

    # Verifica se la password ha almeno un numero
    if not any(letter.isdigit() for letter in password):
        raise ValueError("La password deve contenere almeno un numero")

    # Verifica se la password ha almeno un carattere speciale
    if not any(letter in "!@#$%^&*()-+" for letter in password):
        raise ValueError("La password deve contenere almeno un carattere speciale (!@#$%^&*()-+)")

    
