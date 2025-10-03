# 🤖 Code Explainer Project
#💡 Approach: Dual-Layer Code Understanding
The "Code Explainer" utilizes a dual-layer analysis model to interpret code snippets:

Structural Analysis (The "What"): Using Python's ast module, the project extracts concrete structural features (e.g., number of functions, loops, and conditionals). This provides an objective measure of the code's complexity and composition.

Semantic Analysis (The "Meaning"): Employing state-of-the-art Transformer models (MiniLM, DistilRoBERTa, MPNet), the code is converted into high-dimensional numerical vectors (embeddings). These embeddings capture the semantic meaning and context of the code, allowing for comparison with other snippets.

# 🛠️ Methodology
The project pipeline is broken down into four key phases:

1. Structural Feature Extraction (AST)
A custom CodeAnalyzer class, inheriting from ast.NodeVisitor, is implemented to traverse the Abstract Syntax Tree of Python code.

Tools: Python's built-in ast and astor libraries.

Extracted Features: Counts of functions, classes, imports, loops (for and while), and conditionals (if, elif, else).

Visualization: Aggregated feature counts from multiple snippets are presented using a Bar Chart for easy comparison of structural complexity across the dataset.

2. Semantic Embedding Generation (Transformers)
Pre-trained language models, specifically tuned for code or general language understanding, are used to generate numerical representations (embeddings) for the input code.

Models Used: MiniLM, DistilRoBERTa, and MPNet.

Process: Each code snippet is tokenized using the model's specific tokenizer and passed through the model. The [CLS] token embedding is extracted as the vector representation of the entire code sequence.

Observation Point: The embedding size (hidden dimension) and the token count are noted for each model, highlighting differences in how models process and represent the same code snippet.

3. Model Comparison (PCA Visualization)
To visually compare how different Transformer models interpret the same piece of code, their high-dimensional embeddings are reduced.

Technique: Principal Component Analysis (PCA) is applied to the embeddings, reducing them to a 2D space.

Visualization: A Scatter Plot is generated, showing the position of each model's embedding for a single, standard snippet.
# 📊 Observations
The analyses conducted provide insights into both the code snippets themselves and the capabilities of the language models used:

Structural Analysis Observations:
Complexity Metrics: The AST parser successfully breaks down snippets to provide quantifiable metrics, allowing complex logic (like recursion in the quick sort example) to be analyzed by its component parts (e.g., number of functions and conditionals).

Visualization Utility: The bar chart effectively aggregates the complexity of the entire dataset, quickly highlighting which structural features (e.g., conditionals vs. loops) are most dominant.
