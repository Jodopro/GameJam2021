set up virtual environment:\
`python3.8 -m virtualenv venv` (if python3.8 is not installed, most other versions of python >= 3.6 should work)


activate virtual environment:\
`. ./venv/bin/activate` on ubuntu \
`.\venv\Scripts\active` for windows


and subsequently install the requirements:\
`pip install -r requirements.txt`

then, to run, move into the src directory:\
`cd src`\
and then run main.py:\
`python main.py`




classes:
Game (keeps track of all objects)
Ship
Obstacle
    Cloud (starts as gray, turns either white or dark grey (thunder), hint where the thunder will strike under the cloud by showing some kind of warning, random x coordinate)
    Bird
    Plane
    Alien
    Policebox?
Enemy (all enemies are obstacles)
    Bird
    Plane
    Alien
    
Attack
    SoundWave
    Bliksem

Drawable & Updatable
    Ship
    Obstacle
    Enemy
    Attack



