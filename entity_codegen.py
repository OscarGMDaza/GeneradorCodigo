"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm

def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    # Se crea el modelo a partir del archivo modelo.ent
    modelo_model = entity_mm.model_from_file(join(this_folder, 'modelo.ent'))

    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in modelo_model.entities:
            return True
        else:
            return False

    def pytype(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {
                'integer': 'Integer',
                'string': 'String'
        }.get(s.name, s.name)

    # Crea la carpeta de salida
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Se inicializa Jinja
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Java type names.
    jinja_env.tests['entity'] = is_entity
    jinja_env.filters['pytype'] = pytype

    # Se carga el template a utilizar, en este caso para crear modelsEntidad.py
    template = jinja_env.get_template('models.template')

    for entity in modelo_model.entities:
        # For each entity generate js file
        with open(join(srcgen_folder,
                       "models%s.py" % entity.name), 'w') as f:
            f.write(template.render(entity=entity))

    # Se carga el template a utilizar, en este caso para crear config_app.py
    template = jinja_env.get_template('config_app.template')

    for entity in modelo_model.entities:
        # For each entity generate js file
        with open(join(srcgen_folder,
                       "config_app.py"), 'w') as f:
            f.write(template.render(entity=entity))

    # Se carga el template a utilizar, en este caso para crear requerimientos.txt
    template = jinja_env.get_template('requerimientos.template')

    for entity in modelo_model.entities:
        # For each entity generate js file
        with open(join(srcgen_folder,
                       "requerimientos.txt"), 'w') as f:
            f.write(template.render(entity=entity))

    # Se carga el template a utilizar, en este caso para crear Dockerfile
    template = jinja_env.get_template('Dockerfile.template')

    for entity in modelo_model.entities:
        # For each entity generate js file
        with open(join(srcgen_folder,
                       "Dockerfile"), 'w') as f:
            f.write(template.render(entity=entity))

    # Se carga el template a utilizar, en este caso para crear app.py
    template = jinja_env.get_template('app.template')

    for entity in modelo_model.entities:
        # For each entity generate js file
        with open(join(srcgen_folder,
                       "app.py"), 'w') as f:
            f.write(template.render(entity=entity))                                

if __name__ == "__main__":
    main()