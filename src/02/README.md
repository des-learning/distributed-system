pipe digunakan untuk mengirimkan apa yang ditulis ke stdout proses sebelah kiri
ke stdin proses sebelah kanan operator pipe `|`

contoh:
```bash
python cat.py upper.py | python nl.py
```

operator redirection digunakan untuk mengubah stdin atau stdout sebuah proses.

operator stdin redirection:
```bash
python nl.py < upper.py
```

operator stdout redirection:
```bash
python cat.py upper.py | python nl.py > hasil.txt
```
