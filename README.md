# 🚀 GenAI LinkedIn Post Generator

This project is a **GenAI-powered LinkedIn Post Generator** that helps users create high-quality LinkedIn posts based on their previous writing style.
---

## 📌 Overview
This tool analyzes past LinkedIn posts of a user and generates new posts by mimicking their writing style.

### 💡 Example Use Case

Let’s say **Mohan** is a LinkedIn influencer.

* He uploads his past posts
* The system extracts key insights like:

  * Topic
  * Language
  * Length
* Based on these, he can generate new posts that match his style

👉 This helps maintain **consistency, tone, and engagement**

---

## ⚙️ Technical Architecture

### 🔹 Stage 1: Data Processing

* Collect LinkedIn posts
* Extract metadata:

  * Topic (Tags)
  * Language (English / Hinglish)
  * Length (Short / Medium / Long)

---

### 🔹 Stage 2: Post Generation

* User selects:

  * Topic
  * Length
  * Language
* System uses:

  * Few-shot learning (past posts)
  * LLM (via API)
* Generates a new post matching writing style

---

## 🧠 Features

* ✨ AI-powered LinkedIn post generation
* 🎯 Topic-based customization
* 🌐 Multi-language support (English & Hinglish)
* 📏 Adjustable post length
* 🧩 Few-shot learning for style consistency
* ⚡ Fast and interactive UI using Streamlit

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* LLM API (Groq)
* JSON-based data processing

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/project-genai-post-generator.git
cd project-genai-post-generator
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure API Key

* Get your API key from: https://console.groq.com/keys
* Create a `.env` file in the root directory
* Add:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 4. Run the Application

```bash
streamlit run main.py
```

---

## 📸 Screenshots (Optional)

*Add your app screenshots here for better presentation*

---

## 🔥 Future Enhancements

* 📊 Engagement score prediction
* 🏷️ Auto hashtag generation
* 📈 Analytics dashboard
* 💾 Save & reuse generated posts
* 🌍 Multi-language expansion

---

## ⚠️ License

This project is licensed under the **MIT License**.

However:

* ❌ Commercial use is prohibited without permission
* ✅ Attribution is required

---

## 🙌 Acknowledgements

Inspired by real-world GenAI applications and content creation tools.

---

## 📬 Contact

If you have any questions or suggestions, feel free to reach out!

---

⭐ If you like this project, don’t forget to star the repo!
