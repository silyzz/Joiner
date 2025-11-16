import asyncio
import threading
import time

from discord import listener
from src.roblox import roblox_main





if __name__ == "__main__":
    print("Roblox AutoJoiner for Chilli's Notify by vortaz")
    
    

    
    print("Version: 1.1.2")
    print("Starting in 2 seconds...")
    print()

    # убирая мое авторство вы нарушаете лицензию (читай LICENSE.md)
    # By removing my authorship, you are violating the license (read LICENSE.md)
    

    time.sleep(2)

    threading.Thread(target=roblox_main, daemon=True).start()
    asyncio.run(listener())
