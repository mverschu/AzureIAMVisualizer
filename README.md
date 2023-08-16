# Azure IAM Visualization App

Ever found yourself drowning in the maze of permissions and roles within Azure? It's a headache to explore each assignment one by one. But fear not, we've got something to make your life easier!

This is a Python-based web application that visualizes Azure Identity and Access Management (IAM) relationships using Plotly and Dash. The app reads IAM data from a CSV file and allows users to interactively explore the relationships between roles, users, and object types.

![image](https://github.com/mverschu/AzureIAMVisualizer/assets/69352107/398c4a2a-f4ce-4773-9c39-6895e089a5ce)

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation/Usage](#installation)

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

![image](https://github.com/mverschu/AzureIAMVisualizer/assets/69352107/48bdf34a-7d27-4a44-afa1-a7413dae8f90)

3. **Run the App:**

    - Execute the application script by providing the CSV file as an argument:

      ```bash
      python app.py iam_data.csv
      ```
