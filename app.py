import streamlit as st
import pandas as pd

def main():
    st.title("Basic Data Exploration")

    # Upload CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:

        # Read the csv file into a DataFrame
        df = pd.read_csv(uploaded_file)

        # Display data in a table
        st.write("### Data Preview")
        st.dataframe(df)

        # Provide basic statistics
        st.write("### Basic Statistics")
        st.write("Mean:")
        st.write(df.mean())
        st.write("Median:")
        st.write(df.median())
        st.write("Standard Deviation")
        st.write(df.std())

if __name__ == "__main__":
    main()
