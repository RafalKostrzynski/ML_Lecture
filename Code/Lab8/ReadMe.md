# Praca z formatem JSON oraz CSV

#### Zadania zostały wykonane na podstawie tutoriali ze stron:
* https://realpython.com/python-json/
* https://realpython.com/python-csv/

#### Aby zobaczyć wyniki metod przejdź do poszczególnych plikó .ipynb (Referencja na początku każdego rozdziału)

# Spis treści:
* [JSON](#JSON)
    * [Importy](#Importy-JSON:)
    * [Utworzenie pliku o formacie JSON w pamięci ](#Utworzenie-pliku-o-formacie-JSON-w-pamięci)
    * [Zapisanie pliku w formacie JSON przy wykorzystaniu metody dump()](#Zapisanie-pliku-w-formacie-JSON-przy-wykorzystaniu-metody-dump())
    * [Przekonwertowanie obiektu JSON na obiekt typu Python native str](#Przekonwertowanie-obiektu-JSON-na-obiekt-typu-Python-native-str)
    * [Specyfikacja stylu wcinania](#Specyfikacja-stylu-wcinania)
    * [Zakodowanie oraz odkodowanie obiektu typu JSON](#Zakodowanie-oraz-odkodowanie-obiektu-typu-JSON)
    * [Deserializacja](#Deserializacja)
    * [Deserializacja obiektu typu String](#Deserializacja-obiektu-typu-String)
    * [Utworzenie zapytania JSON oraz deserializacja wyniku zapytania](#Utworzenie-zapytania-JSON-oraz-deserializacja-wyniku-zapytania)
    * [Znalezienie użytkownika który utworzył najdłuższy post](#Znalezienie-użytkownika-który-utworzył-najdłuższy-post)
    * [Odfiltrowanie najdłuższego postu pięciu użytkowników z najdłuższymi postami](#Odfiltrowanie-najdłuższego-postu-pięciu-użytkowników-z-najdłuższymi-postami)
    * [Zakodowanie oraz odkodowanie obiektów niestandardowych](#Zakodowanie-oraz-odkodowanie-obiektów-niestandardowych)
    * [Poprawne zakodowanie złożonych niestandardowych obiektów za pomocą metody](#Poprawne-zakodowanie-złożonych-niestandardowych-obiektów-za-pomocą-metody)
    * [Zakodowanie przy pomocy nadpisania metody default() obiektu JSONEncoder](#Zakodowanie-przy-pomocy-nadpisania-metody-default()-obiektu-JSONEncoder)
    * [Odkodowanie niestandardowego obiektu](#Odkodowanie-niestandardowego-obiektu)
    * [Weryfikacja klucza](#Weryfikacja-klucza)
    
* [CSV](#CSV)
    * [Importy CSV](#Importy-CSV:)
    * [Wczytanie pliku CSV](#Wczytanie pliku CSV)
    * [Wczytanie pliku CSV do słownika](#Wczytanie pliku CSV do słownika)
    * [Utworzenie/Zapisanie pliku CSV](#Utworzenie/Zapisanie pliku CSV)
    * [Utworzenie/Zapisanie pliku CSV ze słownika wraz z przykładowymi danymi](#Utworzenie/Zapisanie pliku CSV ze słownika wraz z przykładowymi danymi)
    * [Parsowanie skomplikowanych danych pliku CSV przy użyciu biblioteki Pandas](#Parsowanie skomplikowanych danych pliku CSV przy użyciu biblioteki Pandas)
    * [Rodzaje danych](#Rodzaje danych)
    * [Zmiana kolumny index tablicy DataFrame](#Zmiana kolumny index tablicy DataFrame)
    * [Naprawa typu kolumny Birthday](#Naprawa typu kolumny Birthday)
    * [Deklaracja nazw kolumn oraz zmiana typu danej przy wczytaniu pliki CSV](#Deklaracja nazw kolumn oraz zmiana typu danej przy wczytaniu pliki CSV)
    * [Zapisanie / Utworzenie pliku CSV przy wykorzystaniu biblioteki Pandas](#Zapisanie/Utworzenie pliku CSV przy wykorzystaniu biblioteki Pandas)
    
# JSON
#### Aby zobaczyć kod źródłowy kliknij [tutaj](./Lab8_json.ipynb)


### Importy JSON:
```
import json
import requests
```
### Utworzenie pliku o formacie JSON w pamięci 
```
data={
    "postId": 1,
    "id": 3,
    "name": "odio adipisci rerum aut animi",
    "email": "Nikita@garfield.biz",
    "body": "quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione"
  }
```
### Zapisanie pliku w formacie JSON przy wykorzystaniu metody dump()
[plik JSON Tutaj](json_files/data_file.json)
```
with open("json_files/data_file.json", "w") as write_file:
    json.dump(data, write_file)
```
### Przekonwertowanie obiektu JSON na obiekt typu Python native str
```
json.dumps(data)
```
### Specyfikacja stylu wcinania
```
json.dumps(data, indent=4)
```
## Deserializacja obiektu JSON
### Zakodowanie oraz odkodowanie obiektu typu JSON 

Konwersja typów nie jest idealna, przez co obustronna konwersja może prowadzić do niezgodności danych
```
new_shoes = ("Price",299)
encoded_shoes = json.dumps(new_shoes)
decoded_shoes = json.loads(encoded_shoes)

```
### Deserializacja
[plik JSON Tutaj](json_files/data_file.json)
```
with open("json_files/data_file.json", "r") as read_file:
    data = json.load(read_file)
```
### Deserializacja obiektu typu String
W pierwszym kroku tworzymy obiekt typu String z wartością docelowego JSONa
Po czym wykonujemy deserializację metodą json.loads()
```
json_string = """
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
"""
data = json.loads(json_string)
```
### Utworzenie zapytania JSON oraz deserializacja wyniku zapytania
```
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = json.loads(response.text)
```
### Znalezienie użytkownika który utworzył najdłuższy post

Utworzenie listy 
```
posts_by_user={}
```
Znalezienie najdłuższego posta każdego użytkownika
```
for post in posts:
    try:
        if len(post["body"])> posts_by_user[post["userId"]]:
            posts_by_user[post["userId"]]=len(post["body"])
    except KeyError:
            posts_by_user[post["userId"]]=len(post["body"])
```
Posortowanie wyniku
```
longest_post = sorted(posts_by_user.items(),
                      key=lambda x:x[1], reverse=True)
```
Znalezienie najdłuższego posta oraz użytkownika
Metoda również uwzględnia przypadek w którym istnieje więcej niż 1 postów o największej długości 
```
users_longest_posts=[]
for longest in longest_post:
    if longest_post[0][1]>longest[1]:
        break
    users_longest_posts.append(str(longest[0]))
```
Utworzenie Stringa z uzyskanych danych
```
user_string = " and ".join(users_longest_posts)
s = "s" if len(users_longest_posts)>1 else ""
```
### Odfiltrowanie najdłuższego postu pięciu użytkowników z najdłuższymi postami 

Utworzenie listy z pięcioma najdłuższymi postami
```
users = longest_post[:5]
```
Metoda filtrująca na podstawie listy z najdłuższami postami
```
def keep(post):
    counter = False
    for user in users:
        if user[1] == len(post["body"]) and post["userId"] == user[0]:
            counter = True
    return counter
```
Wykonanie przefiltrowania danych oraz zapisanie wyniku do [pliku](./json_files/filtered_data_file.json)
```
with open("json_files/filtered_data_file.json","w") as data_file:
    filtered_posts = list(filter(keep,posts))
    json.dump(filtered_posts,data_file,indent=2)

```
### Zakodowanie oraz odkodowanie obiektów niestandardowych

##### Poniższy kod powinien wyrzucić błąd "TypeError" ponieważ python nie jest w stanie domyślnie zakodować niestandardowych obiektów 

Utworzenie niestandardowego obiektu Elf
```
class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]
```
Próba zakodowania nowego obiektu oraz obsługa wyjątku
```
try:
    elf = Elf(level=4)
    json.dumps(elf)
except TypeError as type_error:
    print("A TypeError has occurred!")
    print("Message: ",type_error.args[0])

```
### Poprawne zakodowanie złożonych niestandardowych obiektów za pomocą metody
```
def encode_complex(z):
    if isinstance(z,complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

```
### Zakodowanie przy pomocy nadpisania metody default() obiektu JSONEncoder
```
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)

```
Możliwe wywołania kodowania
```
json.dumps(2 + 5j, cls=ComplexEncoder)
encode = ComplexEncoder()
encode.encode(3 + 6j)
```
### Odkodowanie niestandardowego obiektu
```
complex_json = json.dumps(4+17J,cls=ComplexEncoder)
json.loads(complex_json)
```
### Weryfikacja klucza 
Definicja metody 
```
def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct
```
Wywołanie oraz odkodowanie [pliku](./json_files/complex_data.json)
```
with open("json_files/complex_data.json") as complex_data:
    data=complex_data.read()
    z=json.loads(data, object_hook=decode_complex)

```
# CSV
#### Aby zobaczyć kod źródłowy kliknij [tutaj](./Lab8_csv.ipynb)

### Importy CSV:
```
import csv
import pandas
```
### Wczytanie pliku CSV

Otworzenie oraz proste zapisanie pliku CSV do pamięci

[Plik dostępny tutaj](./csv_files/lorem_ipsum.txt)

```
with open('csv_files/lorem_ipsum.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

```
Metoda wypisująca kolumny oraz wiersze oraz zliczająca wszystkie wiersze
```
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a Latin word {row[1]} is really important, '
                  f'and means a lot {row[2]}.{row[3]} was generated. '
                  f'{row[4]}, I really have no idea what it means')
            line_count += 1
    print(f'Processed {line_count} lines.')

```
### Wczytanie pliku CSV do słownika
Metoda różni się tylko wywołaniem oraz odwoływaniem się do wierszy poprzez nazwy kolumn

[Plik dostępny tutaj](./csv_files/lorem_ipsum.txt)

```
with open('csv_files/lorem_ipsum.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row["First"]} is a Latin word {row["Second"]} is really important, '
                  f'and means a lot {row["Third"]}.{row["Fourth"]} was generated. '
                  f'{row["Fifth"]}, I really have no idea what it means')
            line_count += 1
    print(f'Processed {line_count} lines.')

```
### Utworzenie/Zapisanie pliku CSV

[Plik dostępny tutaj](./csv_files/public_opinion.csv)

```
with open('csv_files/public_opinion.csv', mode='w') as public_opinion_file:
    public_opinion_writer = csv.writer(public_opinion_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    public_opinion_writer.writerow(['Person', 'Job', 'Month'])
    public_opinion_writer.writerow(['Max Musterman', 'Consultant', 'January'])

```

### Utworzenie/Zapisanie pliku CSV ze słownika wraz z przykładowymi danymi

[Plik dostępny tutaj](./csv_files/public_opinion2.csv)

```
with open('csv_files/public_opinion2.csv', mode='w') as csv_file:
    fieldnames = ['person_name', 'job', 'employment_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'person_name': 'Max Musterman', 'job': 'Consultant', 'employment_month': 'January'})
    writer.writerow({'person_name': 'Pawel Kowalski', 'job': 'Nurse', 'employment_month': 'February'})

```

### Parsowanie skomplikowanych danych pliku CSV przy użyciu biblioteki Pandas

[Plik dostępny tutaj](./csv_files/random_csv_data.csv)

```
df = pandas.read_csv("csv_files/random_csv_data.csv")
```

### Rodzaje danych

Pola "Birthday" i "Salary" nie powinny być typu String prawda?
Wartość dftypes wypisaje typ String jako "Object"
```
print(df.dtypes)

```

### Zmiana kolumny index tablicy DataFrame

[Plik dostępny tutaj](./csv_files/random_csv_data.csv)

```
df = pandas.read_csv("csv_files/random_csv_data.csv",index_col="Full name")

```


### Naprawa typu kolumny Birthday

Zmuszamy bibliotekę pandas do sparsowania kolumny "Birthday" przy pomocy "parse_date"

[Plik dostępny tutaj](./csv_files/random_csv_data.csv)

```
df = pandas.read_csv("csv_files/random_csv_data.csv",index_col="Full name", parse_dates=['Birthday'])
```


### Deklaracja nazw kolumn oraz zmiana typu danej przy wczytaniu pliki CSV

[Plik dostępny tutaj](./csv_files/random_csv_data.csv)

```
df = pandas.read_csv('csv_files/random_csv_data.csv',
            index_col='Full name',
            parse_dates=['Birthday_changes'],
            header=0,
            names=['Full name', 'Age_changed','Birthday_changes', 'Email_changed','City_changed','Salary_changed'])
```


### Zapisanie/Utworzenie pliku CSV przy wykorzystaniu biblioteki Pandas

Zapisujemy poprzednio wczytany i zmodyfikowany plik CSV jako zmienną df

[Plik dostępny tutaj](./csv_files/random_csv_data_modified.csv)

```
df.to_csv('csv_files/random_csv_data_modified.csv')
```
