import streamlit as st
import pandas as pd

#Mapping dataframe
company_name_df = pd.read_excel('company_name_map.xlsx')

# Set page layout to wide
st.set_page_config(layout="wide")

# Function to read Excel file and display table
def display_summary(company_name):
    scip_code_df = company_name_df[company_name_df['company_name']==company_name]
    scrip_code = scip_code_df['scrip_code'].iloc[0]
    # Assuming you have predefined paths or a method to select the correct file based on company_name
    file_path = f"./data/{scrip_code}.xlsx"
    
    # Read Excel file into DataFrame
    df = pd.read_excel(file_path)
    
    # Display DataFrame with wrap text enabled
    st.table(df.style.set_properties(**{'white-space': 'normal', 'word-wrap': 'break-word'}))

# Main Streamlit app code
def main():
    st.title('Concall Screener')
    
    # Company selection dropdown
    company_name = st.selectbox('Select a company', company_name_df['company_name'].to_list())
    
    if company_name:
        display_summary(company_name)

if __name__ == '__main__':
    main()

