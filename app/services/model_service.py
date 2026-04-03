import joblib

# Load models
model = joblib.load("career_model.pkl")
tfidf = joblib.load("tfidf.pkl")
le = joblib.load("label_encoder.pkl")

def predict_top3(skills_text: str):
    vec = tfidf.transform([skills_text])
    probs = model.predict_proba(vec)[0]

    top3_idx = probs.argsort()[-3:][::-1]

    results = []
    for idx in top3_idx:
        career = le.inverse_transform([idx])[0]
        confidence = float(probs[idx])

        results.append({
            "career": career,
            "confidence": round(confidence * 100, 2)
        })

    return results