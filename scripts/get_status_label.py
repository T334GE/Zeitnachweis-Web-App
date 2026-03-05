def get_status_label(status_code: str) -> str:
    status_mapping = {
        "ANWESEND": "Anwesend",
        "URLAUB": "Urlaub",
        "KRANK": "Krank",
        "KIND_KRANK": "Kind krank",
        "SCHULE": "Schule",
        "FREI_FEIERTAG": "Frei/Feiertag",
        "FEIERTAG_AUTO": "Feiertag",
        "ENTSCHULDIGT": "Entschuldigt",
        "PRAKTIKUM_NICHT_BEGONNEN": "Nicht Begonnen",
        "FERTIG": "Fertig",
        "UNBEKANNT": "Unbekannt",
        "KEIN_EINTRAG": "Wochenende",
    }
    return status_mapping.get(status_code.upper(), status_code)
