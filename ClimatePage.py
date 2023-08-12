# cliamte page mind-map

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import altair as alt
import graphviz

st.write("Hello")

## Testing code:


def generate_mind_map(nodes):
    dot = graphviz.Digraph(format="png")
    
    for node, parent, description in nodes:
        if parent != "None":
            dot.node(parent)
            dot.node(node, label=f"{node}\n{description}", shape="box")
            dot.edge(parent, node)
        else:
            dot.node(node, label=f"{node}\n{description}", shape="box")
    
    return dot

def main():
    st.title("Mind Map Generator")
    st.write("Create a simple mind map by adding nodes with descriptions.")

    nodes = []  # List to store node information (node, parent, description)

    st.sidebar.header("Add Nodes")

    with st.sidebar.form("add_node_form"):
        new_node = st.text_input("Enter Node Name:")
        description = st.text_area("Enter Description:")
        parent_node = st.selectbox("Select Parent Node:", ["None"] + [node for node, _, _ in nodes])

        submitted = st.form_submit_button("Add Node")

        if submitted and new_node:
            nodes.append((new_node, parent_node, description))
    
    st.sidebar.subheader("Generated Mind Map")

    for node, parent_node, desc in nodes:
        st.sidebar.write(f"Node: {node}, Parent: {parent_node}, Description: {desc}")
    
    st.sidebar.write("Click the button below to generate the mind map:")

    generate_map = st.button("Generate Mind Map")

    if generate_map:
        dot = generate_mind_map(nodes)
        st.graphviz_chart(dot)

if __name__ == "__main__":
    main()


