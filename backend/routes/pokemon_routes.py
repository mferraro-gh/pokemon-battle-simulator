"""
Pokemon routes

Endpoints:
    GET  /api/pokemon/search?q=<query>      — search PokeAPI by name
    GET  /api/pokemon/<pokedex_id>          — get data for one pokemon
    GET  /api/pokemon/owned/<trainer_id>    — all pokemon owned by a trainer
    POST /api/pokemon/catch                 — add a pokemon to trainer's collection
    PUT  /api/pokemon/<pokemon_db_id>       — update (e.g. after level-up)
    DELETE /api/pokemon/<pokemon_db_id>     — release a pokemon
"""

from flask import Blueprint, jsonify, request
from database import get_db, schemas
from services import PokeAPIService

pokemon_bp = Blueprint("pokemon", __name__, url_prefix="/api/pokemon")


@pokemon_bp.route("/search", methods=["GET"])
def search_pokemon():
    """
    Search PokeAPI for Pokemon by name fragment.

    Query param: ?q=char  → returns Charmander, Charmeleon, Charizard

    TODO:
        1. q = request.args.get("q", "")
        2. If not q return 400 with an error message
        3. results = PokeAPIService.search_pokemon(q)
        4. Return jsonify(results)
    """
    pass


@pokemon_bp.route("/<int:pokedex_id>", methods=["GET"])
def get_pokemon(pokedex_id: int):
    """
    Fetch a single Pokemon's data from PokeAPI.

    TODO:
        1. data = PokeAPIService.get_pokemon_data(pokedex_id)
        2. Return jsonify(data)
    """
    pass


@pokemon_bp.route("/owned/<int:trainer_id>", methods=["GET"])
def get_owned_pokemon(trainer_id: int):
    """
    Return all Pokemon rows in the DB owned by trainer_id.

    TODO:
        1. Query PokemonSchema filtered by trainer_id
        2. Return jsonify(list of pokemon dicts)
    """
    pass


@pokemon_bp.route("/catch", methods=["POST"])
def catch_pokemon():
    """
    Add a Pokemon to a trainer's collection (used for the starter pick or debug).

    Request body: { "trainer_id": 1, "pokedex_id": 25 }

    TODO:
        1. Parse trainer_id, pokedex_id
        2. PokeAPIService.get_pokemon_data to fetch stats
        3. Create PokemonSchema row at level 5
        4. Add to DB, commit
        5. Return new pokemon row as JSON, 201
    """
    pass


@pokemon_bp.route("/<int:pokemon_db_id>", methods=["DELETE"])
def release_pokemon(pokemon_db_id: int):
    """
    Release (delete) a Pokemon from a trainer's collection.

    TODO:
        1. Find PokemonSchema by id
        2. Check the trainer still has at least 1 other non-fainted pokemon
           (never let trainer end up with nothing usable)
        3. db.delete(pokemon_row), db.commit()
        4. Return 204 No Content
    """
    pass
