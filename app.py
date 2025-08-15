import streamlit as st
from dog_api import get_all_breeds, get_random_image, get_image_by_breed

st.title("犬の画像アプリ")

breeds = get_all_breeds()
selected_breed = st.selectbox("犬種を選んでください", breeds)

col1, col2 = st.columns(2)

with col1:
    if st.button("犬種の画像を表示"):
        img = get_image_by_breed(selected_breed)
        if img:
            st.image(img, caption=f"{selected_breed}の画像")
        else:
            st.error("画像が取得できませんでした。")

with col2:
    if st.button("ランダムな犬の画像を表示"):
        img = get_random_image()
        if img:
            st.image(img, caption="ランダム犬画像")
        else:
            st.error("画像が取得できませんでした。")
