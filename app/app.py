if __name__ == "__main__":
    import os
    import streamlit as st
    from langchain.chat_models import init_chat_model
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain
    import torch

    torch.classes.__path__ = []  # add this line to get rid of error messages.
    os.environ.get("ANTHROPIC_API_KEY")

    # Streamlit app title
    st.title("Email Crafter")

    chat_model = init_chat_model(
        "claude-3-7-sonnet-20250219",
        model_provider="anthropic",
        configurable_fields="any",
        max_tokens=1024,
        temperature=0.5,
    )

    prompt_template = """ Please revise the following message to improve grammar and clarity. Make the tone friendly, polite, and professional, while keeping it concise and straight to the point. The message will be used as a {use_case}.

        Focus on:
        - Correcting grammar and punctuation.
        - Improving clarity and flow.
        - Maintaining a warm, courteous tone.
        - Keeping the message brief and direct.

        Original message: 
        
        {message}

    """

    prompt = PromptTemplate(
        template=prompt_template, input_variables=["use_case", "message"]
    )

    with st.form("document"):
        message = st.text_area("paste your message draft here: ")
        st.write(f"You wrote {len(message)} characters.")
        use_case = st.text_input(
            "What is the use case? e.g. work email, slack message, etc: "
        )
        submit = st.form_submit_button("Submit Document")

    if submit:
        input_ = {"use_case": use_case, "message": message}
        llm_chain = LLMChain(prompt=prompt, llm=chat_model)
        response = llm_chain.invoke(input_)
        st.write(response["text"])
