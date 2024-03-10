from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)

    # Build the path to the CSV file
    file_path = os.path.join(script_dir, '..','data/raw/matches.csv')

    # Now you can read the CSV file with pandas
    df = pd.read_csv(file_path)

    # Convert the DataFrame to HTML
    table = df.to_html(index=False)

    # Render the HTML
    return render_template('index.html', table=table)

if __name__ == '__main__':
    app.run(debug=True)