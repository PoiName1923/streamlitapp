import streamlit as st
from streamlit_lottie import st_lottie as lt
import json


with open("fontend/animations/loading_animation.json") as f:
    ani = json.load(f)

lt(ani,width=100,height=100)