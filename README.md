# 🎮 Game Glitch Investigator: The Impossible Guesser
## TF Weekly Task 2

The core concept students needed to understand is how to troubleshoot AI generated code until you achieve what you need. Students are most likely to struggle with importing the functions from the `logic_utils.py` after moving them because there is no `__init__.py` file for the module. The AI took a long time trying to figure it out. The AI also wasn’t helpful in running the tests by itself. It kept having issues with the test not found as it wasn’t using my environment. One way I would guide a student without giving the answer is to encourage them to think about what they are trying to solve compared to what is currently happening with the code.  


## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

![Go Lower](<Screenshots/Go Lower.png>)
![Go Higher](<Screenshots/Go Higher.png>)
![Wining](<Screenshots/Winning Screenshot 1.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
