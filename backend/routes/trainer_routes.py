"""
Trainer / User routes

Endpoints:
    POST   /api/trainer             — create account
    GET    /api/trainer/<id>        — get trainer info + party + eggs
    GET    /api/trainer/<id>/party  — list party pokemon
    POST   /api/trainer/<id>/hatch/<egg_id>  — hatch an egg
    PUT    /api/trainer/<id>/party  — move pokemon between party and box
"""

from flask import Blueprint, jsonify, request
from database import get_db, schemas

trainer_bp = Blueprint("trainer", __name__, url_prefix="/api/trainer")


@trainer_bp.route("", methods=["POST"])
def create_trainer():
    """
    Create a new trainer account.

    Request body: { "username": "ash" }

    TODO:
        1. Parse username from request.get_json()
        2. Validate: username must be non-empty string
        3. Open a DB session (use `with get_db() as db:`)
        4. Check username not already taken (db.query(TrainerSchema).filter_by(username=...).first())
        5. Create TrainerSchema row, db.add, db.commit, db.refresh
        6. Give the trainer a starter Pokemon:
               randomly pick one of 1 (Bulbasaur), 4 (Charmander), 7 (Squirtle)
               call PokeAPIService.get_pokemon_data to fetch it
               create PokemonSchema row, add to DB
        7. Return jsonify(trainer data), 201
    """
    pass


@trainer_bp.route("/<int:trainer_id>", methods=["GET"])
def get_trainer(trainer_id: int):
    """
    Return trainer profile with party, box, and eggs.

    TODO:
        1. Query TrainerSchema by trainer_id
        2. If not found return 404
        3. Return jsonify with trainer data + pokemon list + egg list
    """
    pass


@trainer_bp.route("/<int:trainer_id>/party", methods=["GET"])
def get_party(trainer_id: int):
    """
    Return only the active party (in_party=True).

    TODO:
        1. Query PokemonSchema where trainer_id=trainer_id AND in_party=True
        2. Return jsonify(list of pokemon dicts)
    """
    pass


@trainer_bp.route("/<int:trainer_id>/hatch/<int:egg_id>", methods=["POST"])
def hatch_egg(trainer_id: int, egg_id: int):
    """
    Hatch an egg and add the baby Pokemon to the trainer's collection.

    TODO:
        1. Find the EggSchema row (return 404 if not found or already hatched)
        2. Fetch pokemon data from PokeAPI for egg.pokedex_id
        3. Create a PokemonSchema row at level 1
        4. Mark egg as hatched (egg.is_hatched = True)
        5. db.commit()
        6. Return the new pokemon data
    """
    pass


@trainer_bp.route("/<int:trainer_id>/party", methods=["PUT"])
def update_party(trainer_id: int):
    """
    Swap a Pokemon between party and box.

    Request body: { "pokemon_id": 5, "in_party": true }

    TODO:
        1. Parse pokemon_id and in_party from request body
        2. If moving to party: check party isn't already full (max 6)
        3. Update PokemonSchema.in_party field
        4. db.commit()
        5. Return updated party list
    """
    pass
