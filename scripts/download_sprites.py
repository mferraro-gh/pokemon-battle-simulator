"""
download_sprites.py — populate frontend/assets/sprites/ from the PokeAPI archive.

Downloaded sprites are .gitignored (they don't get committed) — this script is
the setup step that fetches them onto your machine. It's a utility (not part of
the OOP exercise), so it's fully implemented; just run it.

Usage (from the project root):
    python scripts/download_sprites.py                      # Gen 1 (1-151), front + back
    python scripts/download_sprites.py --start 1 --end 386  # Gens 1-3
    python scripts/download_sprites.py --no-back            # front sprites only
    python scripts/download_sprites.py --shiny              # also fetch shiny variants
    python scripts/download_sprites.py --enable             # ...and turn local sprites ON

Already-downloaded files are skipped, so re-running is cheap and safe.

Source: https://github.com/PokeAPI/sprites  (Nintendo/Game Freak — non-commercial use)
"""

import argparse
import os
import re

import requests

RAW_BASE = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon"

# This file lives in scripts/, so the sprite folder is ../frontend/assets/sprites/pokemon
HERE = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.normpath(os.path.join(HERE, "..", "frontend", "assets", "sprites", "pokemon"))
SPRITES_JS = os.path.normpath(os.path.join(HERE, "..", "frontend", "js", "sprites.js"))


def download_one(url: str, path: str) -> str:
    """Download a single sprite. Returns 'ok', 'skip', or 'miss'."""
    if os.path.exists(path):
        return "skip"
    resp = requests.get(url, timeout=20)
    if resp.status_code != 200:
        return "miss"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(resp.content)
    return "ok"


def set_local_flag(enabled: bool) -> bool:
    """
    Flip USE_LOCAL_SPRITES in frontend/js/sprites.js so the app uses local
    files. Returns True if the file was edited successfully.
    """
    try:
        # newline="" preserves the file's existing line endings on write
        with open(SPRITES_JS, "r", encoding="utf-8", newline="") as f:
            text = f.read()
    except OSError:
        return False

    new_text, n = re.subn(
        r"(export const USE_LOCAL_SPRITES\s*=\s*)(?:true|false)",
        rf"\g<1>{'true' if enabled else 'false'}",
        text,
        count=1,
    )
    if n == 0:
        return False

    with open(SPRITES_JS, "w", encoding="utf-8", newline="") as f:
        f.write(new_text)
    return True


def main():
    parser = argparse.ArgumentParser(description="Download Pokemon sprites from the PokeAPI archive.")
    parser.add_argument("--start", type=int, default=1,   help="first Pokedex ID (default 1)")
    parser.add_argument("--end",   type=int, default=151, help="last Pokedex ID (default 151)")
    parser.add_argument("--no-back", action="store_true", help="skip back-facing sprites")
    parser.add_argument("--shiny",   action="store_true", help="also download shiny variants")
    parser.add_argument("--enable",  action="store_true",
                        help="after downloading, set USE_LOCAL_SPRITES = true in js/sprites.js")
    args = parser.parse_args()

    # Build the list of (url, destination_path) pairs to fetch.
    targets: list[tuple[str, str]] = []
    for poke_id in range(args.start, args.end + 1):
        targets.append((f"{RAW_BASE}/{poke_id}.png", os.path.join(DEST, f"{poke_id}.png")))
        if not args.no_back:
            targets.append((f"{RAW_BASE}/back/{poke_id}.png", os.path.join(DEST, "back", f"{poke_id}.png")))
        if args.shiny:
            targets.append((f"{RAW_BASE}/shiny/{poke_id}.png", os.path.join(DEST, "shiny", f"{poke_id}.png")))

    print(f"Downloading {len(targets)} sprites into {DEST} ...")
    counts = {"ok": 0, "skip": 0, "miss": 0}
    for url, path in targets:
        result = download_one(url, path)
        counts[result] += 1
        symbol = {"ok": "OK ", "skip": " . ", "miss": "XX "}[result]
        print(f"  {symbol} {os.path.relpath(path, DEST)}")

    print(f"\nDone. {counts['ok']} downloaded, {counts['skip']} skipped, {counts['miss']} not found.")

    # Turn local sprites on automatically, or remind the user how to.
    if args.enable:
        if set_local_flag(True):
            print("Enabled local sprites (USE_LOCAL_SPRITES = true in frontend/js/sprites.js).")
        else:
            print("Could not auto-edit sprites.js — set USE_LOCAL_SPRITES = true manually.")
    elif counts["ok"] or counts["skip"]:
        print("Tip: set USE_LOCAL_SPRITES = true in frontend/js/sprites.js to use them")
        print("     (or re-run with --enable to flip it automatically).")


if __name__ == "__main__":
    main()
