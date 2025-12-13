name: Automate Data Preprocessing

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Preprocessing Script
        run: python 01_preprocessing/automate_Christian-Daniel.py

      - name: Commit and Push Processed Data
        run: |
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git add preprocessing/data_clean/*.csv
          git commit -m "Auto-update: Processed dataset via GitHub Actions" || echo "No changes to commit"
          git push
