# PythonShootGame - Improved OOP Version

A refactored, object-oriented take on the classic plane shooting game using Pygame. This version transforms the original procedural code into a modular architecture using an abstract base class, significantly improving maintainability and clean inheritance.

## ℹ️ Project Origin
This project is an evolution of the [PythonShootGame by Kill-Console](https://github.com/Kill-Console/PythonShootGame). 

My version refactors the original code to implement an object-oriented architecture, improving modularity and maintainability through the use of abstract base classes and centralized configuration.

## 🏗️ Project Architecture
* `core_abstract_blueprint.py`: Contains the `GameObject` abstract base class, establishing the foundation for all game entities.
* `player_plane.py`: Defines the `PlayerShip` class, handling player movement and shooting mechanics.
* `enemy_sprite.py`: Defines the `EnemyShips` class.
* `bullet_sprite.py`: Defines the `ShipBullets` class.
* `main_launcher.py`: The entry point, containing the game loop, event management, and rendering engine.
* `global_configuration_constants.py`: Centralized configuration for screen dimensions and global constants.

## 🚀 How to Start
1. Ensure you have `pygame` installed:
   ```bash
   pip install pygame
