# NewsStream

NewsStream is a web application that uses a news API to fetch and display the latest news articles from various categories, including World, General, Business, Technology, Health, Sports, and Entertainment.

## Features

- Display news articles from multiple categories.
- Search functionality to find specific news articles.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Python)
- **APIs**: News API for fetching news articles

## Getting Started

### Prerequisites

- **Python 3.12.2** 
- **Django** framework
- **News API key** (you can obtain one by signing up at [News API](https://newsapi.org))

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vijayhukum/NewsStream.git
2. **Navigate to the project directory**
      - cd NewsStream
        
3. **Create a virtual environment**
      - python -m venv venv
        
4. **Activate the virtual environment**
      - venv\Scripts\activate
        
5. **Install the required packages**
      - pip install -r requirements.txt
        
6. **Set up environment variables**
      Create a .env file in the project root and add your News API key
      - NEWS_API_KEY=your_api_key_here
        
7. **Run the migrations (if applicable)**
      - python manage.py migrate
        
8. **Run the development server**
     -  python manage.py runserver
       
9. **Access the application**
      -  http://127.0.0.1:8000
