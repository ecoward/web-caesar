from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form="""

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>       
        <h1><form action="/encrypt" method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0"/>
                <p class="error"/></p>
            </div>
            <textarea type="text" name="text"/>{0}</textarea>
            <br>
            <input type="submit" value="Submit"/>
        </form></h1>
    </body>
        
    </html>
                
                
                    
  
"""





@app.route("/")
def index():
    return form.format("")

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot = int(request.form["rot"])
    encrypted_text = request.form["text"]
    return form.format(rotate_string(encrypted_text, rot))

app.run()


