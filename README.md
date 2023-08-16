# Azure IAM Visualization

Ever found yourself drowning in the maze of permissions and roles within Azure? It's a headache to explore each resource one by one. But fear not, I got something to make your life easier!

This is a Python-based web application that visualizes Azure Identity and Access Management (IAM) relationships using Plotly and Dash. The app reads IAM data from a CSV file and allows users to interactively explore the relationships between roles, users, and object types and the associated resources.

![Peek 2023-08-16 21-47](https://github.com/mverschu/AzureIAMVisualizer/assets/69352107/d2d68892-c56b-4bb7-9862-4169f64819ea)

## Features

- Visualize IAM relationships in a Sankey diagram.
- Filter IAM data based on roles, users, and object types.
- Interactive user interface powered by Dash and Plotly.
- Supports reading IAM data from a CSV file.

## Getting Started

### Prerequisites

- Python (3.6+ recommended)
- pip package manager

### Installation / Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mverschu/AzureIAMVisualizer.git
   cd AzureIAMVisualizer
   pip install -r requirements.txt
   ```

2. **Prepare Your IAM Data:** Ensure you have your IAM data in a CSV file (e.g., `iam_data.csv`) that contains relevant information about roles, users, and object types.

![image](https://github.com/mverschu/AzureIAMVisualizer/assets/69352107/1d487062-016d-4985-a3f2-6e5f5c934841)

3. **Run the App:**

    - Execute the application script by providing the CSV file as an argument:

      ```bash
      python app.py iam_data.csv
      ```
      
4. **Contributions and Feedback:**

    - Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to create a pull request or submit an issue in this repository.

      1. Fork the repository.
      2. Create a new branch: `git checkout -b feature/my-feature`.
      3. Make your changes and commit them: `git commit -m 'Add some feature'`.
      4. Push the changes to your fork: `git push origin feature/my-feature`.
      5. Open a pull request in this repository.

### ToDo

1. Add exclusion option.
