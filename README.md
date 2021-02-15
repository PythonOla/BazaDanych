# Baza danych (projekt zaliczeniowy)

## Temat projektu (ze strony)
Baza danych książek, płyt, itp. Baza powinna być zapisywana do pliku (txt, CSV, JSON). Operacje na bazie: wstawianie, usuwanie, wyszukiwanie, listowanie.

## Ogólnie

- Czego dokładnie baza? Jest to baza danych dla administratora portalu takiego jak facebook lub nasza klasa
- Co robimy z danymi? Wstawianie, usuwanie, wyszukiwanie (względem id, imienia i nazwiska), listowanie
- Podstawowa reprezentacja graficzna

## Dependencja
- Kivy v2.0.0
- Python 3.8


## Technikalia 

- Jaki format bazy? JSON 
- Jaka biblioteka do interfejsu? Kivy


### Format danych

- users
    - id
    - name
    - surname
    - birth date
    - friends
    - photos
    - like (comments, posts)
    - posts
    - comments
    - average daily activity
    - joined on

- commets
    - id
    - first comment and reply comment
    - likes 
    - text
    - parent id (previous post/comment id)

- likes
    - id
    - comment likes
    - post likes
    - parent id 

- posts
    - id
    - text
    - attachments
    - likes

### Co mam?
- Profile
- Modele
- Kontrolery
- Zmiany danych w bazie
- Widoki

