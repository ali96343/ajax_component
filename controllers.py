from yatl.helpers import XML

from py4web import action, request, redirect, URL
from py4web.utils.form import Form, FormStyleBulma
from .common import db, session, auth, unauthenticated


@unauthenticated("index", "index.html")
def index():
    dogs = db(db.dog.id > 0).select()
    return dict(dogs=dogs)


@action('edit_dog', method=['GET', 'POST'])
@action.uses(session, db, auth, 'edit_dog.html')
def edit_dog():
    dog_id = request.query.get('id')
    form = Form(db.dog, record=dog_id, formstyle=FormStyleBulma)
    form.param.sidecar = [XML('<button class="button" onclick="close_modal();" '
                              'style="margin-left: .5rem;">Cancel</button>')]

    if form.accepted:
        url = URL('index')
        redirect(url)

    return dict(form=form)
