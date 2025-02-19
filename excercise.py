name = "Jhon Doe"
age = 33
height = 1.75
is_student = False
score = [4.2, 3.5, 5]
files = {"file1": "file1.txt", "file2": "file2.txt", "file3": "file3.txt"}

print(f"Name: {name}", type(name))
print(f"Age: {age}", type(age))
print(f"Height: {height}", type(height))
print(f"Is student: {is_student}", type(is_student))
print(f"Score: {score}", type(score))
print(f"Files: {files}", type(files))

score.append(2.5)
print(f"Score (Modified): {score}", type(score))
score.remove(3.5)
print(f"Score (Modified): {score}", type(score))
score.pop()
print(f"Score (Modified): {score}", type(score))

files["file4"] = "file4.txt"
print(f"Files (Modified): {files}", type(files))
files['file1'] = "file1_modified.txt"
print(f"Files (Modified): {files}", type(files))
files.pop("file2")
print(f"Files (Modified): {files}", type(files))