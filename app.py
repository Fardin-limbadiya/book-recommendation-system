from flask import Flask, render_template, request
import pickle
import numpy as np

popular_df = pickle.load(open('model/popular.pkl', 'rb'))
pt = pickle.load(open('model/pt.pkl','rb'))
books = pickle.load(open('model/books.pkl','rb'))
similarity_scores = pickle.load(open('model/similarity_score.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                        book_name= list(popular_df['Book-Title'].values),
                        author=list(popular_df['Book-Author'].values),
                        image=list(popular_df['Image-URL-M'].values),
                        votes=list(popular_df['num_ratings'].values), 
                        rating=list(popular_df['avg_rating'].values)
                        )
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input').strip()
  # Check if book exists in pt.index
    if user_input not in pt.index:
        return render_template('recommend.html', data=None, message=f"❌ Book '{user_input}' not found. Try another.")

    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key = lambda x:x[1],reverse = True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = (books[books['Book-Title']==pt.index[i[0]]])
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)
    return render_template('recommend.html',data = data)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(f"Feedback from {name} ({email}): {message}")
    return "Thank you for your feedback!"


if __name__ == '__main__':
    app.run(debug=True)