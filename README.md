
## Overview

This project is a team project planner tool that provides APIs for managing project boards and tasks within those boards. The application uses local file storage for persistence and interacts through JSON strings for input and output.

## Thought Process

1. *Abstractions*: Defined clear base classes for board, team, and user management.
2. *Persistence*: Chose JSON files for simplicity and ease of use.
3. *Modularity*: Kept the code modular by separating base classes and concrete implementations.
4. *Error Handling*: Implemented exception handling for invalid inputs and missing files.

## Assumptions

1. Board, task, and user data will be provided as valid JSON strings.
2. Board, task, and user IDs are unique and provided by the user.

## Usage

1. Implement the base classes in project_board_base.py, team_base.py, user_base.py.

## Dependencies

- Python 3.7 or above
- PostgreSQl 
