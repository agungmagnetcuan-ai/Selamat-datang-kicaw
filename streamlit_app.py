import streamlit as st

st.title("🎈 My new appp agung")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


number = st.number_input(
    "masukan nomor panjang" value=None, placeholder="Type a number..."
)
st.write("The current number is ", number)



