# 🤩 Sentiment2Emoji 🤩

Find an emoji for a passage of text. This project uses machine learning to predict the sentiment of a given string and return an appropriate emoji. 

The project uses Flask for the backend server along with Swagger docs for the service. It also uses a Vue frontend hosted on github. 

[Website](https://brandonserna.github.io/sentiment2emoji/)

[API Docs](https://sentiment2emoji.herokuapp.com)

__Note__ — Emojis are best seen on updated iOS or a mac, sometimes the conversion for anger/surprised doesn't show up correctly

_Emotions_:

* Love
* Anger
* Joy
* Surprise
* Sadness
* Fear

### Sample

__input:__ "The last jedi was the greatest movie!"

__output:__ 😍

__input:__ "Collard greens are absolutely disgusting "

__output__: 😡

### Quick Start for Flask app

```sh
python app.py
```

### Demo

```
https://sentiment2emoji.herokuapp.com/predict
```

## Frontend

Using Vue and Vuetify

```sh
vue create frontend
vue add vuetify
npm run build
```



### Resources and References

Thank you

* Python
* Flask restplus
* Vue
* Pandas
* Scikit-learn
* Numpy
* Matplotlib
* Data: ```F. Calefato, F. Lanubile, N. Novielli. “[EmoTxt: A Toolkit for Emotion Recognition from Text](https://arxiv.org/abs/1708.03892)” To appear in *Proceedings of ACII 2017, the 7th International Conference on Affective Computing and Intelligent Interaction*, San Antonio, USA, Oct. 23-26, 2017.```