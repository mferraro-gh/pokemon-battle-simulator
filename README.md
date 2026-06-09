# ⚡ Pokemon Battle Simulator

A learning project for practicing **Object-Oriented Programming** in Python.
Battle Pokemon, level them up, evolve them, and earn eggs — all powered by the
free [PokeAPI](https://pokeapi.co/).

> **Note:** This is a learning scaffold. The structure, classes, comments, and
> method signatures are all in place, but the method bodies are left as `TODO`s
> for you to implement. Each one has a docstring explaining exactly what to do.

---

## ✨ Features (to build)

- 🔍 Search the Pokedex and add Pokemon to your party
- ⚔️ Turn-based battle simulator with type effectiveness
- 📈 Level up and evolve your Pokemon by winning
- 🥚 Win a random base-form egg after each victory, then hatch it
- 💾 Persistent storage with SQLite — your team is saved between sessions
- 👤 Trainer accounts with party + PC box management

---

## 🧱 Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Backend   | Python, Flask, Flask-CORS           |
| Database  | SQLite via SQLAlchemy (ORM)         |
| Frontend  | Vanilla HTML / CSS / JavaScript     |
| Data      | [PokeAPI](https://pokeapi.co/)      |

---

## 📁 Project Structure

```
pokemon-battle-simulator/
├── backend/
│   ├── app.py                 # Flask entry point
│   ├── config.py              # Tuneable constants (XP, egg chance, etc.)
│   ├── models/                # OOP classes — the heart of the project
│   │   ├── pokemon.py         #   Class, Encapsulation, Properties
│   │   ├── move.py            #   Single Responsibility
│   │   ├── egg.py             #   Composition ("has-a")
│   │   ├── trainer.py         #   Aggregation
│   │   └── battle.py          #   State Machine + Value Object
│   ├── database/
│   │   ├── db.py              # SQLAlchemy engine & session
│   │   └── schemas.py         # DB tables (ORM inheritance)
│   ├── services/
│   │   ├── pokeapi_service.py # All PokeAPI HTTP calls
│   │   ├── battle_engine.py   # Coordinates a full battle (Facade)
│   │   └── evolution_service.py
│   └── routes/                # Flask API blueprints
│       ├── pokemon_routes.py
│       ├── battle_routes.py
│       └── trainer_routes.py
├── frontend/
│   ├── index.html             # Team / home screen
│   ├── battle.html            # Battle arena
│   ├── pokedex.html           # Search & catch
│   ├── css/
│   ├── js/
│   │   └── sprites.js         # Sprite resolver (local-vs-remote switch)
│   └── assets/
│       └── sprites/           # Local sprite archive (see its README)
├── scripts/
│   └── download_sprites.py    # Fetch sprites from the PokeAPI archive
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
cd backend
pip install -r ../requirements.txt
```

### 2. Run the backend

```bash
python app.py
```

The API starts at **http://localhost:5000** and creates `pokemon.db` on first run.

### 3. Open the frontend

Either open `frontend/index.html` directly in your browser, or serve it:

```bash
cd frontend
python -m http.server 8000
```

Then visit **http://localhost:8000**.

---

## 🖼️ Sprites

The app uses remote PokeAPI sprite URLs out of the box, so there's nothing to
download to get started. When you want to bundle your **own local sprite
archive**, the structure is already in place:

```bash
python scripts/download_sprites.py     # populate frontend/assets/sprites/
```

Then flip one flag in [`frontend/js/sprites.js`](frontend/js/sprites.js):

```js
export const USE_LOCAL_SPRITES = true;
```

Every sprite in the app resolves through `SpriteResolver`, so that single switch
flips the whole UI over to local files (with automatic fallback to remote if a
file is missing). Full details in
[`frontend/assets/sprites/README.md`](frontend/assets/sprites/README.md).

---

## 🎓 OOP Concepts Covered

| Concept           | Where to find it                          |
|-------------------|-------------------------------------------|
| **Class**         | `models/pokemon.py`, every model          |
| **Encapsulation** | Private attrs + `@property` in `pokemon.py`|
| **Inheritance**   | `database/schemas.py` (all extend `Base`) |
| **Composition**   | `egg.py` contains data to build a Pokemon  |
| **Aggregation**   | `trainer.py` holds collections of Pokemon |
| **State Machine** | `battle.py` (pending → in_progress → finished) |
| **Facade**        | `services/battle_engine.py`               |
| **SRP / DRY**     | service layer separation                  |

---

## 🛠️ Suggested Implementation Order

1. `models/pokemon.py` — stat formulas, `take_damage`, `heal`, `gain_xp`
2. `models/move.py` — PP management (quick warm-up)
3. `models/egg.py` — the `hatch()` method
4. `models/trainer.py` — party management
5. `models/battle.py` — battle loop + damage calculation
6. `services/pokeapi_service.py` — `get_pokemon_data()` first
7. `services/battle_engine.py` — wire it all together
8. `routes/*` — Flask endpoints
9. `frontend/js/*` — implement the `TODO` stubs

---

## 📜 License

MIT — free to use, learn from, and modify.

---

*Built as an OOP learning exercise. Pokemon and all related names are
trademarks of Nintendo/Game Freak. This project is non-commercial and for
educational purposes only.*
