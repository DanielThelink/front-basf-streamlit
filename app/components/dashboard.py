import streamlit as st
import re

from app.services.artificialis_analisys import get_nps_data, get_search_commentary, get_current_commentary
from app.helper.charts import draw_gauge_chart

def dashboard():

    st.markdown("""
                    <style>
                        .css-bda956 {
                            font-family: "Source Sans Pro", sans-serif;
                            margin-bottom: -1rem;
                            color: #000;
                            font-size: 18px;
                        }
                        .css-15tx938 {
                            font-size: 16px;
                            color: rgb(49, 51, 63);
                            margin-bottom: 0.5rem;
                            height: auto;
                            min-height: 1.5rem;
                            vertical-align: middle;
                            display: flex;
                            flex-direction: row;
                            -moz-box-align: center;
                            align-items: center;
                        }
                        .css-1mbg4kq {
                            width: 461px;
                            position: relative;
                            display: flex;
                            flex: 1 1 0%;
                            flex-direction: column;
                            gap: 1rem;
                            background-color: #FFF;
                            padding: 10px;
                        }
                        .st-b7 {
                            width: 95%;
                        }
                        .st-bv {
                            max-width: 95%;
                            margin: auto;
                            margin-left: 15px;
                        }
                        .stSelectbox {
                            background-color: #FFF;
                            padding: 15px;
                            border-radius: 5px;
                        }
                        .css-eqcs3s {
                            position: relative;
                            width: 931px;
                            background-color: #FFF;
                            padding: 15px;
                            border-radius: 5px;
                        }
                        .css-183lzff {
                            font-family: "Poppins", sans-serif;
                            white-space: pre;
                            font-size: 14px;
                            overflow-x: auto;
                            color: rgb(49, 51, 63);
                        }
                    </style>
                """, unsafe_allow_html=True)
                
    nps_data = get_nps_data()
    current_commentary = get_current_commentary()

    filter_options = ["NPS", "Palavra Chave", "Sentimento"]

    choice_to_request = {
                        "NPS": "nps",
                        "Palavra Chave" : "palavraChave",
                        "Sentimento" : "sentimento"
                        }

    color_commentary = {
                        "Promotor": "green",
                        "Neutro" : "yellow",
                        "Detrator" : "red"
                        }     
    
    c1, c2 = st.columns((2, 4))

    with c1:
        st.caption('Score do NPS')
        st.plotly_chart(draw_gauge_chart(round(nps_data["nps_score"])), use_container_width=False)

        st.text(f'Detratores - {round(nps_data["dist_detrator"])}%')
        st.progress(round(nps_data["dist_detrator"]))

        st.text(f'Neutros - {round(nps_data["dist_neutro"])}%')
        st.progress(round(nps_data["dist_neutro"]))
        
        st.text(f'Promotores - {round(nps_data["dist_promotor"])}%')
        st.progress(round(nps_data["dist_promotor"]))

    with c2:
        
        choice = st.selectbox("Tipo de Filtro:", filter_options)
        
        options_filter = (["Promotor", "Neutro", "Detrator"] if choice == "NPS" else ["Positivo", "Neutro", "Negativo", "Misturado"])

        if choice == 'NPS' or choice == "Sentimento":
            text_filter = st.selectbox("Filtro:", options_filter)
        else:
            text_filter = st.text_input("Filtro:")

        if st.button ("Pesquisar"):
            current_commentary = get_search_commentary(choice_to_request[choice], text_filter)
            
        for commentary in current_commentary:

            color = color_commentary [commentary["classificacao_nps"]]

            id = commentary["id"]
            text = commentary["texto"]
            date = commentary["data"] 
            nps_value = commentary["valor_nps"]
            classification = commentary["classificacao_nps"]
            feeling = commentary["sentimento"]

            formated_text = re.sub("\n", " ", text)
               
            st.markdown(
                """
                    <style>
                        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap');
                        .box-""" + str(id) + """ {
                            font-family: "Poppins", sans-serif;
                            background-color: #FFF;
                            padding: 15px;
                            border-radius: 5px;
                            margin: 10px 0px;
                            border-left: 5px solid """ + color + """;
                        }
                    </style> 

                    <div class="box-""" + str(id) + """">
                        <p><b>""" + str(id) + """</b></p>
                        <p>""" + formated_text.capitalize() + """</p>
                        <p>Classificação : """ + classification + """, Valor do NPS : """ + str(nps_value) + """ , Sentimento : """ + feeling.capitalize() + """ </p>
                        <p><i>""" + str(date) + """</i></p>
                    </div>
                """,
                unsafe_allow_html=True
            )