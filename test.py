import json
import requests

#url = "https://netease-cloud-music-api-azure-phi.vercel.app/playlist/track/all"
# https://dataiqs.com/api/docs/?id= 

# 网易云音乐 api
netease="https://music.cyrilstudio.top/" 

# 获取歌曲数据
def getSongUrl(id,level='standard'):
	""" 获取歌曲链接 
	Args:
		id (int): 歌曲id
		level (str): 歌曲音质
	Return:  
	"""	
	r = requests.get(netease+'song/url/v1',params={'id':id,"level":level})
	return r.json()['data'][0]['url']

# 检测歌曲是否有版权
def checkSongUrl(id):
	r = requests.get(netease+'check/music',params={'id':id},timeout=1) 
	return r.json()['success']

# 	# fee: enum,
# 	#   0: 免费或无版权
# 	#   1: VIP 歌曲
# 	#   4: 购买专辑
# 	#   8: 非会员可免费播放低音质,会员可播放高音质及下载
# 	#   fee 为 1 或 8 的歌曲均可单独购买 2 元单曲 
# 	# 1499519826 无版权
# 	# 1888354230 vip 
# 	# 2114161073 免费


# 获取歌单全部歌曲信息
def getPlaylistDetail(id):
	r = requests.get(netease+'playlist/track/all',params={'id':id},timeout=1) 
	songlist = {'nofee':[],'hasfee':{'novip':[],'vip':[]}}	 
	for song in r.json()['songs']: 
		data = {"id":song['id'],"name":song['name'],"singer":song['ar'][0]['name'],"fee":song['fee']}
		if(checkSongUrl(song['id'])):
			if(song['fee']==0): 
				data['url'] = getSongUrl(song['id'],'jymaster')
				songlist['hasfee']['novip'].append(data)
			else: songlist['hasfee']['vip'].append(data)
		else:
			songlist['nofee'].append(data) 
	return songlist

# 下载音乐
def download(singer,name,url):
	if(url.json()['code']!=404):
		print('正在下载',name)
		open('./%s - %s.mp3'%(singer,name),'wb').write(url.content)
		print('下载完成',name)
		return False
	else:
		print('音源不存在，无法下载')
		return True
	...


def main(playlistID):
	songlist = getPlaylistDetail(playlistID)
	# for song in songlist['hasfee']['novip']:
	# 	download(song['singer'],song['name'],song['url'])
	song = songlist['hasfee']['novip'][0]
	download(song['singer'],song['name'],song['url'])


playlist_id = 464327584  	
main(playlist_id)
# print(getSongData(2114161073))
# print(isFreeSong(2114161073))  
# print(getPlaylistDetail(playlist_id))	
# if(r.status_code==200): 
# 	music = r.json()['songs'][0] 
# 	print(music)
