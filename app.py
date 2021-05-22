from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet 
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"]) 
def add_pet():
    form = AddPetForm() # make new Form Object 

    # validate CSRF Token on submit 
    if form.validate_on_submit():
        # form data 
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data 

        # new_pet 
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        # db.session
        db.session.add(new_pet)
        db.session.commit() 

        # redirect 
        return redirect('/')
    else: 
        # render form 
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>')
def display_pet(pet_id):
    """Display Pet Details"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet) 
