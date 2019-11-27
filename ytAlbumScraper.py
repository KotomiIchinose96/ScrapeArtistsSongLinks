from selenium import webdriver
import urllib.parse
import math

# artists_file = open("artists.txt", "a")
#
# getVars = {'q': "best rock bands"}
# url = 'http://www.google.com/search?' + urllib.parse.urlencode(getVars)
#
# browser = webdriver.Firefox()
# browser.maximize_window()
# browser.implicitly_wait(30)
# browser.get(url)
#
# bandslen = len(browser.find_elements_by_class_name("klitem"))
# for bandindex in range(bandslen):
#     if bandindex % 7 == 0:
#         try:
#             browser.find_element_by_class_name("PUDfGe").click()
#         except:
#             print("error")
#     # for i in range(math.floor(bandindex/7)):
#     #     try:
#     #
#     #     except:
#     #         print(" Error ")
#     bandname = browser.find_elements_by_class_name("klitem")[bandindex].get_attribute("aria-label")
#     print(bandname)
#     artists_file.write(f"{bandname}\n")
#
# artists_file.close()
# print("complete")


output_file = open("songs.csv", "a")

def getartistsongs(artist):
    
    getVars = {'q': artist + " albums"}
    url = 'http://www.google.com/search?' + urllib.parse.urlencode(getVars)
    
    # print(url)
    
    # create a new Firefox session
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(30)
    browser.get(url)
    
    # song_list = []
    
    albumslen = len(browser.find_elements_by_class_name("klitem"))
    albumindex = 0
    for i in range(0,albumslen):
        albums = browser.find_elements_by_class_name("klitem")
        album = albums[albumindex]
        album_name = album.get_attribute("title")
        # print(f"album_name = {album_name}")
        album.click()
        browser.find_element_by_class_name("P7Vl4c").click()
        songslen = len(browser.find_elements_by_class_name("rl_item_base"))
        # print(f"songs = {len(songs)}")
        
        songindex = 0
        for j in range(0,songslen):
            songs = browser.find_elements_by_class_name("rl_item_base")
            song = songs[songindex]
            for i in range(math.floor(songindex/12)):
                browser.find_element_by_class_name("kKuqUd").click()
            song_name = song.text.replace("\n",". ")
            song.click()
            try:
                browser.find_element_by_class_name("j0joJb").click()
            except:
                output_file.write(f'"{artist}","{album_name}","{song_name}","**Error**"\n')
                browser.back()
                continue
            song_link = browser.current_url
            # song_list.append((artist, album_name, song_name, song_link))
            songindex += 1
            output_file.writelines(f'"{artist}","{album_name}","{song_name}","{song_link}"\n')
            print((artist, album_name, song_name, song_link))
            browser.back()
            browser.back()
            # break
        albumindex += 1
        browser.back()
        # browser.back()
        # break
    
    browser.quit()

artist_file = open("artists.txt","r")

for lines in artist_file.readlines():
    getartistsongs(lines[:-2])

artist_file.close()
output_file.close()
print("completed")












# output_file = open("songs.csv", "a")
#
# for line in artists_file.readlines():
#     print(line)
#
# getartistsongs("Guns N Roses")
#
# output_file.close()


# class = "EDblX DAVP1"  (div that contains all albums)
# class = "MiPcId mlo-c r-iJ6N1X_mhrv4" (div that contains the album item)
# class = "klitem" (a that contains the href and the title contains the album name)
# click on the above a element
# on the new page look for the class "P7Vl4c" a element and click that for the list of songs
# once the above has been clicked each song is inside the div with class "EDblX DAVP1"
# each song is an a element with the class "rl_item rl_item_base" title attribute is song name
# once the above has been clicked
# then click on the a element in the div with the class "r H1u2de"
# when that link goes through it is the youtube video








# browser.fullscreen_window()

# search_elem = browser.find_element_by_tag_name("input")
# #elem = browser.find_element_by_name('search')  # Find the search box
# search_elem.send_keys('acdc' + Keys.RETURN)
#
#
# # div id = "items" class = "yt-simple-endpoint style-scope ytd-search-refinement-card-renderer"
#
# #albums_div = browser.find_elements_by_class_name("style-scope ytd-horizontal-card-list-renderer")
# albums_list = browser.find_elements_by_tag_name("ytd-search-refinement-card-renderer")
# # <ytd-search-refinement-card-renderer class="style-scope ytd-horizontal-card-list-renderer" card-style="universal_watch_card">
# #
# # <a class="yt-simple-endpoint style-scope ytd-search-refinement-card-renderer" href="/playlist?list=OLAK5uy_kaueFscwZLW5eh2di3wmeerRd-uMPbH1E&amp;playnext=1&amp;index=1">
# # <yt-img-shadow class="style-scope ytd-search-refinement-card-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="" src="https://i9.ytimg.com/s_p/OLAK5uy_kaueFscwZLW5eh2di3wmeerRd-uMPbH1E/mqdefault.jpg?sqp=CMC8j-wFir7X7AMGCKaQ3eEF&amp;rs=AOn4CLANrcOncO12ISHbW2srUYgB6czdeg&amp;v=1547126822" width="90" height="90"></yt-img-shadow>
# # <div id="card-title" class="style-scope ytd-search-refinement-card-renderer">
# # <div class="style-scope ytd-search-refinement-card-renderer">Use Your Illusion I</div>
# # </div>
# # </a>
# # </ytd-search-refinement-card-renderer>
# links = []
# titles = []
#
# for album in albums_list:
#     print(album)
#     a_elem = album.find_element_by_tag_name('a')#"yt-simple-endpoint style-scope ytd-search-refinement-card-renderer")
#     links.append(a_elem.get_attribute("href"))
#     # outer_div = album.find_elements_by_class_name("card-title")
#     # print(len(outer_div))
#     # print(outer_div)
#     # inner_div = outer_div[0].find_elements_by_class_name("style-scope ytd-search-refinement-card-renderer")
#     # titles.append(inner_div[0].text)
#     #print(f"a_elem = {a_elem}")
#     #print(f"a_elem.get_attribute(\"href\") = " + a_elem.get_attribute("href"))
#
# print(zip(links, titles))


