# Infosys CodeGenie AI Explainer and Code Generator: Milestone 2 -> Code Generator 
# Code Generation LLM Benchmarking Tool
This project provides a comprehensive framework for benchmarking and evaluating the performance of various code-generation Language Learning Models (LLMs). Using an interactive interface built with ipywidgets in a Jupyter Notebook, users can input a programming prompt and receive generated code from multiple models simultaneously. The tool then evaluates the generated code based on key software quality metrics and visualizes the results for easy comparison.

# Methodology & Approach
The methodology is structured to provide a seamless workflow from model selection to performance visualization. The core approach involves three main stages: Generation, Evaluation, and Visualization.
# About Model's
| **Model**               | **Developer**     | **Parameters** | **Highlights**                                                                                           |
|------------------------|-------------------|----------------|-----------------------------------------------------------------------------------------------------------|
| DeepSeek-Coder-1.3B    | DeepSeek AI        | 1.3 Billion     | Trained on 2 trillion tokens (87% code, 13% English + Chinese). Supports 16K context window, project-level code completion, and infilling. |
| Phi-2-2.7B             | Microsoft          | 2.7 Billion     | Trained on synthetic NLP and filtered web data. Strong in reasoning, common sense, and language understanding. Open-source and designed for safe AI research. |
| Stable-Code-3B         | Stability AI       | 2.7 Billion     | Trained on 1.3 trillion tokens across 18 programming languages. Supports long context (16K), Fill-in-the-Middle (FIM), and rotary embeddings. Sometimes generates excessive output beyond prompt scope. |

# Setup and Configuration:

Dependencies: The environment is first prepared by installing essential Python libraries, including transformers for model interaction, accelerate and bitsandbytes for efficient model loading, and radon for code quality analysis.

Authentication: Access to models on the Hugging Face Hub is secured using an HF_TOKEN. The script is designed to fetch this token from Colab Secrets, ensuring secure handling of credentials.

Model Selection: A predefined dictionary MODELS maps user-friendly names to their Hugging Face model IDs. This allows for easy extension and management of the models to be tested.

# Code Generation:

Model Loading: The load_model_and_tokenizer function handles the download and loading of the specified model and its tokenizer. It incorporates a caching mechanism (loaded_models_cache) to avoid reloading models, saving significant time and computational resources on subsequent runs. Models are loaded in bfloat16 precision for improved performance on compatible GPUs.

Prompt Engineering: The generate_code function takes a user prompt and formats it for the model. It includes a specific chat template for deepseek-ai models to ensure optimal performance.

Inference: The code is generated using a pipeline with controlled parameters (max_new_tokens, temperature, top_p) to ensure the output is both relevant and concise.

Code Extraction: A regular expression is used to automatically extract the Python code from the model's raw output, which often includes explanatory text and markdown code blocks (e.g., ```python...```).

# Code Quality Evaluation:

Once the code is extracted, the evaluate_code function uses the radon library to perform a static analysis. This analysis yields objective metrics to quantify the quality of the generated code without executing it.

# The following key metrics are calculated:

| **Metric**                 | **Library Method**                    | **Description**                                                                 | **Interpretation**                                                                 |
|---------------------------|----------------------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Cyclomatic Complexity     | `radon.visitors.ComplexityVisitor`     | Measures the number of linearly independent paths through a program's source code. It indicates the code's complexity. | **Lower is Better** — simpler code is easier to test and maintain.                 |
| Maintainability Index (MI)| `radon.metrics.mi_visit`               | A score from 0 to 100 that measures how easy it is to support and change the code. It uses LOC, Halstead volume, and Cyclomatic Complexity. | **Higher is Better** — higher score means better maintainability.                  |
| Logical Lines of Code (LOC)| `radon.raw.analyze`                   | Counts the number of lines that contain actual code, excluding comments and blank lines. | **Context-Dependent** — lower LOC is concise, but higher LOC can be fine if well-structured. |

# Visualization and Interaction:

The plot_metrics function takes the evaluation results and generates three distinct bar charts to visually compare the models across the evaluated metrics.

Two interactive user interfaces are provided using ipywidgets for a user-friendly experience, allowing the user to either benchmark all models at once or select specific ones for a more focused comparison.

# Code Explanation
The notebook is divided into logical sections, each performing a specific task.

Section 1-3: Setup: These cells handle the initial setup, including installing libraries, managing the Hugging Face access token, and importing all necessary modules. The global configuration, such as the MODELS dictionary, is also defined here.

Section 4: Core Functions: This is the engine of the tool.

load_model_and_tokenizer(model_name): Loads a specified model and its tokenizer with caching.

generate_code(model, tokenizer, prompt): Generates and extracts clean code from a given prompt.

evaluate_code(code_string): Analyzes the generated code and returns a dictionary of quality metrics.

# Section 5: Visualization Function:

plot_metrics(results): Creates and displays bar charts comparing the Cyclomatic Complexity, Maintainability Index, and LOC for the generated code from each model.

# Section 6-8: Prompts & Interactive UI:

SAMPLE_PROMPTS: A list containing diverse prompts for testing the models across different domains (e.g., Python, SQL, Web Dev).

Interactive UI-1 & UI-2: These sections create the ipywidgets interfaces. They capture user input (either from a dropdown of sample prompts or a custom textarea), trigger the backend functions for generation and evaluation, and display the results, including the generated code, metrics, and comparison plots.

# Observations (Example Run)
The following observations are based on the sample output provided in the notebook for the prompt: "Create a Python function to implement the bubble sort algorithm."

| **Model**              | **Cyclomatic Complexity** 🔻 | **Maintainability Index** 🔺 | **Logical LOC** (Contextual) | **Generated Code Summary**                                                                                          |
|------------------------|------------------------------|-------------------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------|
| DeepSeek-Coder-1.3B    | 4                            | 68.59                         | 7                             | Generated only the required function. It was correct and concise.                                                   |
| Phi-2-2.7B             | 4                            | 84.83                         | 9                             | Generated the function and included a simple test case, which is helpful. This led to a very high MI score.         |
| Stable-Code-3B         | 12                           | 74.81                         | 38                            | Generated the requested bubble sort function but continued with selection and insertion sorts + test cases. Excessive output. |

# Analysis
Relevance: DeepSeek-Coder and Phi-2 provided highly relevant answers. Stable-Code-3B was less concise and included unsolicited additional code, which significantly increased its Complexity and LOC scores.

Maintainability: Phi-2 scored the highest on the Maintainability Index. Although it generated extra lines for testing, the code was well-structured and easy to understand.

Efficiency: For a straightforward task, DeepSeek-Coder provided the most direct and efficient solution without any extra code.
