# GuardWAF 🛡️

**GuardWAF** is an advanced, local Web Application Firewall (WAF) for web applications, built with Python.  
It detects threats such as SQLi, XSS, LFI, RCE, and bots, and classifies HTTP requests using heuristics and machine learning (ML).

## 🚀 Features
- 🔍 Detection of SQLi, XSS, LFI, RCE (regex + scoring)
- 🧠 Heuristic analysis of HTTP request content
- 🤖 Bot detection based on User-Agent heuristics
- 🧪 Machine Learning classification (Naive Bayes)
- 📊 Export results to JSON, CSV, and Excel
- 📁 Supports Apache and Nginx logs (automatic format detection)
- 🛠 REST API with JWT authentication

## 🔧 Installation

```bash
git clone https://github.com/Hubert-a-bite/guardwaf.git
cd guardwaf
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🧠 Train the Machine Learning model

```bash
python ml/train.py
```

## 📁 Usage – log file analysis

```bash
python waf.py
```

📦 Results will be saved in the `logs/` directory:  
- `waf_alerts.log`  
- `summary.json`, `summary.csv`, `summary.xlsx`

## 🌐 REST API (optional)

```bash
uvicorn api.rest_api:app --port 5000
```

### 🔐 Get a token
```bash
curl -X POST http://localhost:5000/api/token -H "Content-Type: application/json" -d '{"user":"admin"}'
```

### 🔎 Scan a request
```bash
curl -X POST http://localhost:5000/api/scan \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"query": "<script>alert(1)</script>", "user_agent": "curl/7.88.1"}'
```

## 📝 License

MIT License © 2025 Hubert
