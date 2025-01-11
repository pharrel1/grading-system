# School Grading System

This document provides an overview and usage instructions for the School Grading System application. The application allows students to input their names and scores to determine their grades based on a predefined grading scale.

## Features
- **Student Input:** Students can enter their names and scores.
- **Grade Calculation:** Scores are automatically translated into grades based on the grading scale.
- **Interactive Interface:** A user-friendly input and output system for ease of use.

## System Requirements
- Python 3.7 or higher
- Libraries: None (uses only built-in Python modules)

## Installation
1. Ensure Python is installed on your system.
2. Download or clone the project repository.
3. Navigate to the project directory.

## Usage Instructions
1. Open a terminal or command prompt.
2. Navigate to the directory containing the application file (e.g., `grading_system.py`).
3. Run the application with the following command:
   ```
   python grading_system.py
   ```
4. Follow the prompts to:
   - Enter your name.
   - Input your score (a number between 0 and 100).
5. The system will display your name, score, and the corresponding grade.

## Grading Scale
The grading scale used in the system is as follows:

| Score Range | Grade |
|-------------|-------|
| 90-100      | A     |
| 80-89       | B     |
| 70-79       | C     |
| 60-69       | D     |
| 0-59        | F     |

## Example Output
```
Welcome to the School Grading System!
Please enter your name: John Doe
Please enter your score: 85

Student Name: John Doe
Score: 85
Grade: B
```

## Customization
If you wish to customize the grading scale:
1. Open the `grading_system.py` file in a text editor.
2. Modify the grading logic in the section where scores are mapped to grades.

## Troubleshooting
- **Invalid Input:** Ensure you enter a numerical score between 0 and 100. Non-numerical or out-of-range inputs will prompt an error message.
- **System Errors:** Verify that you have the correct version of Python installed.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For questions or feedback, please contact the developer at [kismetjay@outlook.com].

