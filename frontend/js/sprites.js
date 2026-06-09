/**
 * sprites.js — single source of truth for resolving Pokemon sprite URLs.
 *
 * WHY THIS EXISTS
 * Today sprites come straight from PokeAPI (the backend puts a remote URL in
 * each pokemon's `sprite_url`). Eventually you'll want to bundle your own local
 * sprite archive in frontend/assets/sprites/. Instead of hunting down every
 * <img> in the app on that day, ALL sprite paths go through this resolver — so
 * switching to local sprites is a one-line change (see USE_LOCAL_SPRITES below).
 *
 * This file is intentionally already implemented (it's plumbing, not an OOP
 * exercise). Just call SpriteResolver.front(pokemon) etc. from your other code.
 */

// ─────────────────────────────────────────────────────────────────────────────
//  THE SWITCH
//  Flip to true once you've added PNGs to frontend/assets/sprites/.
//  See frontend/assets/sprites/README.md for the folder layout + a downloader.
// ─────────────────────────────────────────────────────────────────────────────
export const USE_LOCAL_SPRITES = false;

// Base path is relative to the HTML files (which sit in frontend/).
const LOCAL_BASE   = "assets/sprites";
const PLACEHOLDER  = `${LOCAL_BASE}/ui/placeholder.png`;
const EGG_FALLBACK = `${LOCAL_BASE}/eggs/egg.png`;

export const SpriteResolver = {

  /** Front-facing sprite — used in lists, the Pokedex, and the opponent slot. */
  front(pokemon) {
    if (!pokemon) return PLACEHOLDER;
    if (USE_LOCAL_SPRITES) return `${LOCAL_BASE}/pokemon/${pokemon.pokedex_id}.png`;
    return pokemon.sprite_url || PLACEHOLDER;
  },

  /** Back-facing sprite — used for YOUR pokemon in the battle arena. */
  back(pokemon) {
    if (!pokemon) return PLACEHOLDER;
    if (USE_LOCAL_SPRITES) return `${LOCAL_BASE}/pokemon/back/${pokemon.pokedex_id}.png`;
    // Our API payload only carries the front URL, so remotely we reuse it.
    return pokemon.sprite_url || PLACEHOLDER;
  },

  /** Shiny variant (optional — only if you've added a shiny/ folder). */
  shiny(pokemon) {
    if (!pokemon) return PLACEHOLDER;
    if (USE_LOCAL_SPRITES) return `${LOCAL_BASE}/pokemon/shiny/${pokemon.pokedex_id}.png`;
    return pokemon.sprite_url || PLACEHOLDER;
  },

  /** Egg sprite. Local mode uses a single generic egg.png. */
  egg(egg) {
    if (USE_LOCAL_SPRITES) return EGG_FALLBACK;
    return (egg && egg.sprite_url) || EGG_FALLBACK;
  },

  /** The "unknown" fallback image. */
  placeholder() {
    return PLACEHOLDER;
  },

  /**
   * Set an <img>'s src with an automatic fallback chain.
   * If the chosen URL 404s (e.g. a local sprite you haven't added yet), the
   * image quietly swaps to `fallback` instead of showing a broken-image icon.
   *
   * Usage:
   *   SpriteResolver.applyTo(imgEl, SpriteResolver.front(pokemon));
   */
  applyTo(imgEl, url, fallback = PLACEHOLDER) {
    if (!imgEl) return;
    imgEl.onerror = () => {
      imgEl.onerror = null;       // avoid an infinite loop if fallback also fails
      imgEl.src = fallback;
    };
    imgEl.src = url;
  },
};
