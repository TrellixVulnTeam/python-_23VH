import Algorithmia

input = {
  "image": "data://gimmy/mlbook/thumb2.jpg",
  "outputUrl": "data://.algo/util/SmartImageDownloader/temp/5_mapped.png",
  "height": 80,
  "width": 80
}
try:
    client = Algorithmia.client('simNzAsHiHWn3zWnktx4UBG8mLO1')
    algo = client.algo('opencv/SmartThumbnail/2.2.2')
    print(algo.pipe(input).result)
except:
    print('資料圖片檔案讀取錯誤！')
