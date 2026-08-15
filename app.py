from flask import Flask
app=Flask(__name__)
@app.get('/')
def home(): return '<h1>Mary Reyes Program</h1><p>Website is online.</p>'
if __name__=='__main__': app.run(host='0.0.0.0',port=5000)
