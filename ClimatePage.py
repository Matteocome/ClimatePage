# cliamte page mind-map

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import altair as alt

st.write("Hello")

## Testing code:
import streamlit as st
import graphviz
import streamlit as st
import graphviz

def generate_mind_map(node, parent=None):
    dot = graphviz.Digraph(format="png")
    
    if parent:
        dot.node(parent)
        dot.node(node)
        dot.edge(parent, node)
    else:
        dot.node(node)
    
    return dot

def main():
    st.title("Mind Map Generator")
    st.write("Create a simple mind map by adding nodes.")

    st.sidebar.header("Add Nodes")

    with st.sidebar.form("add_node_form"):
        new_node = st.text_input("Enter Node Name:")
        parent_node = st.selectbox("Select Parent Node:", ["None"] + [node for node, _ in nodes])

        submitted = st.form_submit_button("Add Node")

        if submitted and new_node:
            nodes.append((new_node, parent_node))
    
    st.sidebar.subheader("Generated Mind Map")

    for node, parent_node in nodes:
        st.sidebar.write(f"Node: {node}, Parent: {parent_node}")
    
    st.sidebar.write("Click the button below to generate the mind map:")

    generate_map = st.button("Generate Mind Map")

    if generate_map:
        dot = graphviz.Digraph(format="png")
        for node, parent_node in nodes:
            if parent_node != "None":
                dot.node(parent_node)
                dot.node(node)
                dot.edge(parent_node, node)
            else:
                dot.node(node)
        
        st.graphviz_chart(dot)

if __name__ == "__main__":
    nodes = []  # List to store node information (node, parent)
    main()

