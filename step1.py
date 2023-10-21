import pandas as pd

#ファイルの読み込み
video_filename = "video_file.csv"
videos = pd.read_csv(video_filename)
#print(videos)

#別のディレクトリから読み込む
video_file = "video_data.csv"
vide_dir = "test_data"
video_path = vide_dir + video_file
videos = pd.read_csv("test_data/video_data.csv")

#csvファイルへの書き込み
save_videodir = "test_data"
save_file = "new_file.csv"
file_name = save_videodir+"/"+save_file
videos = pd.read_csv(video_filename)
videos.to_csv(file_name)