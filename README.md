# MumzWorld AI Smart Basket Assistant

## Overview
AI-powered multilingual shopping assistant for personalized mom and baby recommendations.

## Features
- Multi-agent recommendation engine
- English + Arabic recommendations
- Budget-aware product bundles
- Predictive next-needs suggestions
- Safety-aware product reasoning
- Smart basket scoring

## Tech Stack
- Python
- Streamlit
- Groq LLM API
- CSV Product Catalog

## Run
pip install -r requirements.txt
streamlit run app.py

## Example Prompt
travel essentials for 9 month old under 300 AED

## Files
- app.py → main application
- products.csv → sample catalog
- EVALS.md → evaluation cases
- TRADEOFFS.md → architecture decisions

## AI Usage Note
- Groq LLM API used for multilingual recommendation generation.
- Streamlit used for prototype UI.
- ChatGPT used for prompt iteration and architecture brainstorming.
- Multi-agent reasoning flow manually designed and evaluated.
- Human oversight used to refine outputs and handle failure cases.

## Time Log
- Problem selection & scoping: 45 min
- Prototype building: 2.5 hrs
- Prompt tuning & testing: 1 hr
- Evaluation and documentation: 45 min
- Demo recording & submission prep: 30 min
