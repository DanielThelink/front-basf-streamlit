import streamlit as st

from app.helper.word_cloud import draw_word_cloud

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
                            border-left: 5px solid rgba(177, 182, 166, 0.8);
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

    data = [
            {
                "id": 121,
                "score": 0.999972,
                "texto": "a brand",
                "inicio": 14,
                "fim": 21,
                "id_pesquisa": 19384,
                "classificacao_nps": "Promotor"
            },
            {
                "id": 136,
                "score": 0.999965,
                "texto": "a competent supplier",
                "inicio": 83,
                "fim": 103,
                "id_pesquisa": 19387,
                "classificacao_nps": "Promotor"
            },
            {
                "id": 137,
                "score": 0.9999,
                "texto": "a German company",
                "inicio": 10,
                "fim": 26,
                "id_pesquisa": 19388,
                "classificacao_nps": "Promotor"
            },
            {
                "id": 120,
                "score": 0.999767,
                "texto": "a little delay",
                "inicio": 0,
                "fim": 14,
                "id_pesquisa": 19383,
                "classificacao_nps": "Neutro"
            }
        ]

    text_filter = st.text_input("Filtro:")
        
    c1, c2 = st.columns((4, 2))

    with c1:
        st.pyplot(draw_word_cloud(data))

    with c2:
        for i in range(3):
            st.write(
                """
                    <p><b>Lorem Ipsum</b></p>
                    <p>In vitae ex ante. Aliquam erat dui, consequat nec nunc id, blandit condimentum sem. Morbi facilisis velit ac libero iaculis, in cursus leo aliquam. Proin vel dui nec nulla aliquet malesuada at id urna</p>
                    <p><i>Two Days Ago</i></p>
                """,
                unsafe_allow_html=True
            )

