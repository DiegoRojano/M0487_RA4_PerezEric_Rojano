import sqlite3

def crear_base_dades():
    """
    Crea la base de dades 'grups.db' i la taula 'grups' si no existeix.

    Aquesta funció estableix una connexió amb la base de dades SQLite i crea la taula 'grups' amb els següents camps:
    - nom (text, clau primària)
    - any_inici (enter)
    - tipus_musica (text)
    - membres (enter)
    """
    conn = sqlite3.connect("grups.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grups (
            nom TEXT PRIMARY KEY,
            any_inici INTEGER,
            tipus_musica TEXT,
            membres INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def consultar_grup_per_nom(nom):
    """
    Consulta la base de dades per trobar un grup pel seu nom.

    Args:
        nom (str): El nom del grup a cercar.

    Returns:
        tuple: Una tupla amb les dades del grup si existeix, o None si no es troba.
    """
    conn = sqlite3.connect("grups.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grups WHERE nom = ?", (nom,))
    grup = cursor.fetchone()
    conn.close()
    return grup

def afegir_grup(nom, any_inici, tipus_musica, membres):
    """
    Afegeix un nou grup musical a la base de dades.

    Args:
        nom (str): Nom del grup.
        any_inici (int): Any d'inici del grup.
        tipus_musica (str): Tipus de música que fa el grup.
        membres (int): Nombre d'integrants del grup.
    """
    try:
        conn = sqlite3.connect("grups.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO grups VALUES (?, ?, ?, ?)", (nom, any_inici, tipus_musica, membres))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Ja existeix un grup amb aquest nom.")
    finally:
        conn.close()

def mostrar_grups():
    """
    Retorna una llista de tots els grups musicals de la base de dades.

    Returns:
        list: Una llista de tuples amb la informació de cada grup.
    """
    conn = sqlite3.connect("grups.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grups")
    grups = cursor.fetchall()
    conn.close()
    return grups

def eliminar_grup(nom):
    """
    Elimina un grup de la base de dades pel seu nom.

    Args:
        nom (str): Nom del grup a eliminar.
    """
    conn = sqlite3.connect("grups.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM grups WHERE nom = ?", (nom,))
    conn.commit()
    conn.close()

def actualitzar_grup(nom, any_inici, tipus_musica, membres):
    """
    Actualitza les dades d'un grup existent a la base de dades.

    Args:
        nom (str): Nom del grup que volem actualitzar.
        any_inici (int): Nou any d'inici.
        tipus_musica (str): Nou tipus de música.
        membres (int): Nou nombre d'integrants.
    """
    conn = sqlite3.connect("grups.db")
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE grups SET any_inici = ?, tipus_musica = ?, membres = ?
        WHERE nom = ?
    ''', (any_inici, tipus_musica, membres, nom))
    conn.commit()
    conn.close()

def intro_dades(nom=None):
    """
    Demana dades a l'usuari per a un grup musical, amb validacions.

    Si s'indica un nom, es comprova si ja existeix a la base de dades.
    En cas afirmatiu, es mostren les dades actuals del grup.
    Si no existeix, es demanen les dades del nou grup.

    Args:
        nom (str, opcional): Nom del grup si ja es coneix.

    Returns:
        tuple: Dades del grup introduïdes per l'usuari (nom, any_inici, tipus, membres).
    """
    if nom:
        resultat = consultar_grup_per_nom(nom)
        if resultat is None:
            print("No s'ha trobat cap grup amb aquest nom.")
            nom = ""
        else:
            print("Grup trobat:", resultat[1])
            nom = resultat[1].capitalize()

    while True:
        try:
            nom_input = input(f"Nom: (INTRO per mantenir el nom:{nom})").strip()
            if not nom_input and nom == "":
                raise ValueError("El nom no pot estar buit.")
            elif nom_input and nom != "":
                nom_input = nom
            break
        except ValueError as e:
            print(e)

def menu():
    """
    Mostra un menú interactiu per gestionar grups musicals.
    """
    crear_base_dades()
    while True:
        print("\n1. Afegir grup")
        print("2. Mostrar grups")
        print("3. Eliminar grup")
        print("4. Actualitzar grup")
        print("5. Consultar grup per nom")
        print("0. Sortir")
        try:
            opcio = int(input("Escull una opció: "))
            if opcio == 1:
                nom = input("Nom del grup: ")
                any_inici = int(input("Any d'inici: "))
                tipus = input("Tipus de música: ")
                membres = int(input("Nombre d'integrants: "))
                afegir_grup(nom, any_inici, tipus, membres)
            elif opcio == 2:
                for grup in mostrar_grups():
                    print(grup)
            elif opcio == 3:
                nom = input("Nom del grup a eliminar: ")
                eliminar_grup(nom)
            elif opcio == 4:
                nom = input("Nom del grup a actualitzar: ")
                any_inici = int(input("Nou any d'inici: "))
                tipus = input("Nou tipus de música: ")
                membres = int(input("Nou nombre d'integrants: "))
                actualitzar_grup(nom, any_inici, tipus, membres)
            elif opcio == 5:
                nom = input("Nom del grup a consultar: ")
                grup = consultar_grup_per_nom(nom)
                if grup:
                    print(grup)
                else:
                    print("No s'ha trobat cap grup amb aquest nom.")
            elif opcio == 0:
                print("Sortint del programa...")
                break
            else:
                print("Opció no vàlida.")
        except ValueError:
            print("Error: Entrada no vàlida. Introdueix números on calgui.")

if __name__ == "__main__":
    menu()
