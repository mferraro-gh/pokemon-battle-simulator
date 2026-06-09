/**
 * battle.js — powers the battle.html page.
 *
 * Flow:
 *   1. On load: read ?trainer=<id>&pokemon=<db_id>&opponent=<pokedex_id> from URL
 *   2. Fetch both pokemon details and render the arena
 *   3. User clicks "Fight!" → call API.startBattle()
 *   4. Animate the battle log round by round
 *   5. Show result overlay with XP / egg reward info
 */

import { API } from './api.js';
import { showToast, updateHpBar } from './ui.js';

// ------------------------------------------------------------------ //
//  DOM refs — fill these in as you build battle.html                  //
// ------------------------------------------------------------------ //

// TODO: const playerSprite   = document.getElementById("player-sprite");
// TODO: const opponentSprite = document.getElementById("opponent-sprite");
// TODO: const playerHpBar    = document.getElementById("player-hp-bar");
// TODO: const opponentHpBar  = document.getElementById("opponent-hp-bar");
// TODO: const playerHpLabel  = document.getElementById("player-hp-label");
// TODO: const opponentHpLabel= document.getElementById("opponent-hp-label");
// TODO: const battleLog      = document.getElementById("battle-log");
// TODO: const fightBtn       = document.getElementById("fight-btn");
// TODO: const resultOverlay  = document.getElementById("result-overlay");

// ------------------------------------------------------------------ //
//  State                                                              //
// ------------------------------------------------------------------ //

let trainerId = null;
let playerPokemonId = null;
let opponentPokedexId = null;

// ------------------------------------------------------------------ //
//  Init                                                               //
// ------------------------------------------------------------------ //

/**
 * TODO: implement init()
 *   1. Parse URL query params:
 *        const params = new URLSearchParams(window.location.search);
 *        trainerId        = Number(params.get("trainer"));
 *        playerPokemonId  = Number(params.get("pokemon"));
 *        opponentPokedexId = Number(params.get("opponent"));
 *   2. Validate all three are present — if not redirect to index.html
 *   3. Fetch player pokemon: API.getOwnedPokemon(trainerId) then find by id
 *   4. Fetch opponent: API.getPokemonData(opponentPokedexId)
 *   5. Render both sides: renderPokemon("player", playerData)
 *                         renderPokemon("opponent", opponentData)
 *   6. Enable the fight button
 */
async function init() {
  // TODO
}

// ------------------------------------------------------------------ //
//  Render helpers                                                     //
// ------------------------------------------------------------------ //

/**
 * TODO: implement renderPokemon(side, data)
 *   side  — "player" | "opponent"
 *   data  — pokemon dict from API
 *
 *   Set the sprite src, name, level, type badges, hp bar.
 */
function renderPokemon(side, data) {
  // TODO
}

// ------------------------------------------------------------------ //
//  Battle execution                                                   //
// ------------------------------------------------------------------ //

/**
 * TODO: implement runBattle()
 *   Called when the user clicks "Fight!".
 *
 *   1. Disable fight button
 *   2. Show loading state in battle log
 *   3. result = await API.startBattle(trainerId, playerPokemonId, opponentPokedexId)
 *   4. Animate each round with a delay: animateRounds(result.rounds)
 *   5. After animation ends: showResultOverlay(result)
 */
async function runBattle() {
  // TODO
}

// ------------------------------------------------------------------ //
//  Animation                                                          //
// ------------------------------------------------------------------ //

/**
 * TODO: implement animateRounds(rounds)
 *   For each round in rounds:
 *     1. Append a log entry to battleLog with round.message
 *     2. Update the defender's HP bar (round.hp_remaining)
 *     3. Play shake animation on defender's sprite (add class "hit", remove after 400ms)
 *     4. await sleep(600)  — so the player can follow along
 *
 *   Helper: const sleep = ms => new Promise(r => setTimeout(r, ms));
 */
async function animateRounds(rounds) {
  // TODO
}

// ------------------------------------------------------------------ //
//  Result overlay                                                     //
// ------------------------------------------------------------------ //

/**
 * TODO: implement showResultOverlay(result)
 *   1. Set result title: "You Win!" or "You Lost..."
 *   2. Show XP gained and whether they levelled up
 *   3. If result.evolved: show "Your Pokemon evolved into X!"
 *   4. If result.egg: show egg sprite and "You received an egg!"
 *   5. Add "Play Again" button → goes back to index.html
 *   6. Remove .hidden from resultOverlay
 */
function showResultOverlay(result) {
  // TODO
}

// ------------------------------------------------------------------ //
//  Event listeners                                                    //
// ------------------------------------------------------------------ //

// TODO: document.getElementById("fight-btn").addEventListener("click", runBattle);

// ------------------------------------------------------------------ //
//  Start                                                              //
// ------------------------------------------------------------------ //

init();
