import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import subprocess
import os
import base64
import pickle

def desc_calc():
    # Performs the descriptor calculation
    bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file Slimmed_Descriptors.csv"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    os.remove('molecule.smi')
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    return href
def build_model(input_data):
    # Reads in saved regression model
    load_model = pickle.load(open('Model.pkl', 'rb'))
    # Apply model to make predictions
    prediction = load_model.predict(input_data)
    st.header('**Prediction output**')
    prediction_output = pd.Series(prediction, name='pIC50')
    molecule_name = pd.Series(load_data[1], name='molecule_name')
    df = pd.concat([molecule_name, prediction_output], axis=1)
    st.write(df)
    st.markdown(filedownload(df), unsafe_allow_html=True)



st.header('1. Upload your CSV Data')
uploaded_file = st.file_uploader("Upload your input file", type=['txt'])
st.markdown("""
    [Example input file](https://raw.githubusercontent.com/dataprofessor/bioactivity-prediction-app/main/example_acetylcholinesterase.txt)
    """)

if st.button('Predict'):
        load_data = pd.read_table(uploaded_file, sep=' ', header=None)
        load_data.to_csv('molecule.smi', sep='\t', header=False, index=False)

        st.header('**Original input data**')
        st.write(load_data)

        with st.spinner("Calculating descriptors..."):
            desc_calc()

        # Read in calculated descriptors and display the dataframe
        st.header('**Calculated molecular descriptors**')
        desc = pd.read_csv('Slimmed_Descriptors.csv')
        st.write(desc)
        st.write(desc.shape)

        st.subheader('**Subset of descriptors from previously built models**')
        Xlist = list(pd.read_csv('Slimmed_Descriptors.csv').columns)
        desc_subset = desc[Xlist]
        st.write(desc_subset)
        st.write(desc_subset.shape)

        # Apply trained model to make prediction on query compounds
        build_model(desc_subset)
else:
        st.info('Upload input data in the sidebar to start!')