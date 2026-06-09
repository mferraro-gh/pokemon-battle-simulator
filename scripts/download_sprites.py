"""
download_sprites.py — populate frontend/assets/sprites/ from the PokeAPI archive.

This is a utility (not part of the OOP exercise) so it's fully implemented —
run it whenever you want to bundle local sprites.

Usage (from the project root):
    python scripts/download_sprites.py                      # Gen 1 (1-151), front + back
    python scripts/download_sprites.py --start 1 --end 386  # Gens 1-3
    python scripts/download_sprites.py --no-back            # front sprites only
    python scripts/download_sprites.py --shiny              # also fetch shiny variants

Already-downloaded files are skipped, so re-running is cheap and safe.

Source: https://github.com/PokeAPI/sprites  (Nintendo/Game Freak — non-commercial use)
"""

import argparse
import os

import requests

RAW_BASE = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon"

# This file lives in scripts/, so the sprite folder is ../frontend/assets/sprites/pokemon
HERE = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.normpath(os.path.join(HERE, "..", "frontend", "assets", "sprites", "pokemon"))


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


def main():
    parser = argparse.ArgumentParser(description="Download Pokemon sprites from the PokeAPI archive.")
    parser.add_argument("--start", type=int, default=1,   help="first Pokedex ID (default 1)")
    parser.add_argument("--end",   type=int, default=151, help="last Pokedex ID (default 151)")
    parser.add_argument("--no-back", action="store_true", help="skip back-facing sprites")
    parser.add_argument("--shiny",   action="store_true", help="also download shiny variants")
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
        symbol = {"ok": "✓", "skip": "·", "miss": "✗"}[result]
        print(f"  {symbol} {os.path.relpath(path, DEST)}")

    print(f"\nDone. {counts['ok']} downloaded, {counts['skip']} skipped, {counts['miss']} not found.")


if __name__ == "__main__":
    main()
