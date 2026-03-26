# 🌐 Public IP Lookup Tool 

**Team Project: REST API & Git Collaboration** 

  

## 👥 The Development Team 

* **Scrum Leader:** Almazora - Repo Management & Integration 

* **Developer A:** Rondilla - API Logic & Service Layer 

* **Developer B:** Lapaz - UI & Main Application Logic 

* **QA Engineer:** Delgado - Unit Testing & Validation 

* **Recorder:** Rubis - Documentation & Presentation 

  

## 🚀 Project Overview 

This Python application fetches real-time public network data (IP, City, ISP) using the `ipapi.co` REST API. It demonstrates modular programming, error handling, and collaborative version control. 

 

## 🛠️ Installation & Setup 

#### Clone the repository first: 

 

    git clone https://github.com/rain-zk/public_ip_app.git 

 

#### Option A: Using uv (Recommended/Fastest) 

 

If you have `uv` installed, simply run the command below. It will automatically create a virtual environment and sync all dependencies from `uv.lock`. 

 

    uv run python -m src.main 

 

#### Option B: Standard Python (Pip) 

1. Create and activate a virtual environment: 

    * **Windows:** `python -m venv venv` then `.\venv\Scripts\activate` 

    * **Mac/Linux:** `python3 -m venv venv` then `source venv/bin/activate` 

2. Install dependencies: 

 

    `python -m pip install -r requirements.txt` 

 

## 💻 How to Run 

To start the application, run the following command from the root directory: 

* **Modern (uv):** `uv run python -m src.main` 

* **Standard:** `python -m src.main` 

 

## 🧪 Testing 

To run the automated unit tests: 

* **Modern (uv):** `uv run python -m unittest discover tests` 

* **Standard:** `python -m unittest tests/test_ip.py` 
