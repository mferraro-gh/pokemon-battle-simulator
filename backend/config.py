import os

# ---------------------------------------------------------------------------
# App-wide configuration — edit these values to change behaviour globally
# ---------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SQLite database file — lives next to this file
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'pokemon.db')}"

# PokeAPI base URL (no key needed)
POKEAPI_BASE = "https://pokeapi.co/api/v2"

# How many levels a Pokemon gains per win
XP_PER_WIN = 1

# Max level before a Pokemon cannot level up further
MAX_LEVEL = 100

# Chance (0-1) of receiving an egg after a win
EGG_DROP_CHANCE = 1.0  # TODO: tune this once battle logic is working

# Flask dev settings
DEBUG = True
SECRET_KEY = "change-me-in-production"
