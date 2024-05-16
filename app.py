import streamlit as st
import json
from PIL import Image, ImageOps

# 페이지 기본 설정
st.set_page_config(page_title='PDF eBook Store', page_icon=':books:', layout='wide')

# JSON 데이터 파일 로드
with open('data/books.json', 'r') as file:
    books = json.load(file)

# 커버 이미지 크기 설정
COVER_IMAGE_SIZE = (300, 400)

# 기본 이미지 로드
DEFAULT_IMAGE = Image.new('RGB', COVER_IMAGE_SIZE, color=(200, 200, 200))

# 페이지 타이틀과 설명
st.markdown(
    """
    <style>
    .main-title {
        font-size: 3em;
        text-align: center;
        color: #4A90E2;
    }
    .sub-title {
        font-size: 1.2em;
        text-align: center;
        color: #4A90E2;
        margin-bottom: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<h1 class="main-title">PDF eBook Store</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-title">High-quality eBooks for Learning and Mastery</h2>', unsafe_allow_html=True)

# 전자책을 3열 레이아웃으로 배치
cols_per_row = 3
rows = [books[i:i + cols_per_row] for i in range(0, len(books), cols_per_row)]

for row in rows:
    cols = st.columns(cols_per_row)
    for col, book in zip(cols, row):
        with col:
            # 전자책 커버 이미지 표시
            try:
                image = Image.open(book['cover_image']).resize(COVER_IMAGE_SIZE)
            except FileNotFoundError:
                image = DEFAULT_IMAGE
            st.image(image, use_column_width=True)

            # 전자책 제목, 저자, 설명, 가격 및 구매 버튼 표시
            st.markdown(
                f"""
                <h3 style='text-align: center; color: #4A90E2;'>{book['title']}</h3>
                <h4 style='text-align: center; color: #4A90E2;'>by {book['author']}</h4>
                <p style='text-align: center;'>{book['description']}</p>
                <p style='text-align: center; font-weight: bold;'>Price: ${book['price']}</p>
                """,
                unsafe_allow_html=True
            )
            if st.button(f"Buy {book['title']}", key=book['title']):
                st.write(f"Please go to [this link]({book['purchase_link']}) to purchase.")
            st.markdown('---')

# 사이드바 업데이트 및 정보
st.sidebar.title('Updates & Information')
st.sidebar.info('''
- **New eBooks:** Check out the latest additions to our catalog!
- **Upcoming Features:** We're working on integrating new payment systems.
- **Feedback:** Let us know what you think and how we can improve.
''')