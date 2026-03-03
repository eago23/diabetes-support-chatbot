# 🩺 Intelligent Diabetes Support Chatbot

> A hybrid AI system combining neural networks with A* search for intelligent diabetes risk assessment and personalized health guidance.

---

## ⚙️ Installation

Install the required dependencies:
```bash
pip install pandas numpy keras scikit-learn matplotlib
```

---

## ▶️ Running the Project
```bash
python main.py
```

> Enter patient data when prompted (8 features), then interact with the chatbot. Type `exit` to quit.

---

## 🧠 AI Approach Overview

### 1. Neural Networks
| Model | Accuracy | Dataset |
|-------|----------|---------|
| Diabetes Risk Predictor | 78.57% | 768 patients |
| Intent Classifier | 70% | 245 examples, 8 intents |

### 2. A* Search
- **Purpose:** Symbolic planning for glucose management
- **State:** `(glucose_level, risk_level)`
- **Goal:** `glucose = "normal"`
- **Output:** Optimal action sequences to guide patients toward healthy glucose levels

### 3. Scenario Simulator
- **"What-if" analysis** powered by neural network re-prediction
- Simulates the impact of lifestyle changes:
  - `walk_daily`
  - `healthy_diet`
  - and more...

### 4. Adaptive Chatbot
- ✅ Risk-based personalization tailored to each patient
- ✅ Intent-driven responses
- ✅ Context-aware health advice

---

## 🔬 Hybrid Approach

This system bridges the gap between rule-based AI and modern deep learning by combining:

| Component | Type | Purpose |
|-----------|------|---------|
| A* Search | Symbolic Reasoning | Explainable action planning |
| Neural Networks | Statistical Learning | Adaptive risk prediction |

Together, they deliver **explainable, adaptive, and personalized** diabetes decision support.