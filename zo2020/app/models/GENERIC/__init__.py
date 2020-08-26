''' Generic models are models that exist outside of the specific or 
abstract folders, they are usually models which are created and managed 
by ZO staff and other models just reference them, they do not alter 
or create them. Example being Gender(), many other models may refer
to them. '''

from .person import *