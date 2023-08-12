# cliamte page mind-map

import streamlit as st
import seaborn as sns
import networkx as nx
import matplotlib.pyplot as plt
from streamlit import GraphvizChart
from PIL import Image
import pandas as pd 
import numpy as np
import altair as alt

st.write("Hello")

## Testing code:
def create_mind_map():
    G = nx.DiGraph()

    st.sidebar.header("Add Nodes")

    with st.sidebar.form("add_node_form"):
        new_node = st.text_input("Enter Node Name:")
        parent_node = st.selectbox("Select Parent Node:", ["None"] + list(G.nodes))

        submitted = st.form_submit_button("Add Node")

        if submitted and new_node:
            G.add_node(new_node)
            if parent_node != "None":
                G.add_edge(parent_node, new_node)

    pos = nx.spring_layout(G)  # Positioning of nodes

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=2000)
    st.pyplot(plt)

def main():
    st.title("Mind Map Generator")
    st.write("Create a simple mind map by adding nodes.")

    create_mind_map()

if __name__ == "__main__":
    main()
