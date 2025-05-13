import streamlit as st

# 웹앱 제목과 설명
st.set_page_config(page_title='🎵 우쿨렐레 코드 가이드', page_icon='🎶')
st.title('🎶 우쿨렐레 코드 가이드')
st.write('👉 원하는 코드를 선택하면 해당 코드의 코드표를 바로 확인할 수 있어요! 🎸')

# 코드 선택 섹션
chords = ['C', 'G7', 'Am', 'F', 'D', 'E', 'A', 'Dm', 'Em', 'A7']
selected_chord = st.selectbox('🎸 코드 선택:', chords)

# 코드 다이어그램 표시
chord_images = {
    'C': 'https://upload.wikimedia.org/wikipedia/commons/4/4d/C_Ukulele_Chord.png',
    'G7': 'https://upload.wikimedia.org/wikipedia/commons/3/3d/G7_Ukulele_Chord.png',
    'Am': 'https://upload.wikimedia.org/wikipedia/commons/e/e0/Am_Ukulele_Chord.png',
    'F': 'https://upload.wikimedia.org/wikipedia/commons/6/64/F_Ukulele_Chord.png',
}

if selected_chord in chord_images:
    st.subheader(f'🎵 {selected_chord} 코드')
    st.image(chord_images[selected_chord])

st.write('✨ 즐겁게 연습하세요! 😊')
