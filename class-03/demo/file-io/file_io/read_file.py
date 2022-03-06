

def read_file(path):
    try:
        f = open(path)
    except FileNotFoundError:
        content = "Error: Sorry the file does not exist!"
    else:
        content = f.read()
        f.close()
        with open("./assets/spam_copy.txt", "w") as f:
            f.write(f"THIS IS A COPY OF\n{content}")
    
    finally:
        return content

if __name__ == "__main__":

    content = read_file("./assets/spam.txt")
    with open("./assets/brain.jpg","rb") as img:
        content = img.read()
    with open("./assets/brain_copy.jpg","wb") as img2:
        img2.write(content[:len(content)//2])
