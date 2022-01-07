import asyncio
import datetime

import httpx
import bs4
from colorama import Fore

# Older versions of python require calling loop.create_task() rather than on asyncio.
# Make this available more easily.
global loop

#async to make it an async 
async def get_html(episode_number: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {episode_number}", flush=True)

    url = f'https://talkpython.fm/{episode_number}'
    # same but with async block so that program can give up its execution async with block
    async with httpx.AsyncClient() as client:
        #what we are getting back here is not an answer  not the response but a task or co-routine, that when finish would give us the response
        #and the way to say make the program give up its execution to anything else that needs to run while we are waiting  and give me the answer when it's done is the the following line with await
        resp = await client.get(url, follow_redirects=True)
        resp.raise_for_status()

        return resp.text


def get_title(html: str, episode_number: int) -> str:
    print(Fore.CYAN + f"Getting TITLE for episode {episode_number}", flush=True)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return "MISSING"

    return header.text.strip()


def main():
    t0 = datetime.datetime.now()

    global loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_title_range())

    dt = datetime.datetime.now() - t0
    print(f"Done in {dt.total_seconds():.2f} sec.")


async def get_title_range_old_version():
    # Please keep this range pretty small to not DDoS my site. ;)
    for n in range(270, 280):
        html = await get_html(n)
        title = get_title(html, n)
        print(Fore.WHITE + f"Title found: {title}", flush=True)


async def get_title_range():
    # Please keep this range pretty small to not DDoS my site. ;)

    tasks = []
    for n in range(270, 280):
        tasks.append((n, loop.create_task(get_html(n))))

    for n, t in tasks:
        html = await t
        title = get_title(html, n)
        print(Fore.WHITE + f"Title found: {title}", flush=True)


if __name__ == '__main__':
    main()

# the result is much faster.
#it just about  writing the request as it should be and adding the async block before it and the await before the get call so that
#the program will leave its execution
# because most applications are waiting on something (databases,... you can do a whole lot more work)