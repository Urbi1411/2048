# Dokumentace projektu 2048

## Popis projektu

Projekt implementuje známou hru 2048 v jazyce Python pomocí knihovny tkinter.

Hráč spojuje stejná čísla pohybem po herní ploše, dokud nevytvoří hodnotu 2048.

---

## Funkce projektu

- grafické uživatelské rozhraní
- pohyb pomocí kláves WASD
- spojování políček
- generování nových čísel
- detekce výhry a prohry
- unit testy
- statická analýza kódu
- automatické generování dokumentace

---

## Struktura projektu

### `main.py`

Obsahuje:
- GUI aplikace,
- vykreslování herní plochy,
- zpracování klávesnice,
- hlavní herní smyčku.

### `logic.py`

Obsahuje herní logiku:
- pohyb políček,
- spojování hodnot,
- generování nových čísel,
- kontrolu výhry,
- kontrolu možných tahů.

### `test_logic.py`

Obsahuje automatické unit testy pro:
- pohyb,
- spojování,
- kontrolu herního stavu,
- generování čísel.

---

## Ovládání

| Klávesa | Akce |
|---|---|
| W | pohyb nahoru |
| A | pohyb doleva |
| S | pohyb dolů |
| D | pohyb doprava |

---

## Spuštění projektu

Instalace knihoven:

```bash
pip install -r requirements.txt