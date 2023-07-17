import hello_world # imports only load the modules once per run

# in order to import multiple times in run time we could do

# Reload the module and return it.
# The module must have been successfully imported before.
# This allows you to edit and pick up new code on the fly within the current Python interactive session.

from importlib import reload

reload(hello_world)