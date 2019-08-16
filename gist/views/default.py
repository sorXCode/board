from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

from .. import models


class Logger:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='../templates/home.jinja2')
    def home(self):
        if 'feedback.submitted' in self.request.params:
            subject = self.request.params['subject']
            full_name = self.request.params['full_name']
            email = self.request.params['email']
            message = self.request.params['message']
            print(subject, full_name, email, message)

            def log():
                entry = models.Feedback(
                    subject=subject,
                    full_name=full_name,
                    email=email,
                    message=message
                )
                self.request.dbsession.add(entry)
            log()
        return {}

    @view_config(route_name="records", renderer='../templates/records.jinja2')
    def log_history(self):
        '''
        Displays all submitted forms
        '''
        table = self.request.dbsession.query(models.Feedback)
        return dict(table=table)
