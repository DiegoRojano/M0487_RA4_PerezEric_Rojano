import sqlite3

def obtenir_connexio(conn=None):
    return conn if conn else sqlite3.connect("grups_musicals.db")

def crear_base_de_dades(conn=None):
    conn = obtenir_connexio(conn)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grups (
            nom TEXT PRIMARY KEY,
            any_inici INTEGER,
            tipus_musica TEXT,
            integrants INTEGER
        )
    ''')
    conn.commit()
    if not conn.in_transaction:
        conn.close()

def afegir_grup(nom, any_inici, tipus_musica, integrants, conn=None):
    try:
        conn = obtenir_connexio(conn)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO grups VALUES (?, ?, ?, ?)", (nom, any_inici, tipus_musica, integrants))
        conn.commit()
        if not conn.in_transaction:
            conn.close()
        print("Grup afegit correctament.")
    except sqlite3.IntegrityError:
        print("Ja existeix un grup amb aquest nom.")
    except Exception as e:
        print("Error en afegir grup:", e)

def mostrar_grups(conn=None):
    conn = obtenir_connexio(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grups")
    grups = cursor.fetchall()
    for grup in grups:
        print(grup)
    if not conn.in_transaction:
        conn.close()

def eliminar_grup(nom, conn=None):
    conn = obtenir_connexio(conn)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM grups WHERE nom = ?", (nom,))
    if cursor.rowcount == 0:
        print("No s'ha trobat cap grup amb aquest nom.")
    else:
        print("Grup eliminat.")
    conn.commit()
    if not conn.in_transaction:
        conn.close()

def actualitzar_grup(nom, any_inici=None, tipus_musica=None, integrants=None, conn=None):
    conn = obtenir_connexio(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grups WHERE nom = ?", (nom,))
    if cursor.fetchone() is None:
        print("Grup no trobat.")
        if not conn.in_transaction:
            conn.close()
        return
    if any_inici:
        cursor.execute("UPDATE grups SET any_inici = ? WHERE nom = ?", (any_inici, nom))
    if tipus_musica:
        cursor.execute("UPDATE grups SET tipus_musica = ? WHERE nom = ?", (tipus_musica, nom))
    if integrants:
        cursor.execute("UPDATE grups SET integrants = ? WHERE nom = ?", (integrants, nom))
    conn.commit()
    if not conn.in_transaction:
        conn.close()
    print("Grup actualitzat.")

def menu():
    crear_base_de_dades()
    while True:
        print("\n--- MENÚ ---")
        print("1. Afegir grup")
        print("2. Mostrar grups")
        print("3. Eliminar grup")
        print("4. Actualitzar grup")
        print("5. Sortir")
        opcio = input("Selecciona una opció: ")
        if opcio == "1":
            try:
                nom = input("Nom del grup: ")
                any_inici = int(input("Any d'inici: "))
                tipus_musica = input("Tipus de música: ")
                integrants = int(input("Nombre d’integrants: "))
                afegir_grup(nom, any_inici, tipus_musica, integrants)
            except ValueError:
                print("Dades incorrectes. Introdueix valors vàlids.")
        elif opcio == "2":
            mostrar_grups()
        elif opcio == "3":
            nom = input("Nom del grup a eliminar: ")
            eliminar_grup(nom)
        elif opcio == "4":
            nom = input("Nom del grup a actualitzar: ")
            try:
                any_inici = input("Nou any d'inici (enter per no canviar): ")
                tipus_musica = input("Nou tipus de música (enter per no canviar): ")
                integrants = input("Nou nombre d’integrants (enter per no canviar): ")
                any_inici = int(any_inici) if any_inici else None
                integrants = int(integrants) if integrants else None
                actualitzar_grup(nom, any_inici, tipus_musica or None, integrants)
            except ValueError:
                print("Dades incorrectes.")
        elif opcio == "5":
            print("Fins aviat!")
            break
        else:
            print("Opció no vàlida.")