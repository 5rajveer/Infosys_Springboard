# 🤖 AI Code Assistant (Integrated System)
This project implements an integrated AI Code Assistant using Streamlit for the frontend, SQLite for user authentication, and multiple Hugging Face transformer models for core AI functionalities like code explanation and code generation. The system is designed to run efficiently on a GPU-enabled environment like Google Colab using pyngrok to expose the Streamlit application via a public URL.

# 🌟 Features
User Authentication: Secure login and registration using bcrypt for password hashing and PyJWT for session management.

Role-Based Access: Supports different user roles (Admin, General User, Developer, Student).

Code Explanation: Explains code snippets in simple terms.

Code Generation: Generates code based on a natural language prompt.

Specialized Models: Uses different large language models (LLMs) optimized for specific tasks:

Gemma-2b-it (Google): Optimized for Python code explanation (chat-template-based).

DeepSeek-Coder-1.3b-instruct (DeepSeek-AI): Optimized for generic code generation and non-Python code explanation.

CodeBERT (Microsoft): Loaded, potentially for future features like code search or retrieval (though not directly used in the current version's core logic).

# 💡 Technical Approach & Methodology
The application is structured into three main components: Authentication Backend, AI Model Configuration, and the Streamlit Frontend.

# 1. 🔐 Authentication Backend
Database: A local SQLite database (integrated_app.db) is used to store user data.

Schema: The users table stores email (Primary Key), password_hash (BLOB), and role (TEXT).

Security (Password Hashing): The register_user function uses the bcrypt library and bcrypt.gensalt() to securely hash and salt user passwords before storing them. This prevents storage of plaintext passwords.

Session Management (JWT): The authenticate_user function generates a JSON Web Token (JWT) upon successful login.

The JWT payload includes sub (email) and role and has a 2-hour expiration time (exp) using the HS256 algorithm and a secret key.

The Streamlit app checks for and decodes this token to manage the user session and determine access.

# 2. 🧠 AI Model Configuration & Deployment
Environment: The code is optimized for GPU usage (checked via torch.cuda.is_available()).

Model Caching: The @st.cache_resource decorator is used for the setup_ai_models function. This is critical for performance in Streamlit, ensuring the large models are loaded into memory only once across all user sessions and reruns.

Efficient Loading (Quantization): To reduce memory footprint and increase inference speed, the LLMs (Gemma and DeepSeek) are loaded using the BitsAndBytes (4-bit quantization) configuration (load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16).

Model-Task Mapping:

Code Explanation (Python): Uses Gemma-2b-it with a carefully configured gemma_chat_template to format the code explanation request as a chat prompt, leveraging the model's instruction-following capabilities.

Code Explanation (Other Languages) & Code Generation: Uses DeepSeek-Coder-1.3b-instruct, which is specialized for coding tasks and multilingual code processing.

Inference: Inference for both tasks uses torch.no_grad() to save memory and optimizes generation with parameters like max_new_tokens, do_sample, and a low temperature for generation (Code Gen: 0.2 for deterministic code; Code Explain: 0.7 for more creative/human-like text).

# 3. 🌐 Streamlit Frontend & Deployment
Interface: The application uses the Streamlit library for a simple, interactive web interface featuring separate tabs for Login/Register and two main functionalities: Code Explanation and Code Generation.

State Management: Streamlit's st.session_state is used to persist the user's JWT token and the loaded AI models across reruns.

Deployment (Colab/ngrok): The final cell orchestrates the deployment:

The entire Python script is saved to integrated_app.py.

pyngrok is configured and initiated to create a secure tunnel from the local Colab port (8501) to a public URL.

The Streamlit app is launched in the background (&) using streamlit run on the specified port.
🛠️ Observations & Problem Resolution
### Execution Summary Table

| Step              | Observation                                                                 | Resolution                                                                                                                                                                                                 |
|-------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Initial Execution | The AI Model Configuration section failed with a `SyntaxError: unterminated f-string literal`. | This error occurred because the multiline Python f-string used for `gemma_chat_template` was incorrectly escaped within the outer multiline string (`"""..."""`) in the notebook structure, causing a conflict in handling newline characters (`\n`). |
| Fix               | Code was refactored into a complete Python script (`integrated_app.py`).     | Within the final script, newline characters (`\n`) inside the chat template strings and `explain_code` f-strings were double-escaped to `\\n`. This ensures Python writes a literal `\n` to the file, which the Streamlit app then interprets correctly. |
| Final Run         | The complete application ran successfully.                                   | Models were loaded, a public ngrok URL was generated, and the Streamlit app started in the background. ✅ The system is ready for user interaction via the public URL.                                      |

