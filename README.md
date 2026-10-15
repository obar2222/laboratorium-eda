# Analiza sprzedaży

Projekt wykonany w ramach laboratorium z eksploracji danych.

## Dane

Plik `data/sprzedaz.csv` zawiera 12 fikcyjnych zamówień (kolumny: `id`, `kanal`,
`segment`, `wartosc`). Wartość zamówienia podana jest w złotych. Nazwy kanałów
były zapisane niespójnie (wielkość liter, zbędne spacje), np. `Internet`,
`internet `, `SKLEP`.

## Wykonane analizy

- sprawdzenie struktury danych, typów, braków i duplikatów,
- ujednolicenie nazw kanałów (usunięcie spacji, małe litery),
- liczba zamówień, suma, średnia i mediana wartości zamówień,
- sprzedaż w podziale na kanały (tabela i wykres słupkowy),
- interaktywna aplikacja Streamlit z filtrem kanału i pobieraniem CSV.

## Technologie

Python, pandas, matplotlib, Jupyter, Streamlit, pytest, GitHub, Render

## Uruchomienie lokalne

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
pip install jupyterlab pytest

python -m pytest -q
streamlit run app.py
```

## Struktura projektu

```
app.py          aplikacja Streamlit
analiza.py      funkcje analityczne
data/           dane (sprzedaz.csv)
notebooks/      01_eksploracja.ipynb
tests/          testy pytest
render.yaml     konfiguracja wdrożenia
```

## Aplikacja

https://laboratorium-eda-b7ww.onrender.com

## Wnioski

1. Kanał internetowy generuje większość sprzedaży: 1490 zł wobec 760 zł w sklepie
   (ok. 66% całości), mimo że oba kanały mają po 6 zamówień.
2. Średnia wartość zamówienia w internecie (ok. 248,33 zł) jest prawie dwukrotnie
   wyższa niż w sklepie (ok. 126,67 zł); największe zamówienia (310 zł i 400 zł)
   pochodzą z internetu.
