/**
 * api.js — all fetch() calls to the Flask backend live here.
 *
 * OOP in JS: we use a plain object (API) as a namespace.
 * Every method is async and returns parsed JSON or throws on error.
 *
 * Usage from other files:
 *   import { API } from './api.js';
 *   const trainer = await API.getTrainer(1);
 */

const BASE_URL = "http://localhost:5000/api";

// ------------------------------------------------------------------ //
//  Helper                                                             //
// ------------------------------------------------------------------ //

async function request(method, path, body = null) {
  const options = {
    method,
    headers: { "Content-Type": "application/json" },
  };
  if (body) options.body = JSON.stringify(body);

  const res = await fetch(`${BASE_URL}${path}`, options);

  if (!res.ok) {
    const err = await res.json().catch(() => ({ error: res.statusText }));
    throw new Error(err.error || "Request failed");
  }

  return res.status === 204 ? null : res.json();
}

// ------------------------------------------------------------------ //
//  Trainer endpoints                                                   //
// ------------------------------------------------------------------ //

export const API = {

  /**
   * TODO: implement each method by calling `request(...)` with the right
   * HTTP method, path, and body (if applicable).
   *
   * The path structure mirrors the Flask routes:
   *   GET    /trainer/:id
   *   POST   /trainer          body: { username }
   *   GET    /trainer/:id/party
   *   PUT    /trainer/:id/party  body: { pokemon_id, in_party }
   *   POST   /trainer/:id/hatch/:eggId
   */

  createTrainer(username) {
    // TODO: return request("POST", "/trainer", { username });
  },

  getTrainer(trainerId) {
    // TODO: return request("GET", `/trainer/${trainerId}`);
  },

  getParty(trainerId) {
    // TODO: return request("GET", `/trainer/${trainerId}/party`);
  },

  hatchEgg(trainerId, eggId) {
    // TODO: return request("POST", `/trainer/${trainerId}/hatch/${eggId}`);
  },

  updatePartySlot(trainerId, pokemonId, inParty) {
    // TODO: return request("PUT", `/trainer/${trainerId}/party`, { pokemon_id: pokemonId, in_party: inParty });
  },

  // ---------------------------------------------------------------- //
  //  Pokemon endpoints                                                //
  // ---------------------------------------------------------------- //

  searchPokemon(query) {
    // TODO: return request("GET", `/pokemon/search?q=${encodeURIComponent(query)}`);
  },

  getPokemonData(pokedexId) {
    // TODO: return request("GET", `/pokemon/${pokedexId}`);
  },

  getOwnedPokemon(trainerId) {
    // TODO: return request("GET", `/pokemon/owned/${trainerId}`);
  },

  catchPokemon(trainerId, pokedexId) {
    // TODO: return request("POST", "/pokemon/catch", { trainer_id: trainerId, pokedex_id: pokedexId });
  },

  releasePokemon(pokemonDbId) {
    // TODO: return request("DELETE", `/pokemon/${pokemonDbId}`);
  },

  // ---------------------------------------------------------------- //
  //  Battle endpoints                                                 //
  // ---------------------------------------------------------------- //

  startBattle(trainerId, playerPokemonId, opponentPokedexId) {
    // TODO: return request("POST", "/battle/start", {
    //   trainer_id:          trainerId,
    //   player_pokemon_id:   playerPokemonId,
    //   opponent_pokedex_id: opponentPokedexId,
    // });
  },

  getBattleHistory(trainerId) {
    // TODO: return request("GET", `/battle/history/${trainerId}`);
  },
};
