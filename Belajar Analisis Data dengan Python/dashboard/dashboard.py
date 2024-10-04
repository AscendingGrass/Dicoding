import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


try:
    data = pd.read_csv("data_clean.csv")
except:
    exit("Error loading data")


