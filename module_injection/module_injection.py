
def module_injection_noncompliant():
    import importlib
    module_name = input('module name')
    importlib.import_module(module_name)
