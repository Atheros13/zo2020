from django import forms

class PublicContactForm(forms.Form):

    '''Creates a Form object that View will instruct a Template 
    to interpret into a form for people to fill out. The View will 
    use its get() method to create the blank form, and the 
    post() method to access the process_form() method of the Form.'''

    pass



    def process_form(self, request, *args, **kwargs):

        pass