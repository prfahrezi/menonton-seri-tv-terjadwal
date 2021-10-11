import os

folder_twzone = "D:\Video\TV Shows\Twilightzone\Best of"

os.chdir(folder_twzone)

playlist = []
watchedlist = []

for root, dir, files in os.walk(folder_twzone):
    for s in range(5):
        for e in range(40):
            play = f"S{str(s)} Episode ({str(e)}).mkv"
            if play in files:
                playlist.append(play)

if len(playlist) == 0:
    print("Tidak ada episode baru untuk diputar")
else:
    print(f"Sedang diputar: {playlist[0]}")
    os.startfile(playlist[0])

#     for i in range(30):
#         todayeps = "Episode (" + str(i) + ").mkv"
#         ditonton = ".Episode (" + str(i) + ").mkv"
#         if todayeps in files:
#             playlist.append(todayeps)
#         elif ditonton in files:
#             watchedlist.append(ditonton)
#
# if len(playlist) == 0 and ".Episode (29).mkv" in watchedlist:
#     print("Season 1 Twilight Zone sudah selesai.")
#     print("Menunggu season berikutnya.")
# elif len(playlist) != 0:
#     if playlist[0] == "Episode (29).mkv":
#         print("LAST EPISODE OF SEASON 1 OF TWILIGHT ZONE")
#     else:
#         os.startfile(playlist[0])
