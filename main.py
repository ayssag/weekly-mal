from modules.myanimelist import Manga, getMangaUpdates, Anime, getAnimeUpdates

rss_manga = 'https://myanimelist.net/rss.php?type=rm&u=claricespectro'
rss_anime = 'https://myanimelist.net/rss.php?type=rw&u=claricespectro'

manga_updates = getMangaUpdates(rss_url=rss_manga, number_of_entries=15)

anime_updates = getAnimeUpdates(rss_url=rss_anime, number_of_entries=15)

print('>'*10, 'Manga Updates:')

for manga in manga_updates:
    print(manga_updates[manga])

print('>'*10, 'Anime Updates:')

for anime in anime_updates:
    print(anime_updates[anime])