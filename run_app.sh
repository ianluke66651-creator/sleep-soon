#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the main application
python src/main.py

# Deactivate the virtual environment after the app is closed
deactivate