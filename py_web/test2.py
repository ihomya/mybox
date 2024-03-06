from pycloudmusic import Music163Api
import asyncio


async def main():
    musicapi = Music163Api()
    # 获取歌单 7487291782
    # https://music.163.com/#/playlist?id=7487291782
    playlist = await musicapi.playlist(464327584)
    # 打印歌单信息
    print(playlist.music_list[0])
    print("=" * 50)

    # 打印歌单曲目
    
       # print(music.name, music.artist_str, music.id)
        #print(music)
    # 创建任务
    tasks = [asyncio.create_task(music.play()) for music in playlist]
    # 等待任务
    await asyncio.wait(tasks)

asyncio.run(main())