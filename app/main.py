import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# vars
main_categories = []

# Use the application default credentials.
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)
db = firestore.client()

db_ref = db.collection(u'quiz-db')
firestore_main_categories = db_ref.where('type', '==', 'main-category')

@app.route('/')
@app.route('/index')
def index():
#    if doc.exists:
#        text_entry = 'Document found!'
#    else:
#        text_entry = 'No such document!'
    return render_template('index.html', main_categories=main_categories)

if __name__ == '__main__':
    for main_category in firestore_main_categories.stream():
        main_categories.append((main_category.to_dict()))
    app.run(debug=True, host='0.0.0.0', port=8080)
