import streamlit as st
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:vedesh@123@localhost/your_database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a User model (table)
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"

# Create the tables in the database
with app.app_context():
    db.create_all()  # Create all tables defined by models (in this case, 'users')

# API Route to Create a User
@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        # Get data from the request
        data = request.get_json()
        name = data.get('name')

        if not name:
            return jsonify({"error": "Name is required"}), 400
        
        # Create a new User instance
        new_user = User(name=name)

        # Add to the session and commit the transaction to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": f"User {name} created successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Route to Get all Users
@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        users_list = [{"id": user.id, "name": user.name} for user in users]
        return jsonify({"users": users_list}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)


st.set_page_config(
    page_title="FitFusion - AI for Fitness and Nutrition",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = ["Homepage", "Sign-Up", "Dashboard", "Meal Planner", "Fitness Tracker", "Progress", "About Us"]
selected_page = st.sidebar.radio("Go to", pages)

# Route to different pages
if selected_page == "Homepage":
    import pages.homepage as homepage
    homepage.show()
elif selected_page == "Sign-Up":
    import pages.signup as signup
    signup.show()
elif selected_page == "Dashboard":
    import pages.dashboard as dashboard
    dashboard.show()
elif selected_page == "Meal Planner":
    import pages.meal_plan as meal_plan
    meal_plan.show()
elif selected_page == "Fitness Tracker":
    import pages.fitness_tracker as fitness_tracker
    fitness_tracker.show()
elif selected_page == "Progress":
    import pages.progress as progress
    progress.show()
elif selected_page == "About Us":
    import pages.about as about
    about.show()
