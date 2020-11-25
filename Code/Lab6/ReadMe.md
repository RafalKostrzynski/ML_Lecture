# `Pliki`

### Zadania zostały wykonane na podstawie tutoriala ze strony:
### https://realpython.com/read-write-files-python/

## Aby zobaczyć wywołanie metod wejdź [do pliku .pynb](Lab6.ipynb)


# Podstawowe operacje
## Otworzenie pliku:
`file = open('files/first_file_kostrzynski.txt')`

[Pierwszy plik tekstowy tutaj](files/first_file_kostrzynski.txt)

#
### Metoda Try-Finally do zamknięcia pliku
#### Jest to zabezpieczenie się metodą Try-Finally, przez co nawet w momencie błędu zostanie wykonana metoda close() w bloku Finally
`reader = open("files/first_file_kostrzynski.txt")
try:
    # miejsce na działania na pliku
finally:
    reader.close()
`

#
## Zamknięcie pliku metodą wyrażenia "with" 
#### Jest to preferowane zamykanie pliku. Plik zamyka się automatycznie po wyjściu z wyrażenia "with"
`with open("files/first_file_kostrzynski.txt") as reader:
    # miejsce na działania na pliku
`

#
## Wykorzystanie arumentu pozycyjnego
#### Drugi argument metody wskazuje tryb otworzenia pliku. Istnieją następujące tryby:
* 'r' - Plik wyłącznie do odczytu
* 'w' - Plik w trybie do zapisu
* 'rb' - Plik w trybie binarny w formacie BufferedReader
* 'wb' - Plik w trybie binarnym w foracie BufferedWriter

`with open('files/first_file_kostrzynski.txt', 'r') as reader:
    reader.read()`

# Typy plików
## Typy otwartych plików
#### Używane zostają trzy formaty plików TextIOWrapper,BufferedReader oraz BufferedWriter
`with open('files/first_file_kostrzynski.txt') as file:
    print(type(file)) #TextIOWrapper
with open('files/first_file_kostrzynski.txt', 'r') as file:
    print(type(file)) #TextIOWrapper
with open('files/first_file_kostrzynski.txt', 'w') as file:
    print(type(file)) #TextIOWrapper
with open('files/first_file_kostrzynski.txt', 'rb') as file:
    print(type(file)) #BufferedReader
with open('files/first_file_kostrzynski.txt', 'wb') as file:
    print(type(file)) #BufferedWriter`

#
## Typ plików raw
#### Typem tych plików jest FileIO. Pliki otwierane są w następujący sposób:
`
with open('files/first_file_kostrzynski.txt', 'rb',buffering=0) as file:
    print(type(file)) 
`

# Czytanie plików
## Wczytanie całego pliku
#### Do wczytania pliku wykorzystujemy metodęread()
#### [Plik tylko do wczytania danych tutaj](files/read_only_file_kostrzynski.txt) 
`with open('files/read_only_file_kostrzynski.txt', 'r') as file:
    print(file.read())
`

#
## Wczytanie po pięć bajtów przy każdym wywołaniu metody readline()
`with open('files/read_only_file_kostrzynski.txt','r') as readable:
    for i in range(7):
        print(readable.readline(5))`

#
## Wczytanie całego pliku wykorzystując metodę readlines()
`with open('files/read_only_file_kostrzynski.txt','r') as readable:
    print(readable.readlines())
`

#
## Utworzenie listy z pliku
`f=open('files/read_only_file_kostrzynski.txt')
list(f)`

#
## Iteracja po każdym wierszu pliku
`with open('files/read_only_file_kostrzynski.txt','r') as readable:
    line = readable.readline()
    while line !='':
        print(line,end='')
        line = readable.readline()
`

#
## Wykorzystanie readlines() do iteracji
`with open('files/read_only_file_kostrzynski.txt', 'r') as reader:
     for line in reader.readlines():
         print(line, end='')`

#
## Iteracja po obiekcie pliku
#### Python rozpoznaje wiersze w pliku w pozwala na iterowanie po obiekcie 'line'
`with open('files/read_only_file_kostrzynski.txt', 'r') as reader:
     for line in reader:
         print(line, end='')`

# Pisanie w pliku
## Wykorzystanie metody write()
`with open('files/write_write_file_kostrzynski.txt', 'w') as writer:
    for breed in reversed(read_only_text):
        writer.write(breed)`

[Wynik metody write tutaj](files/write_write_file_kostrzynski.txt)

#
## Wykorzystanie metody writeline()
`with open('files/writeline_write_file_kostrzynski.txt', 'w') as writer:
    writer.writelines(reversed(read_only_text))`

[Wynik metody writeline tutaj](files/writeline_write_file_kostrzynski.txt)

# Podejście bajtowe
## Wczytanie pliku
`with open('files/working_with_bytes_kostrzynski.txt', 'rb') as reader:
     print(reader.readline())`

[Plik working with bytes tutaj](files/working_with_bytes_kostrzynski.txt)

#
## Wczytanie pliku jpg
`with open('files/nikexoffwhite_kostrzynski.jpg', 'rb') as byte_reader:
     print(byte_reader.read(1))
     print(byte_reader.read(3))
     print(byte_reader.read(2))
     print(byte_reader.read(1))
     print(byte_reader.read(1))
`

Obraz w formacie png:

![NikeXOff](files/nikexoffwhite_kostrzynski.jpg)

# Dos2Unix.py
## str2unix
#### Metoda konwertuje zakończenia \r\n na \n
`def str2unix(input_str: str) -> str:
    r_str = input_str.replace('\r\n', '\n')
    return r_str`

#
## dos2unix
#### konwertuje plik posiadający zakończenia Dos\owe na linuxowe
`with open(source_file, 'r') as reader:
        dos_content = reader.read()
    unix_content = str2unix(dos_content)
    with open(dest_file, 'w') as writer:
        writer.write(unix_content)`

#
## Main

Metoda nie działa z powodu błędu parsera
`if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script that converts a DOS like file to an Unix like file",
    )
    parser.add_argument(
        'source_file',
        help='The location of the source '
    )
    parser.add_argument(
        '--dest_file',
        help='Location of dest file (default: source_file appended with `_unix`',
        default=None
    )
    args = parser.parse_args()
    s_file = args.source_file
    d_file = args.dest_file
    if d_file is None:
        file_path, file_extension = os.path.splitext(s_file)
        d_file = f'{file_path}_unix{file_extension}'
    dos2unix(s_file, d_file)`
    
[Plik file with doc signs tutaj](files/file_with_doc_signs_kostrzynski.txt)

[Tutaj powinien wygenerować się plik](files/generated_file_kostrzynski.txt)

#
## Dołączanie do pliku
#### "Słowo Beagle zostanie dołączone na końcu pliku tipps and tricks"
`with open('files/tipps_and_tricks_kostrzynski.txt', 'a') as a_writer:
    a_writer.write('\nBeagle')
with open('files/tipps_and_tricks_kostrzynski.txt', 'r') as reader:
     print(reader.read())`

[Plik tipps and tricks tutaj](files/tipps_and_tricks_kostrzynski.txt)

#
## Pracowanie z dwoma plikami w tym samym czasie
#### Zapisuje odwrócone lorem ipsum do pliku reversed lorem ipsum
`d_path = 'files/tipps_and_tricks_kostrzynski.txt'
d_r_path = 'files/reversed_lorem_ipsum_kostrzynski.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    lorem_ipsum = reader.readlines()
    writer.writelines(reversed(lorem_ipsum))`

[Plik tipps and tricks tutaj](files/tipps_and_tricks_kostrzynski.txt)

[Plik reversed lorem ipsum tutaj](files/reversed_lorem_ipsum_kostrzynski.txt)

#
## Utworzenie nowej klasy menadżera kontekstu
`class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None
    def __enter__(self):
        self.__file_object = open(self.__path)
        return self
    def __exit__(self, type, val, tb):
        self.__file_object.close()
`

#
## Otworzenie pliku png parsowania przy użyciu nowej klasy
`class PngReader:
    _expected_magic = b'\x89PNG\r\n\x1a\n'
    def __init__(self, file_path):
        if not file_path.endswith('.png'):
            raise NameError("File must be a '.png' extension")
        self.__path = file_path
        self.__file_object = None
    def __enter__(self):
        self.__file_object = open(self.__path, 'rb')
        magic = self.__file_object.read(8)
        if magic != self._expected_magic:
            raise TypeError("The File is not a properly formatted .png file!")
        return self
    def __exit__(self, inner_type, val, tb):
        self.__file_object.close()
    def __iter__(self):
        return self
    def __next__(self):
        initial_data = self.__file_object.read(4)
        if self.__file_object is None or initial_data == b'':
            raise StopIteration
        else:
            chunk_len = int.from_bytes(initial_data, byteorder='big')
            chunk_type = self.__file_object.read(4)
            chunk_data = self.__file_object.read(chunk_len)
            chunk_crc = self.__file_object.read(4)
            return chunk_len, chunk_type, chunk_data, chunk_crc
`

#
## Wykorzystanie nowo utworzonej klasy
`with PngReader('files/nikexoffwhite_kostrzynski.png') as reader:
     for l, t, d, c in reader:
         print(f"{l:05}, {t}, {c}")
`

Obraz w formie png

![NikeXOffPng](files/nikexoffwhite_kostrzynski.png)

