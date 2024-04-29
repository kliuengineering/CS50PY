def DefineType(var):
    rc = ""
    name_array = var.strip().lower().split(".")
    suffix = name_array[-1]
    if suffix == "jpeg" :
        rc = "image/jpeg"
    elif suffix == "jpg" :
        rc = "image/jpeg"
    elif suffix == "png":
        rc = "image/png"
    elif suffix == "gif":
        rc = "image/gif"
    elif suffix == "pdf":
        rc = "application/pdf"
    elif suffix == "txt":
        rc = "text/plain"
    elif suffix == "zip":
        rc = "application/zip"
    else:
        rc = "application/octet-stream"
    return rc

def main():
    print( DefineType( input("File name: ") ) )

main()
