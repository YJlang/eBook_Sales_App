import streamlit as st
import json
from PIL import Image

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
    .book-title {
        text-align: center;
        color: #4A90E2;
    }
    .book-author {
        text-align: center;
        color: #4A90E2;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="main-title">PDF eBook Store</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-title">High-quality eBooks for Learning and Mastery</h2>', unsafe_allow_html=True)

# 탭 생성
tabs = [book['title'] for book in books]
tabs.insert(0, "All Books")
selected_tab = st.selectbox("Choose a book", tabs)

# "All Books" 탭 처리
if selected_tab == "All Books":
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
                    <h3 class='book-title'>{book['title']}</h3>
                    <h4 class='book-author'>by {book['author']}</h4>
                    <p style='text-align: center;'>{book['description']}</p>
                    <p style='text-align: center; font-weight: bold;'>Price: ${book['price']}</p>
                    """,
                    unsafe_allow_html=True
                )
                if st.button(f"Buy {book['title']}", key=book['title']):
                    st.write(f"Please go to [this link]({book['purchase_link']}) to purchase.")
                st.markdown('---')

# 개별 전자책 탭 처리
else:
    book = next((book for book in books if book['title'] == selected_tab), None)
    if book:
        col1, col2 = st.columns([1, 2])

        with col1:
            try:
                image = Image.open(book['cover_image']).resize(COVER_IMAGE_SIZE)
            except FileNotFoundError:
                image = DEFAULT_IMAGE
            st.image(image, use_column_width=True)

        with col2:
            st.markdown(
                f"""
                <h2 class='book-title'>{book['title']}</h2>
                <h4 class='book-author'>by {book['author']}</h4>
                <p>{book['description']}</p>
                <p style='font-weight
                <p style='font-weight: bold;'>Price: ${book['price']}</p>
                """,
                unsafe_allow_html=True
            )
            if st.button(f"Buy {book['title']}", key=f"buy-{book['title']}"):
                st.write(f"Please go to [this link]({book['purchase_link']}) to purchase.")

        st.markdown('---')

        st.subheader("More Information")
        st.write(
            f"""
            - **Title:** {book['title']}
            - **Author:** {book['author']}
            - **Price:** ${book['price']}
            - **Purchase Link:** [Click Here]({book['purchase_link']})
            """
        )

        st.subheader("Preview")
        st.info("Download a sample chapter or preview the first few pages.")
        st.markdown(
            f"[Download Sample]({book['file']})", unsafe_allow_html=True
        )

# 사이드바 업데이트 및 정보
st.sidebar.title('Updates & Information')
st.sidebar.info('''
- **New eBooks:** Check out the latest additions to our catalog!
- **Upcoming Features:** We're working on integrating new payment systems.
- **Feedback:** Let us know what you think and how we can improve.
''')

st.sidebar.markdown('---')

st.sidebar.title('Categories')
categories = set(book['author'] for book in books)
st.sidebar.write("\n".join(f"- {category}" for category in categories))

st.sidebar.markdown('---')

st.sidebar.title('Contact Us')
st.sidebar.info(
    '''
    - Email: sean111400@naver.com
    - Phone: +82 (10) 4604-6774
    - Address: S.K.U Media Software Engineering
    '''
)