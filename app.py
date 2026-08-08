import streamlit as st
import joblib

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Nepali News Classification",
    page_icon="📰",
    layout="wide"
)

# -----------------------------------
# Load Model
# -----------------------------------
@st.cache_resource
def load_models():
    model = joblib.load("models/linear_svm.pkl")
    tfidf = joblib.load("models/tfidf_vectorizer.pkl")
    label_encoder = joblib.load("models/label_encoder.pkl")
    return model, tfidf, label_encoder

model, tfidf, label_encoder = load_models()

# -----------------------------------
# Prediction Function
# -----------------------------------
def predict_news(text):
    vector = tfidf.transform([text])
    prediction = model.predict(vector)[0]
    category = label_encoder.inverse_transform([prediction])[0]
    return category

# -----------------------------------
# Sidebar
# -----------------------------------
st.sidebar.title("📊 Model Information")

st.sidebar.success("Linear SVM")

st.sidebar.write("### Dataset")
st.sidebar.write("Hugging Face Nepali News Dataset")

st.sidebar.write("### Vectorizer")
st.sidebar.write("TF-IDF")

st.sidebar.write("### Accuracy")
st.sidebar.write("74.41 %")

st.sidebar.write("### Training Samples")
st.sidebar.write("96,000")

st.sidebar.write("### Categories")

categories = [
    "Business",
    "Crime",
    "Economy",
    "Education",
    "Entertainment",
    "Global",
    "Health",
    "National",
    "Politics",
    "Science & Technology",
    "Society",
    "Sports"
]

for category in categories:
    st.sidebar.write("•", category)

# -----------------------------------
# Main Page
# -----------------------------------
st.title("📰 Nepali News Classification")

st.markdown("""
This application classifies Nepali news articles into **12 different categories**
using a **TF-IDF Vectorizer** and a **Linear SVM** classifier.

Paste a Nepali news article below and click **Predict Category**.
""")

# -----------------------------------
# Text Input
# -----------------------------------
news = st.text_area(
    "📄 Enter Nepali News Article",
    height=300,
    placeholder="Paste your Nepali news article here..."
)

# -----------------------------------
# Statistics
# -----------------------------------
if news.strip():

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Word Count", len(news.split()))

    with col2:
        st.metric("Character Count", len(news))

# -----------------------------------
# Prediction
# -----------------------------------
if st.button("🚀 Predict Category"):

    if news.strip() == "":
        st.warning("Please enter a Nepali news article.")
    else:

        category = predict_news(news)

        st.success("Prediction Completed")

        st.markdown("---")

        st.subheader("📌 Predicted Category")

        st.info(category.upper())

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")

st.caption(
    "Developed using Scikit-learn | Linear SVM | TF-IDF | Streamlit"
)