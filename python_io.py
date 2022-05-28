import time

lyrics = open('song_lyrics.txt')

# how to over road
# lyrics.write('ひとりぽっちの夜')
# lyrics.flush()
# lyrics.close()

# how to read file
lyriclines = lyrics.readlines()

for song in lyriclines:
  print(song)
  time .sleep(4.5)


menu ="""
(1) ue wo muite arukou
(2) bara no hana
"""

print(menu)
choice = int(input("enter song number:"))

selected_filename = "" # empty -> len() = 0
if choice == 1:
  selected_filename = "song_lyric.txt"
elif choice == 2:
  selected_filename = "bara_no_hana.txt"

if len(selected_filename) > 0:
  lyrics = open(selected_filename)
  lyriclines = lyrics.readlines()

  for 歌 in lyriclines:
    print(歌)
    time.sleep(4.5)
else:
  print("incorrect song number!")
  