import streamlit as st
import re 

from app.helper.word_cloud import draw_word_cloud
from app.services.artificialis_analisys import get_current_word_cloud,get_search_word_cloud,get_current_commentary


def words():

    st.markdown("""
                    <style>
                        .css-jwmu0f {
                            position: relative;
                            width: 1408px;
                            background-color: #FFF;
                            padding: 10px;
                            border-radius: 5px;
                        }
                        .css-15tx938 {
                            font-size: 18px;
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
                        .css-znku1x {
                            font-family: "Source Sans Pro", sans-serif;
                            margin-bottom: -1rem;
                            background-color: #FFF;
                            border-radius: 5px;
                            box-shadow: 10px 10px 5px #C1C1C1;
                        }
                        .css-znku1x p {
                            padding-left: 10px;
                            padding-right: 10px;
                        }
                        .css-znku1x:first-child p{
                            padding-top: 10px;
                            padding-bottom: 5px;
                        }
                        .css-znku1x:last-child p{
                            padding-bottom: 15px;
                        }
                    </style>
                """, unsafe_allow_html=True)

    current_words = get_current_word_cloud()

    color_commentary = {
                        "Promotor": "green",
                        "Neutro" : "yellow",
                        "Detrator" : "red"
                        } 

    st.pyplot(draw_word_cloud(current_words))

    text_filter = st.text_input("Filtro:")

    if st.button("Pesquisar"):
        current_words = get_search_word_cloud(text_filter)

    for commentary in current_words:

        color = color_commentary [commentary["classificacao_nps"]]

        id = commentary["id_pesquisa"]
        text = commentary["texto"]
        classification = commentary["classificacao_nps"]
        score = commentary["score"]

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
                    <p> Palavra-Chave : """ + formated_text.capitalize() + """</p>
                    <p>Classifica????o : """ + classification  + """ , Score : """ + str(score) + """ </p>
                </div>
            """,
            unsafe_allow_html=True
        )
