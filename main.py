import streamlit as st
import pandas as pd
import random

st.title("6학년 반편성 웹앱")
st.write("5학년 학생 명단을 입력하고 성별 비율을 유지하여 6학년 반편성을 자동으로 수행합니다.")

# 학생 데이터 입력
st.subheader("5학년 학생 명단 입력")
num_classes = st.number_input("5학년 학급 수", min_value=1, value=7)
class_data = {}

for i in range(num_classes):
    class_name = f"5학년 {i+1}반"
    st.subheader(class_name)
    names = st.text_area(f"{class_name} 학생 이름 (줄바꿈으로 구분)")
    genders = st.text_area(f"{class_name} 학생 성별 (줄바꿈으로 구분, M 또는 F)")

    name_list = names.splitlines()
    gender_list = genders.splitlines()

    if len(name_list) == len(gender_list):
        class_data[class_name] = pd.DataFrame({"이름": name_list, "성별": gender_list})
    else:
        st.error(f"{class_name} 이름과 성별 수가 일치하지 않습니다.")

# 반편성 실행
if st.button("6학년 반편성 실행"):
    all_students = pd.concat(class_data.values(), ignore_index=True)

    males = all_students[all_students["성별"] == "M"].sample(frac=1).reset_index(drop=True)
    females = all_students[all_students["성별"] == "F"].sample(frac=1).reset_index(drop=True)

    num_6th_classes = num_classes
    class_size = len(all_students) // num_6th_classes

    assigned_classes = {f"6학년 {i+1}반": [] for i in range(num_6th_classes)}

    for i in range(class_size):
        for class_name in assigned_classes.keys():
            if len(males) > 0:
                assigned_classes[class_name].append(males.iloc[0].tolist())
                males = males.iloc[1:]
            if len(females) > 0:
                assigned_classes[class_name].append(females.iloc[0].tolist())
                females = females.iloc[1:]

    st.subheader("6학년 반편성 결과")
    for class_name, students in assigned_classes.items():
        st.write(f"### {class_name}")
        st.write(pd.DataFrame(students, columns=["이름", "성별"]))
