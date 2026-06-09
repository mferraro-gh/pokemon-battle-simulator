"""
Battle routes

Endpoints:
    POST /api/battle/start   — start a battle, returns full result immediately
    GET  /api/battle/history/<trainer_id>  — past battle records
"""

from flask import Blueprint, jsonify, request
from database import get_db, schemas
from services import PokeAPIService, BattleEngine

battle_bp = Blueprint("battle", __name__, url_prefix="/api/battle")


@battle_bp.route("/start", methods=["POST"])
def start_battle():
    """
    Run a complete battle simulation and return the result.

    Request body:
        {
            "trainer_id": 1,
            "player_pokemon_id": 3,       -- DB id of the chosen pokemon
            "opponent_pokedex_id": 6      -- pokedex number of wild opponent
        }

    Response:
        {
            "winner": "player" | "opponent" | null,
            "rounds": [ ... ],
            "player_pokemon": { ... },
            "opponent_pokemon": { ... },
            "xp_gained": 50,
            "levelled_up": false,
            "evolved": false,
            "egg": null | { ... }
        }

    TODO:
        1. Parse trainer_id, player_pokemon_id, opponent_pokedex_id from JSON body
        2. Open DB session
        3. Load TrainerSchema and PokemonSchema from DB
        4. Fetch opponent data: PokeAPIService.get_pokemon_data(opponent_pokedex_id)
        5. Build Pokemon model objects from the DB rows and opponent data
        6. Create BattleEngine(trainer_model, player_model, opponent_model)
        7. result = engine.run(db)
        8. Persist battle log to BattleLogSchema
        9. Return jsonify(result)
    """
    pass


@battle_bp.route("/history/<int:trainer_id>", methods=["GET"])
def battle_history(trainer_id: int):
    """
    Return the last 20 battles for this trainer.

    TODO:
        1. Query BattleLogSchema where trainer_id=trainer_id
        2. Order by id descending, limit 20
        3. Return jsonify(list of battle log dicts)
    """
    pass
