# 🚀 Project Overview

This repository contains a collection of tasks related to **Natural Language Processing (NLP)**, **Deep Learning (DL)**, **Transformers**, **LangChain**, **Hugging Face**, **Ollama**, and **API development**.

The goal of this project is to explore and implement different AI concepts and tools through practical tasks.

---

## 📁 Project Structure

```
project/
│── tasks/
│   │── task1
│   │── task2
│   │── task3
│   │── task4
│   │── task5
│   │── task6
│   │── task7
│   │── task9
│
│── outputs/
│   │── task7.png
│   │── task9 chat.png
│   │── task9 output1.png
│   │── task9 summarize.png
│
│── sheet1.csv
│── sheet2.csv
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ Steps to Run the Project

1. Clone the repository:

```bash
git clone <your-repo-link>
cd project
```

2. Create virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run tasks:

Navigate to the `tasks` folder and run any task file:

```bash
cd tasks
python task1.py
```

---

## 📦 Dependencies

* Python
* NumPy
* OpenCV
* Transformers
* LangChain
* Hugging Face Libraries
* FastAPI / Flask (for API tasks)
* Ollama (for local LLM execution)

> Note: Dependencies may vary slightly depending on the task.

---

🧠 Description of Each Task

🔹 NLP

Basic Natural Language Processing tasks such as:

Text preprocessing

Tokenization

Feature extraction

🔹 DL (Deep Learning)

Implementation of deep learning models for:

Classification

Prediction tasks using datasets (sheet1.csv, sheet2.csv)

🔹 Transformers

Usage of transformer-based models for advanced NLP tasks.

🔹 LangChain

Building conversational pipelines and LLM-based workflows.

🔹 Hugging Face

Using pretrained models and pipelines from Hugging Face.

🔹 Ollama

Running and experimenting with local LLMs.

🔹 API

Creating APIs to serve models using FastAPI or Flask.

🖼️ Outputs

The outputs/ folder contains result images generated from different tasks.

🧪 Example Inputs and Outputs
Example 1: NLP Task

Input:

"This is a sample sentence."

Output:

["This", "is", "a", "sample", "sentence"]
Example 2: Transformer Task

Input:

"Translate English to French: Hello"

Output:

"Bonjour"
Example 3: API Task

Request:

POST /predict
{
  "text": "I love AI"
}

Response:

{
  "sentiment": "positive"
}

📌 Notes

Tasks are organized inside the tasks/ folder.

Output images are stored in the outputs/ folder.

CSV files (sheet1.csv, sheet2.csv) are used for model training/testing.

Each task demonstrates a different concept in AI/ML.
