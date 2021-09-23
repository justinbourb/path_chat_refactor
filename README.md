This is an example python flask pathology laboratory website using an sqlight database with websockets chat.
The app provides users a login page, custom order form and chat room to discuss slide images online.  This project was "completed" in 2018.

## Installation & setup
- Download the repo from github to your local environment.  This app was built using Windows 10.
- Install the requirements listed in the requirements.txt
    - Note: You may want to use a virtual environment, since each Python project has different requirements.
    - Installation may be done using pip install commands
    - If using Pycharm packages can also be installed from File->Settings->Project->Python Interpreter-> + 
    symbol in the top right
- Pycharm run configurations can be set from Run -> Edit Configurations
    - Target: set as the path to app.py
    - FLASK_ENV: development
    - Python interpreter: set as path to your python install (or virtual environment for this project)
    - Check: Add content roots to PYTHONPATH
    - Check: Add source roots to PYTHONPATH
    ![image](https://github.com/justinbourb/path_chat_refactor/blob/master/static/images/ReadMe_images/Pycharm_run_configurations.JPG)
## Running the app
- With the project open select the Pycharm terminal and type 'flask run' (without quotations)
    - Note: This is a little different than the standard instructions for running a flask app.  
    Pycharm behaves differently.
- The local server should be running at 127.0.0.1:5000 as specified in the terminal
![image](https://github.com/justinbourb/path_chat_refactor/blob/master/static/images/ReadMe_images/Pycharm_flask_run.JPG)

## App details
- The PathChat website requires users to log in to access both the chat (powered by Websockets) 
 and the order form to place a new order.
- The chatroom is powered by websockets (websockets.py)
- Data for each user and order placed is stored in a sqlite database using Flask-SQLAlchemy
- Users can change their details or password under their profile 
- Users can request password resets
- Users can place orders or chat

## Using the database
- Creating the database for the first time
    - flask db init
- Changing Database contents
    - flask db migrate -m "your message"
        - This does not make any changes, it generates the migration script.  This script should be verified as
         correct before running.
    - flask db upgrade
        - This command will either create or update the database.
    - flask db downgrade
        - This undoes the last upgrade

## Viewing data in the database
- Data can be viewed via the PyCharm terminal 
    - from app import db
    - from Order_Form_Models import Sample_Order
    - orders = Sample_Order.query.all()
    - from models import User
    - users = Users.query.all()
- Query data can be modified by changing the def __repr__(self): functions for the User or Sample_Order models.
![image](https://github.com/justinbourb/path_chat_refactor/blob/master/static/images/ReadMe_images/database_access_orders_from_terminal.JPG)
![image](https://github.com/justinbourb/path_chat_refactor/blob/master/static/images/ReadMe_images/database_access_users_from_terminal.JPG)
## Further database explanations
- The database stores the user information and orders placed via the order form page.
- Alembic maintains a migration repository, which is a directory in which it stores its migration scripts. 
 Each time a change is made to the database schema, a migration script is added to the repository with the 
 details of the change. To apply the migrations to a database, these migration scripts are executed in the 
 sequence they were created.
- With the migration repository in place, it is time to create the first database migration, which will 
  include the users table that maps to the User database model. There are two ways to create a database 
   migration: manually or automatically. To generate a migration automatically, Alembic compares the database 
   schema as defined by the database models, against the actual database schema currently used in the database.
    It then populates the migration script with the changes necessary to make the database schema match the 
    application models. In this case, since there is no previous database, the automatic migration will add 
    the entire User model to the migration script. The flask db migrate sub-command generates these automatic
    migrations: flask db migrate -m "your message"
    
## Website Images
![image](https://github.com/justinbourb/path_chat_refactor/blob/master/diagram.png)
![image](https://github.com/justinbourb/path_chat_refactor/blob/master/static/images/ReadMe_images/path_chat_main_page.png)
![image](https://github.com/justinbourb/path_chat_refactor/blob/master/static/images/ReadMe_images/Profile_page.JPG)
![image](https://github.com/justinbourb/path_chat_refactor/blob/master/static/images/ReadMe_images/order_form.JPG)
![image](https://github.com/justinbourb/path_chat_refactor/blob/master/static/images/ReadMe_images/chat_page.JPG)
