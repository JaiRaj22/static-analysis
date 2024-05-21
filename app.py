import streamlit as st
import radon.raw as rr
import radon.metrics as rm
import radon.complexity as rc
import altair as alt
import plotly.express as px
from app_utils import get_reserverd_words
import parser
import pandas as pd

def convert_df(dict):
    return pd.DataFrame(list(dict.items()), columns=['Keywords', 'Counts'])

def main():
    st.title("Static code analysis App")
    
    with st.form(key="my_form"):
        raw_code = st.text_area("Enter your code here")
        submit = st.form_submit_button("Submit")
        
    
    tab1, tab2, tab3, tab4 = st.tabs(["Code analysis","Reserved kyewords", "Identifier", "AST"])
    results = get_reserverd_words(raw_code)
    if submit:
        with tab1:
            st.subheader("Code analysis")
            with st.expander("original code"):
                st.code(raw_code)
            st.subheader("Metrics")
            analysis = rr.analyze(raw_code)
            st.write(analysis)
            
            maintain_index = rm.mi_visit(raw_code, True)
            
            result = rm.h_visit(raw_code)
            
            col1, col2 = st.columns(2)
            col1.metric(label="Maintainability Index", value=maintain_index)
            
            with st.expander("halstead metrics"):
                st.write(result[0])
            
        with tab2:
            st.subheader("Reserved keywords")
            result_df = convert_df(results["reserved"])
            my_chart = alt.Chart(result_df).mark_bar().encode(x="Keywords", y="Counts", color="Keywords")
            st.altair_chart(my_chart, use_container_width=True)
            t1,t2 = st.tabs(["WordFrequency", "Piechart"])
            
            with t1:
                st.dataframe(result_df)
            with t2:
                fig2 = px.pie(values=results["reserved"].values(), names=results["reserved"].keys())
                st.plotly_chart(fig2)
            
        with tab3:
            st.subheader("Identifier")
            result_df = convert_df(results["identifiers"])
            my_chart = alt.Chart(result_df).mark_bar().encode(x="Keywords", y="Counts", color="Keywords")
            st.altair_chart(my_chart, use_container_width=True)
            
            
        with tab4:
            st.subheader("AST")
            ast_results = parser.make_ast(raw_code)
            st.json(ast_results)
    
if __name__ == "__main__":
    main()