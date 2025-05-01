
## 🧠 Question Answering System

A web-based NLP application that allows users to ask questions and get precise answers from a given context using a BERT model trained on the SQuAD dataset. Built with **Streamlit**, **PyTorch**, and **Transformers**, this system leverages the `bert-large-uncased-whole-word-masking-finetuned-squad` model to perform extractive question answering.

![QA UI](./b6e26163-6163-471b-ba68-f5bb59cbb137.png)

---

### 📌 Features

- 🔍 Extractive Question Answering using BERT
- 🧠 Powered by Hugging Face Transformers
- ⚡ Lightweight Streamlit web interface
- 💬 Real-time answer extraction from context

---

### 📁 Project Structure

```
├── app.py                   # Streamlit application
├── CNLP_Project_QA.ipynb    # Supporting notebook (optional for dev/testing)
├── requirements.txt         # Python dependencies
├── setup.sh                 # Shell script for environment setup and execution
└── README.md                # Project documentation
```

---

### ⚙️ Installation

#### Option 1: Manual Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/qa-system.git
   cd qa-system
   ```

2. **Create a virtual environment (optional)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

#### Option 2: Run with `setup.sh`

You can also use the provided shell script for a quick setup (Linux/macOS):

```bash
chmod +x setup.sh
./setup.sh
```

This script will:
- Set up a virtual environment
- Install all required packages
- Launch the Streamlit app

---

### 🚀 Technologies Used

- **Language Model**: BERT (fine-tuned on SQuAD)
- **Frameworks**: Streamlit, PyTorch, Hugging Face Transformers
- **Language**: Python

---

### 🖼 Example Use

> **Question**: Who developed BERT?  
> **Context**: BERT is a language representation model developed by Google that uses transformers...  
> **Answer**: *Google*

---

### 👨‍💻 Author

**Shashank Jaiswal**  
🔗 [Portfolio](https://portfolio-ndck.vercel.app/)  
📫 [LinkedIn](https://www.linkedin.com/in/shashank-jaiswal-b55429256)  

