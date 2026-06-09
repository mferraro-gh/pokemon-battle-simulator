# Sprite Archive

This folder is where **local Pokemon sprites** live. Right now the app pulls
sprites straight from PokeAPI's remote URLs, so this folder ships mostly empty
(just `.gitkeep` placeholders). When you're ready to bundle your own sprites,
fetch them with the script below and flip one flag — see
[Enabling local sprites](#enabling-local-sprites).

> **Downloaded sprites are not committed to git.** They're listed in
> `.gitignore` and live only on your machine — that keeps the repo small and
> avoids redistributing Nintendo's artwork. Each person who clones the project
> runs the download script once to populate this folder. The folder *structure*,
> this README, and any curated `ui/` + `eggs/` art you add **are** tracked.

---

## 📂 Folder layout

```
assets/sprites/
├── pokemon/            front-facing sprites — shown everywhere
│   ├── 1.png
│   ├── 25.png
│   └── back/           back-facing sprites — used for YOUR pokemon in battle
│       ├── 1.png
│       └── 25.png
├── eggs/               egg sprite(s)
│   └── egg.png
└── ui/                 interface art (logo, pokeball icon, placeholder)
    └── placeholder.png unknown / missing-sprite fallback
```

> A `shiny/` folder (same `{id}.png` naming) is also supported by the resolver
> and the download script (`--shiny`) if you ever want shiny variants.

---

## 🏷️ Naming convention

Files are named by **National Pokedex number**, no zero-padding — exactly how
the PokeAPI archive names them:

| Pokemon    | File              |
|------------|-------------------|
| Bulbasaur  | `pokemon/1.png`   |
| Pikachu    | `pokemon/25.png`  |
| Charizard  | `pokemon/6.png`   |

This matches `pokemon.pokedex_id` from the backend, so the resolver can build a
path with zero guesswork.

---

## ⬇️ Getting the sprites

Sprites come from the official **PokeAPI sprite archive**:
https://github.com/PokeAPI/sprites

A helper script is included to fetch them for you:

```bash
# from the project root
python scripts/download_sprites.py                 # Gen 1 (IDs 1-151), front + back
python scripts/download_sprites.py --start 1 --end 386   # Gens 1-3
python scripts/download_sprites.py --shiny         # also grab shiny variants
python scripts/download_sprites.py --enable        # download AND switch the app to local
```

The script skips files you already have, so it's safe to re-run.

---

## ✅ Enabling local sprites

**Quickest way** — let the download script do both steps:

```bash
python scripts/download_sprites.py --enable
```

**Or manually:**

1. Add the PNGs (run the script above, or copy your own in).
2. Open [`frontend/js/sprites.js`](../../js/sprites.js).
3. Change one line:

   ```js
   export const USE_LOCAL_SPRITES = true;   // was false
   ```

Every page resolves sprites through `SpriteResolver`, so that single switch
makes the whole app use your local archive. If a local file is missing, the
resolver automatically falls back to the remote URL, then to
`ui/placeholder.png` — so a half-finished archive won't break the UI.

---

## ⚖️ Attribution

Pokemon sprites are property of **Nintendo / Game Freak / The Pokemon Company**.
The PokeAPI archive (and this project) are for **non-commercial, educational
use only**. Don't ship these in a commercial product.
