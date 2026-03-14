import os

folder = "files"

for count, filename in enumerate(os.listdir(folder)):
    dst = f"file_{count}.txt"
    src = os.path.join(folder, filename)
    dst = os.path.join(folder, dst)
    os.rename(src, dst)

print("Files renamed successfully")
