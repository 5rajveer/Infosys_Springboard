# Project: CodeGenie - AI Code Generation & Explanation Platform

# 1. Overview

CodeGenie is a full-stack web application designed to serve as an intelligent partner for developers and learners. It provides a seamless interface for generating code from natural language prompts and, crucially, for understanding existing code through detailed, user-friendly explanations.

The platform is built around a robust backend leveraging state-of-the-art Hugging Face models for its core AI functionalities. It also includes a comprehensive admin dashboard for platform monitoring, user management, and AI performance analytics.

# 2. Core Features

For Users:

Secure Authentication: Standard user auth system with "Login," "Sign Up," and "Forgot Password" functionalities.

# 1. Generate Code: A primary interface where users can:

Enter a natural language prompt (e.g., "write a python function to check for a palindrome").

Select a target programming language (e.g., Python, C++, JavaScript, SQL).

Receive AI-generated code complete with syntax highlighting.

# 2. Explain Code: An integrated feature that allows users to:

Take the generated code (or paste their own in the "Code Explainer" section).

Select an explanation style (e.g., "Beginner-Friendly," "Technical Deep-Dive," "Step-by-Step Walkthrough").

Receive a detailed, natural language explanation tailored to their chosen audience, including summary tables that show how the code handles different inputs.

# 3. Provide Feedback: A simple-to-use feedback system (1-5 star rating and optional comments) for every AI-generated output, allowing for continuous model improvement.

For Admins (Admin Dashboard):

Overview Metrics: A high-level snapshot of platform health, tracking:

Total Queries

Total Feedback Submissions

Average User Rating

Active Users

Feedback Management: A detailed table viewing all user feedback, including timestamps, user IDs, ratings, comments, and the original query.

Query & Language Analytics:

Queries & Charts: Visual breakdowns of "Top Trending Queries" and a "Query Timeline" to spot trends.

Languages: "Language Usage" tables and charts (bar, pie) showing the distribution of languages requested by users.

Code Quality Metrics: Granular metrics on AI model performance, including:

Execution Success %

Python Syntax OK %

Runtime Performance Distributions

Member Management (Password Protected):

Registered Members: A complete list of all users with their login history, query counts, and average ratings.

User Activity: A powerful tool to select a specific user and audit their entire activity log (logins, queries, feedback, etc.).

Member Operations: The ability to add or delete members from the platform.

# 3. Project Approach

The project's approach is to create a holistic, closed-loop system for code-related AI. It's not just a "prompt-in, code-out" tool.

Generation: Provide users with immediate utility by generating functional code snippets.

Education: Instantly bridge the gap between "getting code" and "understanding code" with the "Explain Code" feature. This positions the tool as a learning assistant, not just a generator.

Evaluation (Human-in-the-Loop): The feedback system is central. It captures real-world user satisfaction, which is then...

Observation & Iteration: ...fed directly into the admin dashboard. This allows administrators to observe user behavior (Top Queries), model performance (Code Quality), and user sentiment (Feedback/Ratings) in one place. This data is essential for fine-tuning models, fixing bugs, and improving the user experience.

# 4. Methodology & AI Models

The application's AI capabilities are powered by a strategic combination of specialized Hugging Face models, each selected for its strength in a specific domain.

# 1. For Code Generation (Gemma & DeepSeek)

This feature maps a user's natural language prompt to a functional code block.

# Models: DeepSeek CodeBert Gemma.

Why: These are state-of-the-art (SOTA) models trained specifically on massive (trillions of tokens) code-centric datasets.

# Process:

The user's prompt ("write a code to check palindrome") and chosen language ("Python") are formatted into a specific instruction prompt for the model.

This prompt is sent to the backend, which calls the DeepSeek Coder or Gemma model.

These models are highly adept at text-to-code tasks, generating accurate and syntactically correct code.

The generated code is returned to the frontend for display.

# 2. For Code Explanation (CodeBERT)

This feature maps a block of source code to a natural language explanation.

# Model: CodeBERT.

Why: CodeBERT is a bimodal model, meaning it was pre-trained on both natural language (documentation) and programming language (code) simultaneously. This makes it exceptionally good at "code-to-text" tasks, such as generating code documentation or, in this case, explanations.

# Process:

The user's code (either just generated or pasted) is sent to the backend.

The user's chosen style ("Beginner-Friendly") is included as a parameter.

This data is passed to a CodeBERT model (likely one fine-tuned for summarization or documentation) to generate the "Beginner-Friendly explanation."

The model's natural language output is returned to the frontend.

# 5. Observations & Key Insights (from Admin Dashboard)

The admin dashboard is the project's "brain," enabling data-driven decisions. The key observations it provides are:

User Engagement: The "Overview Metrics" and "Query Timeline" directly show how, when, and how much the platform is being used. A rising query count and active user base indicate healthy growth.

Model Performance (Quantitative): The "Code Quality Metrics" (Execution Success %, Syntax OK %) provide an objective, automated score for the code generation models. This is crucial for A/B testing new models or prompts.

Model Performance (Qualitative): The "Feedback" tab is a goldmine for qualitative data. An admin can filter for all "1-star" ratings to immediately find examples where the models are failing and what the common user complaints are.

Popular Use Cases: The "Top Trending Queries" and "Language Distribution" charts clearly show what users want to do (e.g., "addition of two no") and in which languages. This can guide resource allocation, such as improving performance for the most-requested languages.

Security & Auditing: The "Member Management" and "User Activity" tabs provide a complete audit trail, essential for platform security and for debugging issues reported by a specific user.

# Project Architecture

┌─────────────────────────────────────────────────────────────────┐
│                        STREAMLIT APP (app.py)                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────────┐    ┌──────────────────────────┐   │
│  │   CODEGENIE PAGE         │    │  ADMIN DASHBOARD PAGE    │   │
│  │ (Main Application)       │    │ (Analytics & Management) │   │
│  │                          │    │                          │   │
│  │ • Generate Code          │    │ • Overview Metrics       │   │
│  │ • Explain Code           │    │ • Ratings & Feedback     │   │
│  │ • Provide Feedback       │    │ • Queries & Charts       │   │
│  │ • Rate Code              │    │ • Language Usage         │   │
│  └──────────────────────────┘    │ • Code Quality           │   │
│           │                       │ • Member Management      │   │
│           │                       └──────────────────────────┘   │
│           │                                │                     │
│           └────────────┬────────────────────┘                     │
│                        │                                          │
└────────────────────────┼──────────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┬──────────────────┐
        │                │                │                  │
        ▼                ▼                ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ User History │  │   Feedback   │  │  User Mgmt   │  │Admin Dashboard│
│  Module      │  │   Module     │  │   Module     │  │   Module     │
└──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
        │                │                │                  │
        └────────────────┼────────────────┼──────────────────┘
                         │                │
        ┌────────────────┼────────────────┴──────────────┐
        │                │                               │
        ▼                ▼                               ▼
┌─────────────────┐  ┌──────────────────┐  ┌──────────────────────┐
│  Dual Logging:  │  │   User Activity  │  │   User Management    │
│                 │  │    Module        │  │      Functions       │
│ • feedback_log  │  │                  │  │                      │
│   .json         │  │ • user_activity  │  │ • register_user()    │
│                 │  │   .json          │  │ • log_user_activity()│
│ • user_history  │  │                  │  │ • get_all_users()    │
│   .json         │  │ (Centralized     │  │ • get_user_activity()│
│                 │  │  Activity Log)   │  │ • replace_user()     │
│                 │  │                  │  │ • delete_user()      │
└─────────────────┘  └──────────────────┘  └──────────────────────┘
        │                │                       │
        └────────────────┼───────────────────────┘
                         │
                         ▼
        ┌────────────────────────────────┐
        │   JSON STORAGE (streamlit_app/) │
        ├────────────────────────────────┤
        │ • users.json                   │
        │ • user_activity.json           │
        │ • feedback_log.json            │
        │ • user_history.json            │
        └────────────────────────────────┘

# Admin Dashboard Data Flow

Admin Clicks "Admin Dashboard" Button
            │
            ▼
    Dashboard Page Loads
            │
            ├─► get_dashboard_stats()
            │   │
            │   ├─► Read feedback_log.json
            │   ├─► Read user_history.json
            │   │
            │   └─► Calculate:
            │       • average_rating
            │       • total_feedback
            │       • top_queries
            │       • language_stats
            │       • code_quality metrics
            │
            ├─► get_all_users()
            │   ├─► Read users.json
            │   └─► Return user list
            │
            └─► Display Tabs:
                ├─► Overview Metrics
                │   ├─► Total Queries
                │   ├─► Total Feedback
                │   ├─► Avg Rating
                │   └─► Active Users
                │
                ├─► Ratings & Feedback
                │   ├─► Rating Overview (chart)
                │   └─► Feedback Details (table)
                │
                ├─► Queries & Charts
                │   ├─► Top 5 Queries (table + chart)
                │   └─► Query Timeline (line chart)
                │
                ├─► Language Usage
                │   ├─► Statistics (table)
                │   └─► Breakdown (bar + pie chart)
                │
                ├─► Code Quality
                │   ├─► Summary (metrics)
                │   └─► Details (runtime + syntax charts)
                │
                └─► Member Management
                    ├─► All Members (table with stats)
                    ├─► User Activity (select + history)
                    └─► Member Operations (add/replace/delete)
