import streamlit as st

def show_cv():
    """Display the CV for Ho Dinh Duy Luc."""
    st.title("Ho Dinh Duy Luc - CV")
    st.markdown("**Data Science Enthusiast | Game Analytics Specialist**")

    # Contact Info
    st.header("Contact Information")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Email**: [hodinhduyluc@gmail.com](mailto:hodinhduyluc@gmail.com)  
        **Phone**: (+84) 8777 31725  
        **GitHub**: [github.com/Luc-h0](https://github.com/Luc-h0)  
        **Location**: Ho Chi Minh, Vietnam
        """)
    with col2:
        st.markdown("")

    # Education
    st.header("Education")
    st.subheader("University of Science, VNU")
    st.markdown("""
    **Bachelor of Science in Data Science** (Undergraduate)  
    - **GPA**: 3.4/4.0  
    - **Relevant Coursework**: Data Mining, Probability & Statistics, SQL Programming, Intelligence Data Analysis, Big Data  
    """)

    # Skills
    st.header("Skills")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Technical")
        st.markdown("""
        - SQL  
        - Python (Pandas, Matplotlib)  
        - Power BI  
        - Excel  
        """)
    with col2:
        st.subheader("Analytical")
        st.markdown("""
        - Data Cleaning  
        - Retention Analysis  
        - Statistical Testing  
        """)
    with col3:
        st.subheader("Game Knowledge & Soft Skills")
        st.markdown("""
        - Freemium Models  
        - Player Segmentation  
        - Detail-Oriented  
        - Teamwork  
        """)

    # Projects
    st.header("Projects")
    st.subheader("TikTok Analytics")
    st.markdown("""
    - **Link**: [github.com/vphuhan/21KHDL-TikTok-Analytics](https://github.com/vphuhan/21KHDL-TikTok-Analytics)  
    - **Description**: Developed a dashboard to observe changes and patterns, uncovering key insights from TikTok data.  
    """)
    st.subheader("Predict Student Performance from Game Play")
    st.markdown("""
    - **Links**: [EDA](https://www.kaggle.com/code/lchinhduy/data-discovery-process-ipynb), [Model](https://www.kaggle.com/code/lchinhduy/catboost-model-train)  
    - **Description**: Conducted exploratory data analysis (EDA) with visualization charts and deployed machine learning models (e.g., CatBoost) to predict student performance based on gameplay data.  
    """)

    # Certifications
    st.header("Certifications")
    st.markdown("""
    - **IELTS 6.5** - International English Language Testing System, 2021  
    - **Google Data Analyst Certificate** - Coursera, 2022  
    - **Excel Fundamentals for Data Analysis** - Macquarie University, 2022  
    - **JLPT N3** - Japanese Language Proficiency Test, 2024  
    - **SQL** - HackerRank, March 2025  
    """)

    # Additional
    st.header("Additional")
    st.markdown("""
    **Interests**: Strategy Games, Data-Driven Game Design  
    """)


# Optional: Allow standalone execution for testing
if __name__ == "__main__":
    st.set_page_config(layout="wide")  # Set wide mode if run standalone
    show_cv()