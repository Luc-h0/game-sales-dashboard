# Game Sales Dashboard & Portfolio

## Overview
This Streamlit-based multi-page application serves as a comprehensive video game sales dashboard while also featuring my personal CV and a cover letter tailored for a Game Data Analyst position at VNG Corporation. The dashboard analyzes video game sales data from `vgsales.csv`, sourced from vgchartz.com. Additionally, the CV and cover letter showcase my expertise and passion for game analytics.

## Features
- **Dashboard**: An interactive visualization tool for analyzing video game sales, offering filters for platform, genre, year, and publisher. Key insights include:
  - Sales performance metrics
  - Top-selling games
  - Platform and publisher analysis
  - Market trends and segmentation
- **CV**: A detailed resume outlining my education, skills, projects, and certifications.
- **Cover Letter**: A customized letter for VNG Corporation, emphasizing my experience in game analytics and my connection to their gaming ecosystem.

## Project Structure
```
game-sales-dashboard/
├── app.py              # Main Streamlit app with multi-page navigation
├── dashboard.py        # Game sales dashboard logic
├── cv.py               # CV page
├── cover_letter.py     # Cover letter for VNG
├── vgsales.csv         # Dataset for the dashboard
├── requirements.txt    # Python dependencies
├── .gitignore          # Excludes unnecessary files (e.g., .venv/)
└── README.md           # This file
```

## Prerequisites
- Python 3.8+
- Git
- A GitHub account
- Streamlit Community Cloud account (optional, for deployment)

## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/Luc-h0/game-sales-dashboard.git
cd game-sales-dashboard
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```
The application will be available at: [http://localhost:8501](http://localhost:8501)

Use the sidebar to navigate between **Dashboard**, **CV**, and **Cover Letter**.

## Deployment on Streamlit Community Cloud
### 1. Push to GitHub
Ensure all changes are committed and pushed:
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### 2. Deploy on Streamlit Cloud
1. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) using your GitHub account.
2. Click **New app** → **From existing repo**.
3. Select the repository (e.g., `Luc-h0/game-sales-dashboard`).
4. Set `app.py` as the **Main file path**.
5. Click **Deploy** and wait for the app to build.

### Troubleshooting
- Check the deployment logs for any errors.
- Ensure `vgsales.csv` is in the root directory.
- Confirm that all dependencies are listed in `requirements.txt`.

## Live Demo
Access the deployed app here: [Game Sales Dashboard](https://vng0game0data0analytics0project.streamlit.app/)

## Dependencies (`requirements.txt`)
```txt
streamlit
pandas
plotly
```

## Dataset
- **File**: `vgsales.csv`
- **Source**: [vgchartz.com](https://www.vgchartz.com/)
- **Description**: Contains video game sales data for games that sold over 100,000 copies. It includes:
  - Game Name, Platform, Year, Genre, Publisher
  - Regional sales (NA_Sales, EU_Sales, JP_Sales, etc.)

## Author
**Ho Dinh Duy Luc**  
📧 Email: [hodinhduyluc@gmail.com](mailto:hodinhduyluc@gmail.com)  
🔗 GitHub: [github.com/Luc-h0](https://github.com/Luc-h0)

## Credits
- Built with **Streamlit** and **Plotly**.
- Inspired by my passion for strategy games and data-driven game design.

## License
This project is for personal use and demonstration purposes. Feel free to modify and adapt it for your needs!

