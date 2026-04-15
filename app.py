import streamlit as st
from api_calling import notegenerator
from api_calling import text_to_speech
from api_calling import Quiz_generator
from PIL import Image
from gtts import gTTS
import io
#Title
st.title("Note Summary and Quiz Generator")
st.text("upload upto 3 images to generate Note Summary and Quiz")
st.divider()

#sidebar
with st.sidebar:
    st.header("Controls")
    images=st.file_uploader("upload Images:",accept_multiple_files=True,type=['png','jpg','jpeg'])
    if len(images)>5:
        st.error("Picture over The Five")
    else:
        st.subheader("Upload:")
        if images:
            cols=st.columns(len(images))
            for i ,pre_pic in enumerate(images):
                with cols[i]:
                    st.image(pre_pic)
        
        selected=st.selectbox("Enter the Difficulity:",options=['Easy','Medium','Hard'],index=None)
        if selected:
            st.markdown(f'You selected **{selected}** as difficulity of your quiz')
       
        button=st.button("Click The Button to initiate AI",type="primary")


if button:
    if not images:
        st.error("You must upload 1 picture")
    if not selected:
        st.error("you must be select the difficulity")
    if images and selected:
        #note
        with st.container(border=True):
            st.subheader("Your Note")
            with st.spinner("AI is writting notes for you"):
                images=[Image.open(i) for i in images]
                note=notegenerator(images)

                #clearing the markdown

                note=note.replace("#",'')
                note=note.replace("*",'')
                note=note.replace("-",'')
                note=note.replace("'",'')
                note=note=note.replace("",'')
                st.markdown(note)

        #Audio transcript
        with st.container(border=True):
            st.subheader("Audio transcription")
            with st.spinner("AI is generating transcription for you"):
                st.audio(text_to_speech(note))
            

        #Quiz
        with st.container(border=True):
            st.subheader(f"Quiz({selected}) Diffculity")
            with st.spinner("AI is generating quiz for you"):
                quiz=Quiz_generator(images,selected)
                st.markdown(quiz)
                pass


