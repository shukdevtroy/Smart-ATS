import streamlit as st
import openai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()  # Load all environment variables

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can choose any other model as per your requirement
        messages=[{"role": "user", "content": input}]
    )
    return response.choices[0].message['content']

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of the tech field like Software Engineering, Software Developer, Systems Engineering, Data Scientist, data analysis, Machine Learning Engineer, AI Engineer, Database Administrator, Network Engineer, Cybersecurity Analyst, Security Engineer, DevOps Engineer, Cloud Engineer, Embedded Systems Engineer, Frontend Developer, Backend Developer, Full Stack Developer, Quality Assurance (QA) Engineer, Application Support Analyst, IT Project Manager, IT Consultant, UX/UI Designer, Systems Architect, Site Reliability Engineer (SRE), Business Intelligence (BI) Developer, Big Data Engineer, Block-chain Developer, Game Developer, Augmented Reality (AR) Developer, Virtual Reality (VR) Developer, Natural Language Processing (NLP) Engineer, Internet of Things (IoT) Engineer, Systems Administrator, Technical Support Specialist, Mobile App Developer, and IT Operations Manager. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
the best assistance for improving the resumes. Assign the percentage Matching based 
on JD and the missing keywords with high accuracy.
resume: {text}
description: {jd}

I want the response in the following format:
JD Match: %
Missing Keywords: []
Profile Summary: 
"""

# Function to generate and return the report content
def generate_report(match, keywords, summary):
    report = f"JD Match: {match}\nMissing Keywords: {keywords}\nProfile Summary: {summary}"
    return report

# Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume for ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        formatted_prompt = input_prompt.format(text=text, jd=jd)
        response = get_openai_response(formatted_prompt)

        # Parse the response
        match_percentage = response.split("\n")[0].split(": ")[1]
        missing_keywords = response.split("Missing Keywords: ")[1].split("\n")[0]
        profile_summary = response.split("Profile Summary: ")[1]

        # Display results
        st.markdown(f"**JD Match:** {match_percentage}")
        st.markdown(f"**Missing Keywords:** {missing_keywords}")
        st.markdown(f"**Profile Summary:** {profile_summary}")

        # Generate and add the download button for the report
        report_content = generate_report(match_percentage, missing_keywords, profile_summary)
        st.download_button("Download Report", report_content, "report.txt", "text/plain")
