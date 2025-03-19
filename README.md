# Smart Finance Manager

## 📌 Project Overview

Smart Finance Manager is an AI-powered financial management tool designed to help users track expenses, manage budgets, and gain insights using AI-based recommendations. It integrates Flask for backend operations and utilizes Bootstrap and JavaScript for a seamless frontend experience. The project also incorporates the Gemini API for AI-driven assistance.

## 🚀 Features

- **Expense Tracking**: Users can log and categorize their daily expenses.
- **Budget Management**: Set budgets and receive alerts for overspending.
- **AI-Powered Assistance**: ChatGPT API for personalized financial advice.
- **User Authentication**: Secure login and registration system.
- **Data Visualization**: Graphs and charts for financial insights.
- **Reports & Analytics**: Monthly and yearly financial reports.

## 🛠️ Tech Stack

- **Frontend**: Bootstrap, JavaScript, HTML, CSS, Chart.js (for graph visualization)

- **Frontend**: Bootstrap, JavaScript, HTML, CSS

- **Backend**: Flask (Python)

- **Database**: MySQL

- **AI Integration**: Gemini API

## 📦 Dependencies

- Flask
- Flask SQLAlchemy
- Flask-WTF
- Flask-Login
- MySQL Connector
- Gemini API (for AI integration)

## 🔧 Installation & Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/vyankatesh-pandit/smart-finance-manager.git
   cd smart-finance-manager
   ```
2. **Create & Activate Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate***
   ```
3. **Set Up Database**
   - Create a MySQL database.
   - Update `config.py` with your database credentials.
   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'root'
   app.config['MYSQL_PASSWORD'] = 'DB_password'
   app.config['MYSQL_DB'] = 'Db_name'
   ```

app.config['MYSQL\_USER'] = 'root'
app.config['MYSQL\_PASSWORD'] = '123456'\
app.config['MYSQL\_DB'] = 'SFM'

```
5. **Run the Application**
python app.py
```

Access the app at `http://127.0.0.1:5000`

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

## 📧 Contact

- **Name**: Vyankatesh Pandit
- **Email**: [vyankateshpandit1511@gmail.com](mailto\:vyankateshpandit1511@gmail.com)
- **Portfolio**: [vyankatesh.vercel.app](https://vyankatesh.vercel.app/)

