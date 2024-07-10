## Overview

### Application
Implement a team project planner tool. The tool consists of API's for
* Managing users
* Manging teams
* Managing a team board and tasks within a board 


The directory consists of base abstract classes. The goal is to implement the API methods defined in these classes
Create a module for concrete implementation of these base classes extending the base classes.
* The input and output will be JSON strings. Structure of which is mentioned in the method doc string.
* Every API needs to adhere to the constraints and raise exceptions for invalid inputs.
* The method doc, will include some additional requirements specific to the method.

### Persistence
The application should use the local file storage for persistence.  
The **db** folder should contain all the files created to persist the application data.  
The choice of the file format and data type is up to the developer.  
The user of the application should not be exposed to the internal file storage and only interact using the API's.

### Submission
* Update the **README.md** file with a brief summary of your project. Include your thought process of making the choices you made.
* You are free to use any python library. Add the required dependency to **requirements.txt**
* Create a zip of the final project. Please **Do Not** include the db files* or any imported libraries.
* For non explicilty mentied requirements you are free to make assumptions and add the rationale for the assumption in the **README.md**

### Evaluation
* Implementation of use cases
* Clean modular code
* Clear Abstractions
* Runtime Performance
* Handling edge cases
* Documentation
* Quality of Readme.md (Concise and to the point)
* Creativity and simplicity


