import streamlit as st
import feedparser

st.title("🎧 Entertainment and health app")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Health check ❤️", "📰 News", " Gold price", "Step advice", "Water Tracker"])

with tab1:
    st.header("Kiểm tra sức khỏe của bạn")
    can_nang = st.number_input("Nhập cân nặng của bạn  (kg)", min_value=10.0, max_value=200.0, value=60.0, step=0.1)
    chieu_cao = st.number_input("Nhập chiều cao của bạn (m): ", min_value=1.0, max_value=2.5, value=1.7, step=0.01)
    if st.button("Tinh BMI"):
        bmi = can_nang/(chieu_cao ** 2)
        st.success(f"chỉ số bmi của bạn là: {bmi: .2f}")

        if bmi < 18.5:
            st.warning("bạn đang thiếu cân, nên ăn uống đầy đủ, ngủ đủ giờ(8h/ngày), đồ ăn nhiều dinh dưỡng hơn")
        elif 18.5 < bmi < 25:
            st.info("bạn có cân nặng bình thường. Hãy tiếp tục duy trì lối sống lành mạnh.")
        elif 25 <= bmi < 30:
            st.warning("Bạn đang thừa cân, nên cân đối chế độ ăn uống và tập thể dục. ")
        else:
            st.error("Bạn đang béo phì, nên gặp chuyên gia dinh dưỡng hoặc bác sĩ để được tư vấn ")

with tab2:
    st.header("The latest news from VnExpress")
    feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
    for entry in feed.entries[:10]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)

with tab3:
    st.header("💰 Cập nhật giá vàng từ Vietnamnet")

    feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
    gold_news = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]

    if gold_news:
        for entry in gold_news[:5]:  # Hiện 5 bài gần nhất
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
    else:
        st.warning("Không tìm thấy bản tin giá vàng gần đây.")

with tab4:
    st.header("Step advice by age")
    Age = st.number_input("Your age:", min_value=1, max_value=100, value=12, step=1)
    if st.button("Advice"):
        st.success(f"Your age: {Age: .2f}")

        if Age < 18:
            st.info("You should walk about 12000 to 15000 steps per day")

        if Age > 17 and Age < 39:
            st.info("You should walk about 8000 to 10000 steps per day")

with tab5:
    st.header("Water Tracker by Age")
    age = st.number_input("Your age:", min_value=1, max_value=100, value=12, step=1)
    gender = st.number_input("Your gender(1 = Male, 2 = Female):", min_value=1, max_value=2, value=2, step=1)
    if st.button("Water reccomendations"):
        st.sucess(f"Your age: {Age: .2f}")

        if age < 4:
            st.info("You should drink 1.3L per day")

        if age < 9:
            st.info("You should drink 1.7L per day")

        if age < 14:
            st.info("You should drink 2.1 - 2.4L per day")

        if age < 19 and gender == 1:
            st.info("You should drink 3.3L per day")
        
        if age < 19 and gender == 2:
            st.info("You should drink 2.3L per day")
        
        if age < 51 and gender == 2:
            st.info("You should drink 2.7L per day")

        if age < 51 and gender == 1:
            st.info("You should drink 3.7L per day")

        if age > 50:
            st.info("You should drink 2.5 - 3.0L per day depending on your exercising level.")
