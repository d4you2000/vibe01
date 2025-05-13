import streamlit as st
import pandas as pd
import random

st.title("초등학교 6학년 반편성 웹앱")

# 학생 명단 입력
st.header("5학년 학생 명단 입력")
uploaded_file = st.file_uploader("학생 명단 CSV 파일을 업로드하세요 (이름, 성별)")

if uploaded_file is not None:
    students_df = pd.read_csv(uploaded_file)
    st.write("업로드된 학생 명단:")
    st.dataframe(students_df)

    # 성별 비율 확인
    male_students = students_df[students_df['성별'] == '남']
    female_students = students_df[students_df['성별'] == '여']

    st.write(f"남학생: {len(male_students)}명, 여학생: {len(female_students)}명")

    # 반 수 입력
    num_classes = st.number_input("6학년 반 수 입력", min_value=1, max_value=10, value=6)

    if st.button("반편성 실행"):
        random.shuffle(male_students.values.tolist())
        random.shuffle(female_students.values.tolist())

        # 반편성 로직
        class_lists = [[] for _ in range(num_classes)]

        for i, student in enumerate(male_students.values.tolist() + female_students.values.tolist()):
            class_lists[i % num_classes].append(student)

        # 결과 출력
        st.header("6학년 반편성 결과")
        for i, class_list in enumerate(class_lists, start=1):
            st.subheader(f"6-{i}반")
            class_df = pd.DataFrame(class_list, columns=["이름", "성별"])
            st.dataframe(class_df)
