import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def moveFiles(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{files}")

if __name__ == "__main__":
    files = os.listdir()
    files.remove("main.py")

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Medias')
    createIfNotExist('Others')

    imgExt = [".jpg", ".jpeg", ".png"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]

    docExt = [".txt", ".doc", ".docx", ".xlsl", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExt]

    mediaExt = [".mp3", ".mp4", ".mkv", ".flv", ".avi"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExt) and (ext not in docExt) and (ext not in mediaExt) and os.path.isfile(file):
            others.append(file)

    moveFiles("Images", images)
    moveFiles("Docs", docs)
    moveFiles("Medias", medias)
    moveFiles("Others", others)
