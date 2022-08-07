import streamlit as st

from app.helper.charts import draw_gauge_chart

def sentiment_analisys():

    st.markdown("""
                    <style>
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
                        .css-183lzff {
                            font-family: "Source Code Pro", monospace;
                            white-space: pre;
                            font-size: 14px;
                            overflow-x: auto;
                            background-color: #FFF;
                            padding: 15px;
                            border-radius: 10px;
                        }
                        .css-bda956 {
                            font-family: "Source Sans Pro", sans-serif;
                            margin-bottom: -1rem;
                            color: rgb(0, 0, 0);
                            font-size: 20px;
                        }
                        .css-1kyf0rc {
                            width: 459px;
                            position: relative;
                            display: flex;
                            flex: 1 1 0%;
                            flex-direction: column;
                            gap: 1rem;
                        }
                        .css-bda956 p, .css-bda956 ol, .css-bda956 ul, .css-bda956 dl, .css-bda956 li {
                            font-size: inherit;
                            padding: 10px;
                            background-color: #FFF;
                            width: 450px;
                        }
                    </style>
                """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns((2, 2, 2))

    with c1:
        st.caption('Score de Sentimento')
        st.plotly_chart(draw_gauge_chart(45), use_container_width=False)

    with c2:
        with st.container():
            pass
    with c3:
        for i in range(3):
            st.write(
                """
                    <p><b>Lorem Ipsum</b></p>
                    <p>In vitae ex ante. Aliquam erat dui, consequat nec nunc id, blandit condimentum sem. Morbi facilisis velit ac libero iaculis, in cursus leo aliquam. Proin vel dui nec nulla aliquet malesuada at id urna</p>
                    <p><i>Two Days Ago</i></p>
                """,
                unsafe_allow_html=True
            )