**Support Agent Chatbot**

A chatbot designed to assist with "how-to" questions related to four **Customer Data Platforms (CDPs)**: **Segment**, **mParticle**, **Lytics**, and **Zeotap**. This chatbot references the official documentation of these platforms to provide accurate guidance on tasks and solutions.

## Features

- **Respond to "How-to" Queries**:
    - Provides detailed responses to questions about using features or completing tasks within each CDP.
    - Example: "How can I add a new source in Segment?"

- **Information Extraction from Documentation**:
  - Retrieves and utilizes relevant details from the official documentation of the specified CDPs.

- **Question Variability Support**:
  - Understands different ways questions might be phrased, including longer or less specific queries.

**Cross-CDP Feature Comparisons**:
  - Answers questions comparing functionalities or workflows across the four platforms.
  - Example: "What are the differences between audience creation in Segment and Lytics?"

- **Advanced "How-to" Questions**:
  - Handles detailed or unique "how-to" queries for specific platforms.
  Example: "How do I set up data integration with Zeotap?"


## Technologies Used

- **Web Scraping**:
Utilizes [Playwright](https://playwright.dev/) for dynamic content and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for static content.
- **Natural Language Processing**:
Powered by the [Groq API](https://groq.com/) (`llama-3.3-70b-versatile`).
- **Web Framework**:
Built with [Streamlit](https://streamlit.io/) for an interactive interface.
- **Programming Language**: Python.
- **Data Storage**: Stores scraped documentation in JSON format.

## Installation

1. **Clone the Repository**:
Clone the project to your local machine:
```bash
   git clone https://github.com/not-indro/support-agent-chatbot.git
   cd support-agent-chatbot
   ```

2. **Set Up a Virtual Environment**:
Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**:
Install Required Dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Set up a .env file in the project's root directory and include your Groq API key:
     ```plaintext
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - Copy the same API key and paste it into the **secrets.toml** file in the *.streamlit* folder.

---

## Usage

### Step 1: Scrape Documentation
Run the scraping script to gather information from the official documentation of the four CDPs:
```bash
python doc_scraping.py
```
This generates a docs.json file containing the extracted documentation after scraping.

### Step 2: Launch the Chatbot
Start the chatbot interface by running the Streamlit application:
```bash
streamlit run app.py
```

### Step 3: Interact with the Chatbot
- Type your query into the text input field and press **Submit**.
- The chatbot will analyze the documentation and provide a relevant answer.
- A history of the last three questions and answers will be displayed in the sidebar.


## Project Structure

```
support-agent-chatbot/
│
├── app.py                # Streamlit app for the chatbot interface
├── chatbot.py            # Chatbot logic powered by the Groq API
├── doc_scraping.py        # Web scraping script to collect documentation
├── docs.json         # Generated JSON file containing documentation data
├── .env                  # File to store environment variables
├── requirements.txt      # Dependencies for the project
└── README.md             # Documentation for the project
```

## Acknowledgments

- Special thanks to [Playwright](https://playwright.dev/) for web automation.
- Gratitude to [Groq](https://groq.com/) for providing an advanced LLM API.
- Appreciation to [Streamlit](https://streamlit.io/) for the user-friendly interface.
