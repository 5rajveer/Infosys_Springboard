# Infosys CodeGenie AI Explainer and Code Generator: Milestone-2
# Code Generator 
# 📜 Overview
The primary goal of this project is to offer a straightforward way to assess the code generation capabilities of different LLMs. Instead of relying solely on subjective evaluation, this tool uses the radon library to provide quantitative metrics on code complexity, maintainability, and size. This data-driven approach allows for a more objective comparison of model performance.

#n✨ Key Features
Interactive UI: Built with ipywidgets for an easy-to-use interface directly within the notebook.

Multiple Model Support: Benchmarks several popular code-generation models simultaneously.

Quantitative Analysis: Automatically evaluates the generated code using three key metrics.

Dynamic Visualization: Generates bar charts with matplotlib to visually compare the performance of the models.

Flexible & Extensible: Easily add new models to the benchmark or customize the evaluation prompts.

# 🔬 Methodology
The benchmarking process follows a clear, automated methodology for each model selected:

Model Loading: The script loads a specified model and its tokenizer from Hugging Face. To improve performance and avoid redundant downloads, models are cached in memory after their first use. It uses bfloat16 precision and device_map="auto" to efficiently utilize available GPU resources.

Code Generation: The user provides a prompt (either from a predefined list or a custom input). This prompt is passed to the loaded model, which generates a code snippet. The script then intelligently extracts the Python code from markdown code blocks (e.g., ```python...```) in the model's response.

Code Evaluation: The extracted code is analyzed using the radon library, a tool for static code analysis in Python. It calculates three distinct metrics to quantify the code's quality.

Visualization: After all selected models have been processed, the collected metrics are visualized as bar charts for direct comparison.

Evaluation Metrics
Code quality is measured using the following radon metrics:

## 📊 Code Quality Metrics Explained

| Metric                  | Description                                                                                   | Interpretation                                                                 |
|-------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Cyclomatic Complexity   | Measures the number of linearly independent paths through a program's source code.            | Lower score = simpler, easier-to-test code. *(Lower is better)*                |
| Maintainability Index (MI) | A score from 0 to 100 that represents how easy it is to support and change the code.       | Higher score = easier to maintain. 85–100 = high, <65 = low. *(Higher is better)* |
| Logical Lines of Code (LOC) | The number of executable lines of code, ignoring comments and blank lines.               | Gauges conciseness of code. *(Context-dependent)*                              |

# 🚀 How to Use
Follow these steps to run the benchmarking tool:

1. Installation
Run the first code cell to install all the necessary libraries.

Bash

!pip install -q -U transformers accelerate bitsandbytes radon ipywidgets matplotlib
2. Hugging Face Authentication
For models like Gemma, you need to be authenticated with Hugging Face. The notebook checks for an environment variable named HF_TOKEN.

Important: Before running, ensure you have set an environment variable named HF_TOKEN with your Hugging Face access token. You may also need to accept the terms of use on the Hugging Face pages for gated models like Gemma.

3. Running the Notebook
Execute the cells in order. The notebook is divided into two main interactive sections.

UI #1: Benchmark All Models
This interface allows you to run a prompt against all five models at once.

Select a pre-defined prompt from the dropdown or type a custom one.

Click the "Benchmark All Models" button.

The notebook will generate code, print the outputs and metrics, and display comparative bar charts.

UI #2: Inspect Selected Models
This interface provides more flexibility by allowing you to choose which models to compare.

Select or enter a prompt.

Use the checkboxes to select the desired models.

Click the "Generate & Inspect Selected" button.

# 🤖 Models & Observations
The notebook is configured to benchmark the following models. The example run for the prompt "Create a Python function to implement the bubble sort algorithm" provides key insights into their behavior.

## 🔍 Model Evaluation Summary

| Model              | Generated Output & Observations                                                                 | Metrics (Complexity, MI, LOC) |
|-------------------|--------------------------------------------------------------------------------------------------|-------------------------------|
| DeepSeek-Coder-1.3B | ✅ Generated a correct, standard, and clean bubble sort implementation.                          | (4, 68.59, 7)                 |
| Phi-2-2.7B         | ✅ Generated a correct and functional implementation, nearly identical to DeepSeek's output.     | (4, 68.59, 7)                 |
| Stable-Code-3B     | ⚠️ Failed to generate valid code. It produced a list of descriptive requirements instead of the function itself, causing the radon analysis to fail. | (-1, -1, -1)                
Analysis of Results
From this single run, we can observe significant differences in model performance and reliability:

Top Performers: DeepSeek-Coder-1.3B and Phi-2-2.7B performed excellently, producing identical, functional code with good maintainability scores (68.59, which is moderately maintainable).

Instruction Following: Stable-Code-3B completely misunderstood the instruction to create a function, instead listing what the function should do. This indicates a potential weakness in following direct coding commands compared to the other models.

Environmental Dependencies: The failures of Gemma-2B-IT and Replit-Code-3B underscore the importance of environment setup, including authentication tokens and ensuring library versions are compatible with the model's tokenizer.

The generated plots visually confirm that for this specific task, DeepSeek-Coder and Phi-2 are the top performers based on the chosen metrics.
