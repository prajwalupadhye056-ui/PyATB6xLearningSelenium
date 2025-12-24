🚀 Selenium Web Automation Framework (Python – Selenium 4.x)
📌 Project Overview
This repository contains a Python-based Selenium 4.x Web Automation Framework designed to automate modern web applications.
The project demonstrates industry-standard automation practices, including locator strategies, waits, actions, window handling, iframe handling, Selenium Grid, and reporting using PyTest and Allure.
The framework is suitable for:


Learning Selenium automation from basics to advanced


Real-world UI automation projects


Interview preparation & portfolio showcase



🧑‍💻 Author
Author: Prajwal
Role: QA / Automation Engineer
Tech Stack: Python | Selenium | PyTest | Allure | GitHub

🛠️ Tech Stack & Tools
ToolPurposePython 3.xProgramming LanguageSelenium 4.xWeb AutomationPyTestTest Execution FrameworkAllure ReportTest ReportingChrome / FirefoxBrowser AutomationSelectorsHubLocator IdentificationSelenium GridParallel & Cross-Browser TestingGit & GitHubVersion Control

📂 Project Structure
selenium-web-automation/
│
├── tests/
│   ├── test_login.py
│   ├── test_waits.py
│   ├── test_actions.py
│   ├── test_windows_iframes.py
│
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│
├── utils/
│   ├── driver_factory.py
│   ├── logger.py
│   ├── waits.py
│
├── reports/
│   └── allure-results/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md


⚙️ Key Automation Concepts Covered
✅ Selenium Fundamentals


WebDriver Architecture (Selenium 4 – W3C)


Browser Drivers (Chrome, Firefox)


WebDriver Hierarchy & API


✅ Locator Strategies


ID, Name, Class Name


CSS Selectors (Advanced)


XPath (Relative, Functions, Axes)


Best Locator Practices (Performance-oriented)


✅ Synchronization


Implicit Wait


Explicit Wait (Expected Conditions)


Fluent Wait


Best practices (No time.sleep() misuse)


✅ Advanced Selenium Features


ActionChains (Keyboard & Mouse events)


Handling Alerts (Accept, Dismiss, Send Keys)


Handling Windows & Multiple Tabs


Handling Iframes


File Upload


Web Tables (Static & Dynamic)


✅ Framework Capabilities


PyTest fixtures (conftest.py)


Logging support


Test categorization using markers


Parallel execution (Grid ready)



🌐 Selenium Grid & Cloud Execution


Local Selenium Grid (Standalone / Distributed)


Docker-based Selenium Grid


Cloud execution using BrowserStack



🧪 Sample Test Scenarios Automated


Login with valid & invalid credentials


Error message validation


Dynamic element synchronization


Dropdown handling (Static & Dynamic)


Heatmap interaction using Actions + iFrame


Web table data extraction


Window & tab switching



▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/selenium-web-automation.git
cd selenium-web-automation

2️⃣ Create Virtual Environment
python -m venv venv

Activate:


Windows


venv\Scripts\activate



Mac/Linux


source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Tests
pytest -v

5️⃣ Generate Allure Report
pytest --alluredir=reports/allure-results
allure serve reports/allure-results


📊 Reporting


Allure HTML reports with:


Step-wise execution


Screenshots (if enabled)


Test status & history





📈 Best Practices Followed


Page Object Model (POM)


Reusable utilities


Clean locator strategy


Explicit waits over static waits


Scalable & maintainable structure



📌 Use Cases
✔ Learning Selenium Automation
✔ Interview Demonstration
✔ Framework Reference
✔ Portfolio Project

📞 Contact
Author: Prajwal
