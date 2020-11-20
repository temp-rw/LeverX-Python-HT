# LeverX-Python-HT
## Task №1
Даны 2 файла (смотрите в прикрепленных файлах):
- students.json
- rooms.json

Необходимо написать скрипт, целью которого будет загрузка этих двух файлов, объединения их в список комнат где каждая комната содержит список студентов которые
находятся в этой комнате, а также последующую выгрузку их в формате JSON или XML. 

Необходима поддержка следующих входных параметров:
- students # путь к файлу студентов
- rooms # путь к файлу комнат
- format #  выходной формат (xml или json)

Ожидается использование ООП и SOLID

## Task №2
Расширить реализацию класса Version (см. файл task_2.py), чтобы позволять использовать его для
семантического сравнения.

Пример:
```
>>> Version('1.1.3') < Version('2.2.3')
True

>>> Version('1.3.0') > Version('0.3.0')
True

>>> Version('0.3.0b') < Version('1.2.42')
True

>>> Version('1.3.42') == Version('42.3.1')
False
```

## Task №3
Найти и исправить ошибку (смотри вложенный файл), оставив многопоточность.

```
from threading import Thread

a = 0


def function(arg):
    global a
    for _ in range(arg):
        a += 1


def main():
    threads = []
    for i in range(5):
        thread = Thread(target=function, args=(1000000,))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]
    print("----------------------", a)  # ???


main()
```