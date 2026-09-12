# LIBER_ANATHEMA8
import streamlit as st


# browser tab settings
st.set_page_config(
    page_title="LIBER_ANATHEMA",
    page_icon="💀",
    layout="centered"
)


# custom dark design
st.markdown("""
<style>

.stApp {
    background-color: #0d0d0d;
    color: #e6e6e6;
}

h1 {
    text-align: center;
    letter-spacing: 4px;
}

[data-testid="stFileUploader"] label {
    color: #e6e6e6 !important;
    font-weight: 600;
}

[data-testid="stFileUploader"] button {
    color: #FFFFFF !important;
    background-color: #222222 !important;
    border: 1px solid #666666 !important;
}

</style>
""", unsafe_allow_html=True)


st.title("LIBER_ANATHEMA")

st.markdown(
    "<p style='text-align:center; color:#FFFFFF;'>Python Syntax Corrector</p>",
    unsafe_allow_html=True
)
uploaded_file = st.file_uploader(
    "Choose Python file:",  # text shown above the upload button
    type=["py"]  # only allows .py Python files
)


if uploaded_file:  # only runs the code below if the user uploads a file

    # gets the uploaded file and converts it into normal readable text
    code = uploaded_file.getvalue().decode("utf-8")


    try:  # try to check the Python code

        # checks if the uploaded code has valid Python syntax
        compile(code, uploaded_file.name, "exec")

        st.markdown(
            """
            <div style="
                background-color:#7fff00;
                color:#f8f8ff;
                padding:14px;
                border-radius:8px;
                box-shadow: 0 0 0px #39FF14;
                font-weight:bold;
                margin-bottom:12px;
            ">
                ✅ No syntax errors
            </div>
            """,
            unsafe_allow_html=True
        )

    except SyntaxError as error:  # runs if Python finds a syntax error

        st.markdown(
    """
    <div style="
        background-color:#E63946;
        color:#FFFFFF;
        padding:14px;
        border-radius:8px;
        box-shadow: 0 0 10px #E63946;
        font-weight:bold;
        margin-bottom:12px;
    ">
        ⚠️ SYNTAX ERROR
    </div>
    """,
    unsafe_allow_html=True
)
        st.markdown(
    f"""
    <div style="
        background-color:#F0F2F6;
        color:#111111;
        padding:14px;
        border-radius:8px;
        margin-bottom:12px;
    ">
        🚨 Line: <strong>{error.lineno}</strong>
    </div>
    """,
    unsafe_allow_html=True
)
        st.markdown(
    f"""
    <div style="
        background-color:#F0F2F6;
        color:#111111;
        padding:14px;
        border-radius:8px;
        margin-bottom:12px;
    ">
        ⛔ Error: <strong>{error.msg}</strong>
    </div>
    """,
    unsafe_allow_html=True
)



        if error.text:  # if Python knows which line caused the error

            st.code(error.text.rstrip())  # shows the broken line


        if error.offset:  # if Python knows the position of the error 

                # puts ^ underneath the position where Python found the problem
            st.code(" " * (error.offset - 1) + "⬆ Problem found here")


        # turns the whole uploaded code into a list of lines
        lines = code.splitlines()


        # gets the line before the error line
        previous_number = error.lineno - 2


        # keep moving backward until you find a previous line that actualy has code on it
        while previous_number >= 0 and not lines[previous_number].strip():

            previous_number -= 1


        # if there is a previous non-empty line
        if previous_number >= 0:

            st.markdown(
            """
            <div style="
                background-color:#F0F2F6;
                color:#111111;
                padding:14px;
                border-radius:8px;
                margin-bottom:12px;
                font-weight:bold;
            ">
                📄 Previous:
                </div>
                """,
                unsafe_allow_html=True
            )

            # shows the previous non-empty line
            st.code(lines[previous_number])


        
        # checks Python's error message for a missing :
        if "expected ':'" in error.msg:

            broken_line = error.text.strip()

            first_word = broken_line.split()[0]

            colon_statements = [
                "if",
                "elif",
                "else",
                "for",
                "while",
                "def",
                "class",
                "try",
                "except",
                "finally"
            ]

            if first_word in colon_statements:

                st.info(
                    f"💡 Hint: Add a : at the end of the {first_word.upper()} statement."
                )

            else:

                st.info(
                    "💡 Hint: Add a : at the end of this line."
                )


        elif "was never closed" in error.msg:

            st.info("💡 Hint: Check your brackets or parentheses.")


        elif "unexpected indent" in error.msg:

            st.info("💡 Hint: Check the spaces at the beginning of the line.")


        elif "unterminated string literal" in error.msg:

            st.info("💡 Hint: Check if it's missing a quotation mark.")


        else:

            st.info("💡 Hint: Look carefully at the line Python mentioned.")
