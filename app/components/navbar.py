import streamlit as st

def navbar():

    st.markdown("""
                    <style>@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap');
                        * {
                            font-family: 'Poppins', sans-serif;
                        }
                        #MainMenu {visibility: hidden;}
                        .css-k0sv6k {
                        position: fixed;
                        top: 0px;
                        left: 0px;
                        right: 0px;
                        height: 2.875rem;
                        background: rgb(255, 255, 255) none repeat scroll 0% 0%;
                        outline: currentcolor none medium;
                        z-index: 1000020;
                        display: none;
                        }
                        .css-10xlvwk {
                            background-attachment: fixed;
                            flex-shrink: 0;
                            height: calc(-2px + 100vh);
                            top: 2px;
                            overflow: auto;
                            position: relative;
                            transition: margin-left 300ms ease 0s, box-shadow 300ms ease 0s;
                            width: 21rem;
                            z-index: 999991;
                            margin-left: 0px;
                            background-color: rgba(177, 182, 166, 0.8);
                            box-shadow: 10px 5px 15px #9A9A9A;
                        }
                        .css-rytr0c {
                            vertical-align: middle;
                            overflow: hidden;
                            color: rgb(151, 166, 195);
                            fill: currentcolor;
                            display: inline-flex;
                            -moz-box-align: center;
                            align-items: center;
                            font-size: 1.25rem;
                            width: 1.25rem;
                            height: 1.25rem;
                            display: none;
                        }
                        .css-j7qwjs {
                            display: flex;
                            flex-direction: column;
                            border-bottom: 1px solid rgb(129, 149, 149);
                        }
                        .css-1s3y5qe {
                            cursor: default;
                            position: absolute;
                            height: 1rem;
                            left: 0px;
                            right: 0px;
                            bottom: 0px;
                            display: flex;
                            -moz-box-align: center;
                            align-items: center;
                            -moz-box-pack: center;
                            justify-content: center;
                            color: rgba(49, 51, 63, 0.6);
                            border-bottom: 1px solid rgba(49, 51, 63, 0.2);
                            transition: color 500ms ease 0s;
                            display: none;
                        }
                        .css-1v3fvcr {
                            display: flex;
                            flex-direction: column;
                            width: 100%;
                            overflow: auto;
                            -moz-box-align: center;
                            align-items: center;
                            background-color: #EEE;
                        }
                        .css-18ni7ap {
                            position: fixed;
                            top: 0px;
                            left: 0px;
                            right: 0px;
                            height: 2.875rem;
                            background: rgb(255, 255, 255) none repeat scroll 0% 0%;
                            outline: currentcolor none medium;
                            z-index: 999990;
                            display: none;
                        }
                        .css-9s5bis {
                            box-shadow: unset !important;
                            outline: unset;
                        }
                        .css-9s5bis:focus {
                            box-shadow: unset !important;
                            outline: unset;
                        }
                        .css-1q1n0ol {
                            padding-left: 1rem;
                            padding-right: 1rem;
                            display: none;
                        }
                        .css-12oz5g7 {
                            flex: 1 1 0%;
                            width: 100%;
                            padding: 6rem 1rem 10rem;
                            max-width: 90rem;
                        }
                        .css-1p1nwyz {
                            width: 304px;
                            position: relative;
                            display: none;
                        }
                    </style>
                """, unsafe_allow_html=True)