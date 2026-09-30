# Markdown Planning Sheet
***Computational Thinking***

| Computational Thinking Skill | Description |
|------------------------------|-------------|
| Decomposition | The Plant Class and Zombie Class, the methods within each class, the specific objects, and the code that will connect them all together.|
| Pattern Recognition | The game will check the health of all objects (both plants and the one zombie), and the distance of the zombie from the nearest living plant. Depending on the above information, the turn can consist of an from each living plant, and an attack from the zombie, or the end of the game.|
| Abstraction | Each "Plant" character needs a name and values for health and damage, while the "Zombie" character needs a name, health, damage, and a distance value.|
| Algorithm Design | Both plants attack. If the Zombie reaches 0 health, the game ends and prints the victory for the plants. If the Zombie's health is greater than 0, its distance value decreases. The turn ends if the distance value is greater than 0. If not, the Zombie attacks the first plant. A new value will be added to the Zombie's distance if the first plant dies. On the next turn, a "dead" plant will inflict no damage to the Zombie. The game stops when the Zombie or both plants die.
