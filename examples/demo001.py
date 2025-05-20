from tzafon import Waypoint
from dotenv import load_dotenv
import os

load_dotenv()

client = Waypoint(token=os.getenv("WAYPOINT_TOKEN"))

image_path = "screenshot.jpg"


async def main():
    async with client:
        await client.goto("https://www.tzafon.ai")

        # Get URL to image
        url = await client.screenshot(return_url=True)
        print("Image url:", url)

        # Save image to file
        await client.screenshot(path=image_path)
        print("Image saved to:", image_path)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
