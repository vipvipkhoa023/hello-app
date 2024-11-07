import streamlit as st
from comparison import compare_models_function
from vizualization import visualize_inferences
from feedback import feedback_ui


def display_dashboard():   
  
    

    dashboard_sections = ["Compare models", "Statistics", "Feedback Section"]

        # By default, the section is set to None to show the instruction page.
    section = st.session_state.get('dashboard_section', "")

        # Render the selectbox and store the choice in 'section'
    section = st.sidebar.selectbox("Choose a section to continue:", [""] + dashboard_sections, key="dashboard_section_selectbox", format_func=lambda x: "Select a section..." if x == "" else x)

    st.session_state.dashboard_section = section

    if not section:
        lottie = """
            <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
            <lottie-player src="https://raw.githubusercontent.com/irinagetman1973/YOLO-Streamlit/main/animation_sphere.json" background="transparent" speed="1" style="width: 400px; height: 400px;" loop autoplay></lottie-player>
            """
        st.markdown("""
            <style>
                iframe {
                    position: fixed;
                    top: 16rem;
                    bottom: 0;
                    left: 105;
                    right: 0;
                    margin: auto;
                    z-index=-1;
                }
            </style>
            """, unsafe_allow_html=True
        )


        st.components.v1.html(lottie, width=410, height=410) # When the selection is empty
        col1, col2 = st.columns([0.6, 0.3])  # Create a 2-column layout with equal width for each column

        with col1:
            st.subheader("🎓 Welcome to the Dashboard!")
            st.divider()
            st.write("""
            Welcome! Please select an option from the sidebar to begin. Each section offers unique functionalities:
            """)

            # Models Performance Comparison
            st.markdown("""
            **:one: **Models Performance Comparison**:**
            Compare the object detection capabilities of different models. 
            View detected images side-by-side for visual comparison, inference times
            and explore detection results including the count of each detected class 
            in a detailed table format.
            You can also save detection results to the database for future analysis.
            """)

            st.divider()

            # Results Access
            st.markdown("""
            **:two: **Results Access**:**
            Access and review past detection results. 
            Visualize them through charts and graphs, 
            and download the results as an Excel worksheet.
            """)

            st.divider()

            

            # Feedback
            st.markdown("""
            **:three: **Feedback**:**
            We value your input! Share your feedback  to help us improve.
            """)

            st.divider()

            st.write("**Enjoy your experience and happy detecting!** :green_heart:")

            
            

    

    elif section == "Compare models":
      
        compare_models_function() 
    
    elif section == "Statistics":
      
      visualize_inferences()

     

    

    elif section == "Feedback Section":

        feedback_ui()
     
