import feedparser
from pydantic import BaseModel
from typing import List, Dict, Optional

class Manga(BaseModel):
    title: str
    link: str
    updates: List[str] = []

class Anime(BaseModel):
    title: str
    link: str
    updates: List[str] = []

def groupMangaByTitle(entries: List)->Dict:
    manga_by_title = {}
    for entry in entries:
        if not entry.title in manga_by_title:
            manga_by_title[entry.title] = Manga(title=entry.title,link=entry.link)
    return manga_by_title

def groupUpdatesByTitle(entries: List, manga_by_title: Dict)->Dict:
    for entry in entries:
        manga_by_title[entry.title].updates = entry.summary
    return manga_by_title

def getMangaUpdates(rss_url: str, number_of_entries: int)->List:
    feed = feedparser.parse(rss_url)
    entries = [entry for entry in feed.entries]
    manga_by_title = groupMangaByTitle(entries)
    manga_updates = groupUpdatesByTitle(entries, manga_by_title)
    
    return manga_updates

def groupAnimeByTitle(entries: List)->Dict:
    anime_by_title = {}
    for entry in entries:
        if not entry.title in anime_by_title:
            anime_by_title[entry.title] = Anime(title=entry.title,link=entry.link)
    return anime_by_title

def groupUpdatesByTitle(entries: List, anime_by_title: Dict)->Dict:
    for entry in entries:
        anime_by_title[entry.title].updates = entry.summary
    return anime_by_title

def getAnimeUpdates(rss_url: str, number_of_entries: int)->List:
    feed = feedparser.parse(rss_url)
    entries = [entry for entry in feed.entries]
    anime_by_title = groupAnimeByTitle(entries)
    anime_updates = groupUpdatesByTitle(entries, anime_by_title)
    
    return anime_updates

