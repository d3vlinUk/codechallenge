def create_file_noncompliant(results):
    import tempfile
    filename = tempfile.mktemp()
    with open(filename, "w+") as f:
        f.write(results)
    print("Results written to", filename)
