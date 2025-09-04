# 📚 Book Recommendation System

A web-based book recommendation system built with Flask that suggests books based on user preferences and popularity ratings.

## 🌟 Features

- Display top 50 popular books with ratings and author information
- Interactive book cards with flip animation
- Personalized book recommendations based on user input
- Contact form for user feedback
- Responsive design for all devices

## 🛠️ Technologies Used

- Python 3.x
- Flask
- Pandas
- NumPy
- Pickle
- Bootstrap 5
- HTML/CSS

## 📁 Project Structure

```
book_recommend_system_UI/
├── app.py
├── model/
│   ├── books.pkl
│   ├── popular.pkl
│   ├── pt.pkl
│   └── similarity_score.pkl
├── templates/
│   ├── contact.html
│   ├── index.html
│   └── recommend.html
└── README.md
```

## 🚀 Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/your-username/book-recommendation-system.git
cd book-recommendation-system
```

2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Unix/macOS
venv\Scripts\activate     # For Windows
```

3. Install required packages
```bash
pip install flask pandas numpy
```

4. Run the application
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## 📸 Screenshots

<img width="1919" height="933" alt="image" src="https://github.com/user-attachments/assets/2c93b712-cbe1-4dc5-acd4-5bbbcad31f56" />
<img width="1915" height="920" alt="image" src="https://github.com/user-attachments/assets/7d15da05-9741-4817-9e72-3537ce64ffbc" />
<img width="1885" height="923" alt="image" src="https://github.com/user-attachments/assets/e1155ef9-553c-40ec-9d98-8d3da1cf589a" />


## 🔧 How It Works

The system uses collaborative filtering and content-based filtering to recommend books:

1. **Popular Books**: Displays top-rated books based on user ratings and popularity
2. **Recommendation Engine**: Suggests similar books based on user input using:
   - Collaborative filtering
   - Similarity scores
   - Book metadata analysis

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Data source: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset
