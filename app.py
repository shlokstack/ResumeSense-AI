import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import pypdf
import re
from prompts import template
from dotenv import load_dotenv
import os
load_dotenv()

# Page configuration for text to display in browser tab
st.set_page_config(
    page_title="ResumeIQ Resume Analyser",
    layout="wide"
)

# Title and description
st.title("🎓 ResumeIQ - AI Resume Analyzer")
st.write("Upload your resume from the sidebar to receive an ATS score and personalized feedback.")

with st.sidebar:
    st.title("🎓 ResumeIQ")
    st.write("Upload your resume to receive an ATS analysis.")
    upload = st.file_uploader("Upload file", type="pdf")
    text = ""
    if upload is not None:
        pdf = pypdf.PdfReader(upload)
        for page in pdf.pages:
            extract = page.extract_text()
            if extract:
                text += extract+"\n"
        if not text.strip():
            st.error("No readable text found in the pdf")
    button = st.button("Analyse Resume", disabled=(upload is None))
    
llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature= 0.4
)

prompt = PromptTemplate(
    input_variables=["text"],
    template=template
)
if button:
    if upload is None:
        st.error("Please upload a valid resume")
    elif not text.strip():
        st.error("This PDF contains no selectable text. Please upload a text-based resume.")
    else:
        try:
            chain = prompt | llm
            with st.spinner("Analyzing your resume... This may take a few seconds."):
                response = chain.invoke({"text":text})
                match = re.search(
                r'ATS\s*Score\s*:?\s*(\d{1,3})\s*/\s*100',
                response.content,
                re.IGNORECASE
            )
                if match:
                    ats_score = int(match.group(1))
                else:
                    ats_score = 0
            # Protect the model from hallucinating, for eg, giving score as 105/100
            ats_score = max(0, min(100, ats_score)) 
            st.subheader("Resume Analysis")
            
            with st.container():
                st.subheader("ATS Score")
                st.progress(ats_score / 100)
                if ats_score >= 80:
                    st.success(f"Excellent ATS Score: {ats_score}/100 🎉")
                elif ats_score >= 60:
                    st.warning(f"Good ATS Score: {ats_score}/100 👍")
                else:
                    st.error(f"Low ATS Score: {ats_score}/100 🚨")

                st.metric(
                    label="Overall ATS Score",
                    value=f"{ats_score}/100"
                )
            st.divider()
            # Formatting to remove printing of duplicate ATS score response by the model.
            analysis = re.sub(
            r"# ATS Score.*?(?=\n# Strengths)",
            "",
            response.content,
            flags=re.DOTALL | re.IGNORECASE
        )
            st.markdown(analysis)
        except Exception as e:
            st.error(f"Error:{e}")