# Gestor de Grups Musicals

## Descripció del projecte

Aquest projecte és una aplicació en Python que utilitza SQLite per gestionar una base de dades de grups musicals. Permet afegir, eliminar, actualitzar, consultar i mostrar informació de grups musicals mitjançant un menú interactiu en consola.

L'objectiu és facilitar la gestió d'informació com el nom del grup, l'any d'inici, el tipus de música i el nombre d'integrants.

---

## Estructura del codi

- **crear_base_dades()**: Crea la base de dades i la taula `grups` si no existeix.
- **consultar_grup_per_nom(nom)**: Retorna la informació d’un grup segons el seu nom.
- **afegir_grup(...)**: Afegeix un nou grup a la base de dades.
- **mostrar_grups()**: Mostra tots els grups registrats.
- **eliminar_grup(nom)**: Elimina un grup donat el seu nom.
- **actualitzar_grup(...)**: Actualitza la informació d’un grup existent.
- **intro_dades(nom=None)**: Demana dades a l'usuari, amb validacions incloses.
- **menu()**: Mostra el menú principal i gestiona les opcions escollides per l'usuari.

---

## Instruccions d'ús

1. Assegura't de tenir **Python 3.x** instal·lat.
2. Desa el codi en un fitxer anomenat `gestor_grups.py`.
3. Executa el fitxer:
   ```bash
   python gestor_grups.py

---

## Crèdits i autoria

- Fet per Eric Perez Diaz i Diego Rojano Zambrano