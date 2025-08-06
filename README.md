 Snake Water Gun Game (Python)

This is a simple command-line game implemented in Python, inspired by the classic "Rock Paper Scissors" game, but with a twist: **Snake, Water, Gun**.

## Game Rules

- **Choices:**  
  - `S` for Snake  
  - `W` for Water  
  - `G` for Gun

- **How it works:**  
  - Both you and the computer choose one option.  
  - The winner is determined by these rules:
    - Snake drinks Water → Snake wins
    - Water drowns Gun → Water wins
    - Gun kills Snake → Gun wins
    - Same choices → Draw

## How To Play

1. Run the program using Python:
    ```bash
    python filename.py
    ```
2. Enter your choice when prompted:
    - Type `S` for Snake
    - Type `W` for Water
    - Type `G` for Gun

3. The program will display both choices and the result (win/lose/draw).

## Example

```
Enter your choice: S
You chose Snake 
Computer chose Gun 
You loose
```

## Requirements

- Python 3.x

## Notes

- The computer's choice is random every time.
- If you enter anything other than `S`, `W`, or `G`, the program may show an error.
