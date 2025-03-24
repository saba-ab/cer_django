from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dataclasses import dataclass

@dataclass
class BlogDTO:
    title: str
    slug: str
    content: str
    source_url: str
    youtube_url: str
    photo_url: str
    published_at: datetime
    created_at: datetime

def fetch_blogs_from_bmg():
    url = construct_url()
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    container = soup.select_one("div.more-news-content")
    if not container:
        print("No blog container found.")
        return []

    links = container.find_all("a", href=True)
    unique_urls = {link['href'] for link in links if link['href'].startswith("https://bm.ge/news")}
    blog_urls = list(unique_urls)

    data = []

    for blog_url in blog_urls:
        try:
            blog = parse_blog(blog_url)
            data.append(blog)
        except Exception as e:
            print(f"Error parsing blog {blog_url}: {e}")

    return data


def parse_blog(blog_url: str) -> BlogDTO:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(blog_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    section = soup.select_one("div.section-news")
    if not section:
        raise ValueError("Blog section not found")

    title = section.select_one("h1.title").text.strip()

    iframe = section.select_one("iframe")
    youtube_url = iframe['src'] if iframe else ""

    img = section.select_one("img.w-full")
    photo_url = img["src"] if img else ""

    date_div = section.select_one("div.flex.items-center.gap-3.font-avenir.text-xs.text-gray-500.m-0")
    date_span = date_div.select_one("span")
    naive_published_at = datetime.strptime(date_span.text.strip(), "%d.%m.%y %H:%M")
    published_at = naive_published_at.replace(tzinfo=ZoneInfo("Asia/Tbilisi"))


    content_container = section.select_one("div.description")
    paragraphs = content_container.find_all("p")
    content = "\n\n".join(p.get_text(strip=True) for p in paragraphs)

    slug = blog_url.split("/")[-1]

    return BlogDTO(
        title=title,
        slug=slug,
        content=content,
        source_url=blog_url,
        youtube_url=youtube_url,
        photo_url=photo_url,
        published_at=published_at,
        created_at=datetime.utcnow(),
    )

def construct_url():
    """ Date format should be 2025-3-23"""
    url = "https://bm.ge/category/udzravi-qoneba?startDate={start}&endDate={end}"
    today = datetime.now().date()
    formated_date = f"{today.year}-{today.month}-{today.day-1}"


    formated_url = url.format(start=formated_date, end=formated_date)
    return formated_url