/**
 * pokemon.js — powers the index.html party view and pokedex.html browser.
 */

import { API } from './api.js';
import { showToast, buildPokemonCard, setLoading, loadTrainerId, saveTrainerId } from './ui.js';

// ------------------------------------------------------------------ //
//  Home page: trainer party display                                   //
// ------------------------------------------------------------------ //

/**
 * TODO: implement loadParty(trainerId)
 *
 *   1. setLoading(partyGrid, true)
 *   2. const party = await API.getParty(trainerId)
 *   3. Clear partyGrid
 *   4. For each pokemon: create a card via buildPokemonCard(p)
 *      then append a "Battle with this" button that links to:
 *         battle.html?trainer=<trainerId>&pokemon=<p.id>&opponent=<random_id>
 *      For now hard-code opponent to a random int 1–151:
 *         Math.floor(Math.random() * 151) + 1
 *   5. setLoading(partyGrid, false)
 */
async function loadParty(trainerId) {
  // TODO
}

/**
 * TODO: implement loadEggs(trainerId)
 *   1. Fetch trainer data: API.getTrainer(trainerId)
 *   2. For each egg in trainer.eggs that is not hatched:
 *         render an egg card with a "Hatch" button
 *   3. Hatch button click → API.hatchEgg(trainerId, egg.id)
 *                         → show toast with new pokemon name
 *                         → reload party and eggs
 */
async function loadEggs(trainerId) {
  // TODO
}

// ------------------------------------------------------------------ //
//  Trainer login / create                                             //
// ------------------------------------------------------------------ //

/**
 * TODO: implement handleLogin()
 *   Called when user submits the login form on index.html.
 *
 *   1. username = loginInput.value.trim()
 *   2. If empty show error toast and return
 *   3. trainer = await API.createTrainer(username)
 *      (backend returns existing trainer if username is taken, or creates new)
 *   4. saveTrainerId(trainer.id)
 *   5. Hide login form, show party section
 *   6. loadParty(trainer.id) + loadEggs(trainer.id)
 */
async function handleLogin() {
  // TODO
}

// ------------------------------------------------------------------ //
//  Pokedex browser (pokedex.html)                                     //
// ------------------------------------------------------------------ //

/**
 * TODO: implement searchAndRender()
 *   Called on each keystroke in the search box.
 *
 *   1. query = searchInput.value.trim()
 *   2. If query.length < 2 clear results and return
 *   3. results = await API.searchPokemon(query)
 *   4. For each result render a small card with:
 *         sprite, name, "Add to party" button
 *   5. "Add to party" → API.catchPokemon(trainerId, result.id)
 *                     → showToast(`${result.name} added!`)
 */
async function searchAndRender() {
  // TODO
}
