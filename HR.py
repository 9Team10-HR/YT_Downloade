import sys 
from pytube import YouTube 
username = "habib"
password = '123'

logo = """ \033[0;31m 
╭╮╱╱╭┳━━━━╮╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮
┃╰╮╭╯┃╭╮╭╮┃╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃┃
╰╮╰╯╭┻╯┃┃╰╯╱┃┃┃┣━━┳╮╭╮╭┳━╮┃┃╭━━┳━━┳━╯┣━━┳━╮
╱╰╮╭╯╱╱┃┃╱╱╭╯╰╯┃╭╮┃╰╯╰╯┃╭╮┫┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯
╱╱┃┃╱╱╱┃┃╱╱╰━━━┻━━╯╰╯╰╯╰╯╰┻━┻━━┻╯╰┻━━┻━━┻╯
-------------------------------------------"""

 
givenusername = input("\033[0;36mEnter your Username : ")
 
if givenusername == username : 
  print("\033[0;35mCorrect username ")
else : 
   print("\033[0;31mWorong Pass")
givenpassword = input("\033[0;33mEnter Your Pass: ")

if givenpassword == password : 
  print("correct password ")
else : 
   print("wrong password")
   sys.exit ()
   
print(logo)

link = input("Enter the YouTube video URL: ")
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")
