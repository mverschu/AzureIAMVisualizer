# Azure IAM Visualization App

This is a Python-based web application that visualizes Azure Identity and Access Management (IAM) relationships using Plotly and Dash. The app reads IAM data from a CSV file and allows users to interactively explore the relationships between roles, users, and object types.

![App Screenshot](screenshot.png)

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Visualize IAM relationships in a Sankey diagram.
- Filter IAM data based on roles, users, and object types.
- Interactive user interface powered by Dash and Plotly.
- Supports reading IAM data from a CSV file.

## Getting Started

### Prerequisites

- Python (3.6+ recommended)
- pip package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mverschu/AzureIAMVisualizer.git
   cd AzureIAMVisualizer
   pip install -r requirements.txt
   ```
