"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        courses = self.models['WelcomeModel'].get_all_courses()
        print 'at the index'
        return self.load_view('index.html', courses = courses)

    def add(self):
        # in actuality, data for the new course would come 
        # from a form on our client
        course_details = {
            'title': request.form['name'],
            'description': request.form['description']
        }
        self.models['WelcomeModel'].add_course(course_details)
        return redirect('/')

    def delete(self, id):
        courses = self.models['WelcomeModel'].get_course_by_id(id)
        print courses
        return self.load_view('delete.html', courses = courses, id=id)
    def donezo(self, id):
        self.models['WelcomeModel'].delete_course(id)
        print id
        return redirect('/')

