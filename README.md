# Smart ATS

## Overview

Smart ATS is a web application built using Streamlit and OpenAI's GPT-3.5 Turbo model, designed to help users improve their resumes for Application Tracking Systems (ATS). This tool evaluates resumes against job descriptions, providing users with valuable feedback to enhance their application.

## Features

- **Job Description Input**: Users can paste a job description into a text area.
- **Resume Upload**: Users can upload their resumes in PDF format.
- **ATS Evaluation**: The application analyzes the resume against the job description and provides:
  - JD Match Percentage
  - Missing Keywords
  - Profile Summary
- **Downloadable Report**: Users can download a detailed report in text format.

## Requirements

- Python 3.7 or higher
- Streamlit
- OpenAI API client
- PyPDF2
- python-dotenv

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/smart-ats.git
   cd smart-ats
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Input the job description and upload your resume in PDF format.

4. Click the "Submit" button to receive feedback on your resume.

5. Review the JD match percentage, missing keywords, and profile summary.

6. Download the report for further reference.

## Code Explanation

- **Imports**: The application imports necessary libraries for functionality, including `streamlit`, `openai`, `os`, `PyPDF2`, and `dotenv`.

- **Environment Variables**: The application loads environment variables using `dotenv`, allowing for secure management of the OpenAI API key.

- **OpenAI Response**: The `get_openai_response` function sends user input to OpenAI and returns the model's response.

- **PDF Text Extraction**: The `input_pdf_text` function extracts text from the uploaded PDF resume.

- **Prompt Template**: The prompt template is structured to guide the AI in evaluating resumes based on the job description.

- **Report Generation**: The `generate_report` function compiles the results into a formatted string for easy reading and download.

- **Streamlit Interface**: The main interface allows users to input job descriptions, upload resumes, and view results in a user-friendly format.

## Contributing

Feel free to submit issues or pull requests for improvements. Contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [OpenAI](https://openai.com/)
- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [dotenv](https://pypi.org/project/python-dotenv/)

For any questions or feedback, please reach out!
