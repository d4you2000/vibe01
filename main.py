import streamlit as st
import pandas as pd
import random

st.title("6학년 반편성 웹앱")
st.write("엑셀 파일을 업로드하여 5학년 학생 명단을 불러오고 성별 비율을 유지하여 6학년 반편성을 자동으로 수행합니다.")

# 엑셀 파일 업로드
uploaded_file = st.file_uploader("엑셀 파일 업로드", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        # 기본적으로 openpyxl 설치 확인하지 않고 pandas 기본 엔진 사용
        df = pd.read_excel(uploaded_file)

        if "이름" in df.columns and "성별" in df.columns:
            st.write("5학년 학생 명단:")
            st.dataframe(df)

            # 반편성 실행
            if st.button("6학년 반편성 실행"):
                males = df[df["성별"] == "M"].sample(frac=1).reset_index(drop=True)
                females = df[df["성별"] == "F"].sample(frac=1).reset_index(drop=True)

                num_6th_classes = st.number_input("6학년 학급 수", min_value=1, value=7)
                class_size = len(df) // num_6th_classes

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
        else:
            st.error("엑셀 파일에 '이름'과 '성별' 열이 필요합니다.")
    except Exception as e:
        st.error(f"엑셀 파일을 읽는 중 오류가 발생했습니다: {str(e)}")
