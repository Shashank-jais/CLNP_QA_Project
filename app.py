import streamlit as st
import torch
import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer

model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

# Your QA function
def question_answer(question, text):

    input_ids = tokenizer.encode(question, text)

    tokens = tokenizer.convert_ids_to_tokens(input_ids)

    sep_idx = input_ids.index(tokenizer.sep_token_id)

    num_seg_a = sep_idx + 1

    num_seg_b = len(input_ids) - num_seg_a

    segment_ids = [0] * num_seg_a + [1] * num_seg_b

    assert len(segment_ids) == len(input_ids)

    output = model(torch.tensor([input_ids]), token_type_ids=torch.tensor([segment_ids]))

    answer_start = torch.argmax(output.start_logits)
    answer_end = torch.argmax(output.end_logits)

    if answer_end >= answer_start:
        answer = tokens[answer_start]
        for i in range(answer_start + 1, answer_end + 1):
            if tokens[i][:2] == "##":
                answer += tokens[i][2:]
            else:
                answer += " " + tokens[i]

    # Handle case where no answer is found
    if answer.startswith("[CLS]"):
        answer = "Unable to find the answer to your question."

    return answer.capitalize()

# Streamlit UI
st.set_page_config(layout="wide")
st.title("Question Answering System")

col1, col2 = st.columns(2)
with col1:
    question = st.text_input("Your Question:", placeholder="Ask me anything...")
with col2:
    text = st.text_area("Context Text:", height=150, placeholder="Paste the text you want to ask about...")

if st.button("Get Answer", type="primary"):
    if question and text:
        with st.spinner("Analyzing..."):
            answer = question_answer(question, text)
            st.success("Answer:")
            st.markdown(f"**{answer}**")
    else:
        st.warning("Please enter both a question and context text")
