ALLOWED_EXTENTION = {"jpg", "png", "jpeg"}
BUCKET_NAME = "momento"

def allowed_file(filename):
    filename = filename.lower()
    extention = filename.split(".")[-1]
    return extention in ALLOWED_EXTENTION