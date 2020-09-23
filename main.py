import flask
import os
import random

app = flask.Flask(__name__)

@app.route('/') # Python decorator
def index():
    # Choose a random number of potatoes and generate them
    numPotatoes = random.randint(10, 20)
    potatoes = createPotatoes(numPotatoes)
    return flask.render_template(
        "index.html",
        numPotatoes=numPotatoes,
        potatoes=potatoes,
    )
    
def createPotatoes(numPotatoes):
    # Each potato must be different, so generate values for
    # position, size, transparency, and rotation. You could also
    # theoretically add more potato images and randomly select one for
    # more variation.
    
    # Position/size/opacity are measured in percentages, while rotation
    # is measured in degrees
    potatoes = []
    for i in range(numPotatoes):
        currPotato = {}
        currPotato['position'] = {
            'x': f'{random.randint(0, 100)}%',
            'y': f'{random.randint(0, 100)}%',
        }
        currPotato['size'] = f'{random.randint(3, 20)}%'
        currPotato['opacity'] = f'{random.randint(20, 50)}%'
        currPotato['rotation'] = f'{random.randint(0, 360)}deg'
        potatoes.append(currPotato)
    return potatoes
    
app.run(
    debug=True,
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
