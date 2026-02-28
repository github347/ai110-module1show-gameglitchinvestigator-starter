# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- The hint keep saying "Go Higher" even while my input was 99 or 100 and the range is supposedbe between 1 and 100. Should have been "Go LOWER" instead.
- Clicking "New Game" doesn't remove the Game over message. Expected a new game to start and clear the error message.
- New Game aslo doesn't let you continue playing after winning a game. Expected a a new game to start.
- There is a discrepancy between the "Guess a number between 1 and 100. Attempts left: 6" and the Setting showing a different range and the new game creating a new secret number out of range. Expected to have the same range and limit be applied properly.
- 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
- I used Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    - It was about the text for going higher and lower. I parse the first part and asked the AI for help and the answer also caught a second part fallback where it happened again before I realized that.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
 - Not incorect per se but it failed to copy the 📉 emoji in the answer.
 - Was having issue with the imports to to run the pytest as there was no "__init__.py" file to make modules.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Running the game and see if what I expected to happen actualy does or the pytest that were created passed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  The code for the initial 3 test passed successfuly: `[100%] 3 passed in 0.01s`
- Did AI help you design or understand any tests? How?
    - It switched the variable names from the first 3 test.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
