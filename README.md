# 🧠 LearnMate — AI Study Assistant

LearnMate is a beginner-friendly AI study assistant powered by Google's Gemini API.

It is designed to help users understand topics through simple explanations, examples, and supportive guidance.

The project is built with Python and demonstrates how to integrate a generative AI model into a real application.


## ✨ Features

- 💬 Ask questions about any subject
- 🧠 Get simple, beginner-friendly explanations
- 💡 Receive examples to make concepts easier to understand
- 🔄 Continue a conversation with Gemini
- 🛡️ Handle empty input and API errors gracefully
- 🚪 Exit the application anytime with `exit`
- 🔐 Keep the Gemini API key in environment variables


## 🛠️ Technologies Used

- **Python** — Main programming language
- **Google Gemini API** — Provides the AI capabilities
- **Google GenAI SDK** — Connects the Python application to Gemini
- **python-dotenv** — Loads environment variables from the .env file


## 📂 Project Structure

```text
ai-study-assistant/
│
├── app.py              # Main application logic
├── config.py           # Gemini API configuration
├── prompts.py          # AI system instructions
├── messages.py         # User-facing messages
├── requirements.txt    # Python dependencies
├── .env                # API key (not uploaded to GitHub)
├── .env.example        # Example environment configuration
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```


## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd ai-study-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project folder and add:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own Gemini API key.

### 6. Run LearnMate

```bash
python app.py
```


## 🔐 Environment Variables

LearnMate uses an environment variable to securely store the Gemini API key.

Create a `.env` file in the project folder:

```text
GEMINI_API_KEY=your_api_key_here
```

Never share or commit your real API key to GitHub.

The `.env` file is included in `.gitignore`, while `.env.example` provides a safe template for other users.


## 💬 Usage

Start LearnMate with:

```bash
python app.py
```

Once the application starts, you can enter a question at the prompt.

Example:

```text
🧠 Ask LearnMate: What is artificial intelligence?

🧠 LearnMate:
Artificial intelligence (AI) is ...
```

You can continue asking questions, and LearnMate maintains the conversation during the current session.

To exit the application, type:

```text
exit
```


