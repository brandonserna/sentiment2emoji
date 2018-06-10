from flask import Flask, request, jsonify, redirect
import pickle


app = Flask(__name__)
# Load scikit learn model
clf = pickle.load(open('gb_model.sklearn', 'rb'))
# Load previous tfidf representation
load_tfidf = pickle.load(open('tfidf.sklearn', 'rb'))
print('Loaded model ✔')

@app.route('/', methods=['GET'])
def get():
    return redirect('/predict')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        
        try:
            # pre-process
            x = str(request.form.get('query'))
            tfidf = load_tfidf.transform([x])
            prediction = clf.predict(tfidf)

            if prediction == ['love']:
                return '😍'
            if prediction == ['anger']:
                return '😡'
            if prediction == ['joy']:
                return '😊'
            if prediction == ['sad']:
                return '☹️'
            if prediction == ['fear']:
                return '😳'
            if prediction == ['surprised']:
                return '🤭'
        except Exception as e:
            print(e)
            return '☠️'
    return '''
    <!doctype html>
    <title>Sentiment2Emoji</title>
    <h1>Enter a text snippet to predict the sentiment</h1>
    <br>
    <p><strong>Example: </strong>
    <br>
    Collard greens are absolutely disgusting.
    <form method=post>
      <p><input type=text name=query>
         <input type=submit>
    </form>
    '''


if __name__ == '__main__':
    try:
        # Load scikit learn model
        clf = pickle.load(open('gb_model.sklearn', 'rb'))
        # Load previous tfidf representation
        load_tfidf = pickle.load(open('tfidf.sklearn', 'rb'))
        print('Resources Loaded')

    except Exception as e:
        print(e)
        clf = None

    app.run(host='0.0.0.0', port=9999, debug=True)