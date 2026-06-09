"""
Service layer: all PokeAPI network calls live here.

OOP CONCEPT: SINGLE RESPONSIBILITY PRINCIPLE (SRP)
This file has ONE job: talk to the PokeAPI.  No battle logic, no DB writes.
If the API ever changes you only touch this file.
"""

import requests
from config import POKEAPI_BASE


class PokeAPIService:
    """
    Static helper class for fetching Pokemon data from https://pokeapi.co/api/v2

    All methods are @staticmethod because this service holds no state —
    every call is independent.  You never need to do PokeAPIService() first.
    """

    @staticmethod
    def get_pokemon_data(pokedex_id: int) -> dict:
        """
        Fetch full data for one Pokemon and return a normalised dict.

        Returns:
            {
                "pokedex_id": int,
                "name": str,
                "types": list[str],
                "sprite_url": str,
                "base_stats": { "hp": int, "attack": int, "defense": int, "speed": int },
                "evolution_id": int | None,
                "evolution_level": int | None,
            }

        TODO:
            1. GET f"{POKEAPI_BASE}/pokemon/{pokedex_id}"
            2. Parse response JSON:
                - name         → data["name"]
                - types        → [t["type"]["name"] for t in data["types"]]
                - sprite_url   → data["sprites"]["front_default"]
                - base_stats   → iterate data["stats"] and map:
                                    "hp"      from stat name "hp"
                                    "attack"  from "attack"
                                    "defense" from "defense"
                                    "speed"   from "speed"
            3. Call get_evolution_data(pokedex_id) to get evolution info
            4. Return the assembled dict

        Hint — response stat structure:
            data["stats"] = [
                {"base_stat": 45, "stat": {"name": "hp"}},
                {"base_stat": 49, "stat": {"name": "attack"}},
                ...
            ]
        """
        pass

    @staticmethod
    def get_evolution_data(pokedex_id: int) -> tuple[int | None, int | None]:
        """
        Return (evolution_pokedex_id, min_level) for the given pokemon,
        or (None, None) if it does not evolve.

        TODO:
            1. GET f"{POKEAPI_BASE}/pokemon-species/{pokedex_id}"
            2. From response get the evolution chain URL:
                   species_data["evolution_chain"]["url"]
            3. GET that URL
            4. Walk the chain to find this pokemon's entry and look at
               evolves_to[0]["evolution_details"][0]["min_level"]
            5. The next form's ID is in evolves_to[0]["species"]["url"]
               (parse the ID from the last segment of the URL)

        This is tricky!  The PokeAPI chain structure is nested:
            chain → evolves_to[] → evolves_to[] → ...
        Consider writing a recursive helper or a while loop.
        """
        pass

    @staticmethod
    def get_random_base_pokemon_id() -> int:
        """
        Return a random pokedex ID from only non-evolved (base form) Pokemon.

        For simplicity return a random int from a hardcoded list of base-form IDs
        (gen 1 starters and common base forms).

        TODO:
            - Define a list of base-form pokedex IDs (gen 1: 1,4,7,10,13,16,19,21,
              23,25,27,29,32,35,37,39,41,43,46,48,50,52,54,56,58,60,63,66,69,72,
              74,77,79,81,83,84,86,88,90,92,95,96,98,100,102,104,106,107,108,109,
              111,113,114,115,116,118,120,122,123,124,125,126,127,128,129,131,
              132,133,137,138,140,142,143,147)
            - Return random.choice(BASE_POKEMON_IDS)
        """
        pass

    @staticmethod
    def search_pokemon(query: str) -> list[dict]:
        """
        Return a list of {id, name} dicts whose names contain `query`.

        TODO:
            1. GET f"{POKEAPI_BASE}/pokemon?limit=151"  (gen 1 only to start)
            2. Filter results where query.lower() is in result["name"]
            3. Return [{"id": parse_id(r["url"]), "name": r["name"]} for r in filtered]

        Parse ID from URL: the URL ends in "/pokemon/25/" so split("/")[-2]
        """
        pass
