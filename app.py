from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq_questions = [
    "What is admission process?",
    "What are college timings?",
    "Where is the college located?",
    "What courses are available?",
    "How can I contact the college?"
]

faq_answers = [
    "You can apply online through the college website.",
    "College timings are 10 AM to 5 PM.",
    "The college is located in Sangli, Maharashtra.",
    "The college offers Engineering, MBA and Diploma courses.",
    "You can contact the college through phone or email."
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(faq_questions)

print("===== FAQ Chatbot =====")

while True:
    query = input("\nAsk a Question (type exit to quit): ")

    if query.lower() == "exit":
        break

    query_vector = vectorizer.transform([query])
    similarity = cosine_similarity(query_vector, X)
    index = similarity.argmax()

    print("Bot:", faq_answers[index])
