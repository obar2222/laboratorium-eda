import pandas as pd


def wczytaj_dane(sciezka):
    return pd.read_csv(
        sciezka,
        sep=";"
    )


def wyczysc_dane(df):
    wynik = df.copy()
    wynik["kanal"] = (
        wynik["kanal"]
        .astype(str)
        .str.strip()
        .str.lower()
    )
    return wynik


def podsumowanie(df):
    wartosci = df["wartosc"]
    if wartosci.empty:
        return {
            "liczba": 0,
            "suma": 0.0,
            "srednia": 0.0,
            "mediana": 0.0,
        }
    return {
        "liczba": int(len(wartosci)),
        "suma": float(wartosci.sum()),
        "srednia": float(wartosci.mean()),
        "mediana": float(wartosci.median()),
    }


def sprzedaz_wg_kanalu(df):
    wynik = (
        df.groupby("kanal")["wartosc"]
        .sum()
        .reset_index()
        .rename(columns={"wartosc": "suma_sprzedazy"})
    )
    return wynik
