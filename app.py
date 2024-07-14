import streamlit as st
import pandas as pd

# Set page layout to wide
st.set_page_config(layout="wide")

# Function to read Excel file and display table
def display_summary(company_name):
    # Assuming you have predefined paths or a method to select the correct file based on company_name
    file_path = f"{company_name}.xlsx"
    
    # Read Excel file into DataFrame
    df = pd.read_excel(file_path)
    
    # Display DataFrame with wrap text enabled
    st.table(df.style.set_properties(**{'white-space': 'normal', 'word-wrap': 'break-word'}))

# Main Streamlit app code
def main():
    st.title('Concall Screener')
    
    # Company selection dropdown
    company_name = st.selectbox('Select a company', ['comp1', 'comp2'])
    
    if company_name:
        display_summary(company_name)

if __name__ == '__main__':
    main()

