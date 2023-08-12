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
import streamlit as st
import graphviz

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
    current_parent = None

    st.sidebar.header("Set Parent Node")

    parent_node = st.text_input("Enter Parent Node Name:")

    st.sidebar.write("Click the button below to set the parent node:")

    set_parent = st.button("Set Parent Node")

    if set_parent:
        current_parent = parent_node

    st.sidebar.subheader("Add Child Nodes")

    with st.sidebar.form("add_node_form"):
        new_node = st.text_input("Enter Child Node Name:")
        description = st.text_area("Enter Description:")

        submitted = st.form_submit_button("Add Child Node")

        if submitted and new_node:
            nodes.append((new_node, current_parent, description))
    
    st.sidebar.subheader("Generated Mind Map")

    for node, parent_node, desc in nodes:
        st.sidebar.write(f"Node: {node}, Parent







