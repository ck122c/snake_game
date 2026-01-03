📌 Explanation of Snake Game (Python)
This program is a classic Snake Game developed using Python and the Pygame library. The objective of the game is to control a snake, eat food, grow longer, and avoid hitting the walls or the snake’s own body.

🧩 Libraries Used
pygame – Used to create the game window, graphics, and handle keyboard input
time – Used to control the game speed
random – Used to generate food at random positions

🖥️ Game Window Setup
A game window is created with a fixed width and height
The window title is set to "Snake Game"
Colors such as white, black, red, green, and blue are defined using RGB values

🐍 Snake Properties
The snake is represented as a list of blocks
Each block has a fixed size
Initially, the snake starts from the center of the screen
The snake moves in four directions:
Left
Right
Up
Down

🍎 Food Generation
Food is generated at a random location
When the snake eats the food:
The score increases
The snake length increases
New food appears at a new random position

🎮 Game Controls
The snake is controlled using keyboard keys:
Arrow Left → Move left
Arrow Right → Move right
Arrow Up → Move up
Arrow Down → Move down

💥 Game Over Conditions
The game ends if:
The snake hits the wall
The snake collides with its own body
When the game is over:
A Game Over message is displayed
The final score is shown
The player can choose to:
Press C to play again
Press Q to quit the game

📊 Score Display
The score is displayed on the screen
Each time the snake eats food, the score increases by 10 points

🔁 Game Loop
The program runs inside a continuous loop that:
Handles user input
Updates snake movement
Checks collisions
Draws the snake and food
Refreshes the screen

✅ Conclusion
This Snake Game demonstrates:
Use of loops
Conditional statements
Functions
Keyboard event handling
Basic game logic
It is a beginner-friendly project that helps understand game development concepts using Python.
