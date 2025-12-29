# app.py
import pandas as pd
from flask import Flask, render_template_string
from scipy.io import arff

app = Flask(__name__)

# Load EEG Eye State dataset (.arff)
DATA_PATH = "EEG Eye State.arff"  # place file here

def load_data(path):
    raw_data = arff.loadarff(path)
    df = pd.DataFrame(raw_data[0])
    # Decode bytes to str if needed
    for col in df.select_dtypes([object]):
        df[col] = df[col].str.decode("utf-8")
    return df

@app.route("/")
def index():
    df = load_data(DATA_PATH)
    # Show first 10 rows
    table_html = df.head(10).to_html(classes="table table-striped")
    return render_template_string("""
        <!doctype html>
        <html>
        <head>
            <title>EEG Eye State Preview</title>
            <link rel="stylesheet"
             href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        </head>
        <body class="container">
            <h1 class="mt-4">EEG Eye State Dataset Preview</h1>
            {{ table|safe }}
        </body>
        </html>
    """, table=table_html)

if __name__ == "__main__":
    app.run(debug=True)
