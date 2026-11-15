# 247 Free Poker Clone (Pixel-to-Pixel)

A 100% pixel-to-pixel clone of the **247 Free Poker** (Texas Hold'em Poker) web application, containing all authentic game assets, sounds, animations, and game rules.

## What is Cloned
- **The Free Poker Game Engine**:
  - HTML5 Canvas Texas Hold'em Poker game
  - 5 Player Table (User + 4 AI bot opponents with distinct playstyles: Bill, Cassie, Molly, Todd, etc.)
  - Full betting controls: Fold, Check, Call, Raise (+ dynamic betting slider), All-In
  - Complete card graphics (52 deck cards + card back)
  - Realistic chip stacks and denominations ($1 blue, $5 red, $25 green, $100 purple, $500 gold, etc.)
  - Dealer button progression ("D")
  - Sound effects for dealing cards, card flips, chip clinks, raises, folds, turn prompts, and victory jingles
  - Difficulty selection (Easy, Medium, Hard, Expert)
  - Automatic game state persistence via local storage
- **Website UI & Styling**:
  - Header with original title graphic and navigation
  - Authentic table felt texture, wood border, and lighting gradients
  - Step-by-step How to Play Texas Hold'em guide with visual diagrams (Pre-flop, Flop, Turn, River, Showdown)
  - Hand Rankings guide (Royal Flush down to High Card)
  - Strategies guide and rules
  - Cleaned of external ad trackers and third-party promotions to ensure fast, standalone, offline-ready gameplay.

## How to Run

Run the local server script:
```bash
python3 start_server.py
```
Or with python's built-in module:
```bash
python3 -m http.server 8080
```
Then open [http://localhost:8080](http://localhost:8080) in your web browser.

You can also run the game frame directly at [http://localhost:8080/game/frame.html](http://localhost:8080/game/frame.html).
