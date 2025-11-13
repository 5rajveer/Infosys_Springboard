import streamlit as st
import os
import sys

# Ensure backend directory is on path (same approach used in app.py)
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if backend_dir not in sys.path:
    sys.path.append(backend_dir)

try:
    from backend.code_explainer_module import explain_code
    from backend.user_history_module import log_user_query
except Exception as e:
    # If imports fail, show a helpful message when running the page directly
    explain_code = None
    log_user_query = None
    _IMPORT_ERROR = e
else:
    _IMPORT_ERROR = None


def render_explain_only(user_id=None):
    """Render the Explain-Only UI.

    Parameters
    - user_id: optional user identifier (string). If provided, the explanation
      interaction will be logged to the user's history via log_user_query.
    """

    st.title("🔍 Explain Only — Paste Code to Explain")
    st.write("This view accepts a code snippet and returns an explanation. It does not generate new code.")

    if _IMPORT_ERROR:
        st.error(f"Could not import backend modules required for explanations: {_IMPORT_ERROR}")
        st.stop()

    code_input = st.text_area("Paste code here:", height=320, placeholder="def is_palindrome(s):\n    # ...")

    style = st.selectbox(
        "Explanation style:",
        ["Beginner-Friendly", "Technical Deep-Dive", "Step-by-Step Guide", "Real-World Examples", "Bullet Points"]
    )

    if st.button("Explain Code"):
        if not code_input or not code_input.strip():
            st.warning("Please paste some code to explain.")
        else:
            with st.spinner("Generating explanation..."):
                try:
                    explanation = explain_code(code_input, style)
                except Exception as e:
                    explanation = f"Error while generating explanation: {e}"

            st.subheader("Explanation")
            st.markdown(explanation)

            # Log the interaction to user history if available
            try:
                if log_user_query:
                    log_user_query(
                        user_id=user_id,
                        query=None,
                        language=None,
                        generated_code=code_input,
                        explanation=explanation,
                    )
            except Exception:
                # Logging failures should not block the UI
                pass


if __name__ == "__main__":
    # Allow running this file directly: streamlit run explain_only.py
    render_explain_only()
