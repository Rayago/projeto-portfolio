from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.router('/')

if __name__ == '__main__':
    app.run()