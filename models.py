"""
This file defines the database models
"""

from .common import db, Field
from pydal.validators import *

### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
#
# db.commit()
#

db.define_table('dog',
                Field('name'),
                Field('breed'))

db.commit()

if len(db(db.dog.id > 0).select()) == 0:
    db.dog.insert(name='Spot', breed='Beagle')
    db.dog.insert(name='Judge', breed='St Bernard')
    db.dog.insert(name='Chip', breed='German Shepard')
    db.dog.insert(name='Stella', breed='Border Collie')
    db.dog.insert(name='Syd', breed='Golden Lab')

    db.commit()
