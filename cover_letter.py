import streamlit as st

def show_cover_letter():
    """Display a cover letter tailored for VNG Game Data Analyst position."""
    st.title("Cover Letter - VNG Game Data Analyst")
    
    # Contact Info Header
    st.markdown("""
    **Ho Dinh Duy Luc**  
    [hodinhduyluc@gmail.com](mailto:hodinhduyluc@gmail.com) | (+84) 8777 31725 | [github.com/Luc-h0](https://github.com/Luc-h0)  
    Ho Chi Minh, Vietnam  
    March 30, 2025  
    """)

    # Greeting
    st.markdown("""
    **Hiring Team**  
    VNG Corporation  
    Ho Chi Minh City, Vietnam  
    """)

    # Body
    st.header("Dear VNG Hiring Team,")
    st.markdown("""
    I am excited to apply for the Game Data Analyst position at VNG Corporation. As a final-year Data Science student at the University of Science, VNU, with a strong foundation in SQL, Python, and game analytics, I am eager to contribute my skills to a pioneering company renowned for its innovative titles like *ZingSpeed* and *Dead Target*. Having grown up playing games on ZingMe such as *Khu Vuon Tren May*, *Dao Rong*, *Hang Rong*, and *Nha Hang Vui Ve*, these unforgettable childhood memories fuel my passion for data-driven game design and my ambition to shape the future of gaming in Vietnam with VNG. Your commitment to leveraging data to enhance player experiences resonates deeply with me.

    Through my academic projects and self-directed learning, I’ve developed a robust skill set tailored to game analytics. In my *TikTok Analytics* project ([github.com/vphuhan/21KHDL-TikTok-Analytics](https://github.com/vphuhan/21KHDL-TikTok-Analytics)), I built a dashboard using Python (Pandas, Matplotlib) to uncover patterns and insights from large datasets, a process directly applicable to analyzing player behavior and retention in games. Similarly, my *Predict Student Performance from Game Play* project ([EDA](https://www.kaggle.com/code/lchinhduy/data-discovery-process-ipynb), [Model](https://www.kaggle.com/code/lchinhduy/catboost-model-train)) involved exploratory data analysis and machine learning (CatBoost) to predict outcomes based on gameplay data—an experience that honed my ability to derive actionable insights from complex datasets, a key requirement for optimizing freemium models and player segmentation at VNG.

    My technical toolkit—SQL, Python, Power BI, and Excel—complements my analytical strengths in data cleaning, statistical testing, and visualization. Coupled with my understanding of freemium models and player segmentation from studying strategy games, I am well-prepared to tackle challenges like improving in-game monetization or identifying key performance indicators for VNG’s diverse portfolio. Certifications such as the Google Data Analyst Certificate (2022) and SQL from HackerRank (March 2025) further validate my readiness to deliver impactful results.

    What excites me most about VNG is your focus on creating engaging, data-informed gaming experiences that resonate with millions. I am particularly inspired by your mobile gaming innovations and would love to contribute to projects that blend creativity with analytics. My detail-oriented approach, teamwork skills, and fluency in Vietnamese and English (IELTS 6.5), along with intermediate Japanese (JLPT N3), position me to collaborate effectively in your dynamic, multicultural environment.
pip freeze > requirements.txt
    I would be thrilled to bring my enthusiasm and expertise to VNG, helping to drive data-informed decisions that elevate player satisfaction and business success. Thank you for considering my application. I look forward to the opportunity to discuss how I can contribute to your team. Please feel free to contact me at [hodinhduyluc@gmail.com](mailto:hodinhduyluc@gmail.com) or (+84) 8777 31725.

    Sincerely,  
    **Ho Dinh Duy Luc**  
    """)

# Optional: Allow standalone execution for testing
if __name__ == "__main__":
    st.set_page_config(layout="wide")  # Set wide mode if run standalone
    show_cover_letter()