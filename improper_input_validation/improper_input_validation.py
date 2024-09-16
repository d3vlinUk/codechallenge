
def yaml_load():
    import json
    import yaml
    response = yaml.dump({'a': 1, 'b': 2, 'c': 3})
    # Noncompliant: uses unsafe yaml load.
    result = yaml.load(response)
    yaml.dump(result)
