🛡️ AI-Market Pulse: Intelligence Dashboard
An automated Cloud-Native Intelligence Pipeline that monitors global market sentiment using Artificial Intelligence, Networking Probes, and GitHub Cloud Automation.

🚀 Live Demo
(Note: Replace this with a screen recording of your Streamlit dashboard later!)

🧠 Project Core
Networking (The Probe): Automates data fetching from global news feeds using requests and BeautifulSoup4.

AI Engine (The Brain): Implements a Transformer-based Deep Learning model (DistilBERT) via HuggingFace to categorize text sentiment with high confidence.

Cloud (The Heart): Utilizes GitHub Actions to orchestrate the pipeline 24/7 on a serverless schedule.

Interface (The Face): Provides an interactive web dashboard built with Streamlit and Plotly for real-time visualization.

🛠️ Tech Stack
Language: Python 3.12

AI/ML: Transformers, PyTorch

Data: Pandas, NumPy

Cloud: GitHub Actions (CI/CD)

UI: Streamlit, Plotly

📂 Project Structure
engine/: Contains the scraper and AI sentiment logic.

ui/: The Streamlit dashboard interface.

.github/workflows/: Cloud automation scripts for scheduled runs.