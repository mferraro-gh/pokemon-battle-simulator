/**
 * ui.js — reusable UI helpers shared across all pages.
 */

// ------------------------------------------------------------------ //
//  Toast notifications                                                //
// ------------------------------------------------------------------ //

/**
 * Show a temporary toast message at the bottom-right of the screen.
 *
 * TODO:
 *   1. Create a div.toast element
 *   2. Set its textContent to `message`
 *   3. If `type` is "error" change the border-left color to red
 *   4. Append to #toast-container
 *   5. After 3000ms remove the element
 *
 * @param {string} message
 * @param {"info"|"error"|"success"} type
 */
export function showToast(message, type = "info") {
  // TODO: implement
}

// ------------------------------------------------------------------ //
//  HP Bar                                                             //
// ------------------------------------------------------------------ //

/**
 * Update an HP bar element's width and colour class.
 *
 * @param {HTMLElement} barEl   — the .hp-bar div
 * @param {number}      current — current HP
 * @param {number}      max     — max HP
 *
 * TODO:
 *   1. Calculate percent = (current / max) * 100
 *   2. Set barEl.style.width = percent + "%"
 *   3. Remove old hp-* classes and add the right one:
 *        > 50% → hp-high
 *        > 20% → hp-medium
 *        else  → hp-low
 */
export function updateHpBar(barEl, current, max) {
  // TODO: implement
}

// ------------------------------------------------------------------ //
//  Pokemon card builder                                               //
// ------------------------------------------------------------------ //

/**
 * Build a .card element showing a Pokemon's info (sprite, name, types, HP).
 * Returns the element — the caller decides where to insert it.
 *
 * @param {object} pokemon — a pokemon dict from the API
 * @returns {HTMLElement}
 *
 * TODO:
 *   1. Create a div.card element
 *   2. Build inner HTML with:
 *        - <img class="sprite">  — set its src via SpriteResolver.front(pokemon)
 *          (import { SpriteResolver } from './sprites.js'; don't use
 *           pokemon.sprite_url directly — the resolver handles local-vs-remote)
 *        - Pokemon name and level
 *        - Type badges (.type-badge .type-{type} for each type)
 *        - HP bar (use the hp-bar-container / hp-bar pattern from CSS)
 *   3. Call updateHpBar on the hp-bar element
 *   4. Return the div
 */
export function buildPokemonCard(pokemon) {
  // TODO: implement
}

// ------------------------------------------------------------------ //
//  Type badge helper                                                  //
// ------------------------------------------------------------------ //

/**
 * Return an HTML string for type badges.
 * e.g. typeBadgesHtml(["fire", "flying"]) →
 *   '<span class="type-badge type-fire">fire</span> ...'
 *
 * TODO: implement
 */
export function typeBadgesHtml(types) {
  // TODO: return types.map(t => `<span class="type-badge type-${t}">${t}</span>`).join(" ");
}

// ------------------------------------------------------------------ //
//  Spinner                                                            //
// ------------------------------------------------------------------ //

/**
 * Show/hide a loading spinner inside `containerEl`.
 *
 * TODO:
 *   show=true  → insert <div class="spinner"> into containerEl
 *   show=false → remove any .spinner from containerEl
 */
export function setLoading(containerEl, show) {
  // TODO: implement
}

// ------------------------------------------------------------------ //
//  Local storage helpers for active trainer session                   //
// ------------------------------------------------------------------ //

const TRAINER_KEY = "pbs_trainer_id";

export function saveTrainerId(id) {
  localStorage.setItem(TRAINER_KEY, String(id));
}

export function loadTrainerId() {
  return Number(localStorage.getItem(TRAINER_KEY)) || null;
}

export function clearTrainerId() {
  localStorage.removeItem(TRAINER_KEY);
}
