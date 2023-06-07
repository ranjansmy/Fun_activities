# Write a python3 snippets that computes the MD5 sum of the data in a file. You don't need to worry about any of the file's metadata, such as last modified time or the file's name, only it's content 
import hashlib

def md5_sum(file_path):
  with open(file_path, "rb") as f:
    md5 = hashlib.md5()
    for chunk in iter(lambda: f.read(4096), b""):
      md5.update(chunk)
    return md5.hexdigest()

if __name__ == "__main__":
  file_path = input("Enter the file path: ")
  md5_sum = md5_sum(file_path)
  print("The MD5 sum of the file is:", md5_sum)
'''
This snippet first imports the hashlib module, which provides a number of hash functions, including MD5. It then defines a function called md5_sum(), which takes a file path as its only argument. The function opens the file in binary mode and then reads the contents of the file in chunks of 4096 bytes. For each chunk, the function updates the MD5 hash object. Once the entire file has been read, the function returns the MD5 hash object as a hexadecimal string.
The if __name__ == "__main__" block is used to run the code if the snippet is being run as a script. The block prompts the user for the file path and then calls the md5_sum() function to compute the MD5 sum of the file. The MD5 sum is then printed to the console.
'''
