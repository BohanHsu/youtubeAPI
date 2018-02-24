# -*- coding: utf-8 -*-

import io


import youtube_code as youtube
import youtube_video_code as youtube_video
import youtube_search_code as youtube_search
import paths as path

parts = 'snippet,contentDetails,statistics'

#search_keyword = "facebook"
def main(search_keyword):
  max_result = 10
  service = youtube.get_authenticated_service()
  video_ids = youtube_search.youtube_search(service, {'q': search_keyword, 'max_results': max_result})
  videos = youtube_video.videos_list_multiple_ids(service, part=parts, id=video_ids)
  return videos


def handle_videos(videos):
  results = {}
  for p in path.paths:
    results[p] = []

  for video in videos['items']:
    plain_result = handle_video_result(video)
    for p in path.paths:
      if p in plain_result:
        results[p].append(plain_result[p])
      else:
        results[p].append('')

  return results

def result_to_csv(results):
  csv = []
  titles = ['id'] + sorted(path.paths)

  string = u""
  for title in titles:
    string += title
    string += ","

  string = string[:-1]
  string = string.encode('utf-8')
  string = string + "\n"
  csv.append(string)
  
  count = 0
  while count < len(results['id']):
    string = ""
    for title in titles:
      #print results[title][count]
      string += results[title][count]
      string += ","

    string = string[:-1]
    string = string.encode('utf-8')
    string = string + "\n"
    csv.append(string)
    count += 1

  return csv


  str = ""

def handle_video_result(video):
  plain_video = {}
  for p in path.paths:
    path_array = p.split('.')
    item = None
    i = 0
    current_result = video
    while i < len(path_array):
      key = path_array[i]
      if not (type(current_result) is dict) or not (key in current_result):
        current_result = ''
        break

      current_result = current_result[key]
      i += 1

    if not (type(current_result) is dict):
      if type(current_result) is list:
        plain_video[p] = ','.join(map(lambda x: str(x.encode('utf-8', 'ignore')), current_result))
      else:
        #if type(current_result) is str:
        if type(current_result) is bool:
          current_result = str(current_result)

        current_result = current_result.encode('utf-8', 'ignore').strip()
        plain_video[p] = current_result

    else:
      print 'remove!', p

  for k in plain_video:
    plain_video[k] = handle_string(plain_video[k])

  return plain_video

def handle_string(string):
  string = string.replace('"', "'")
  string = string.replace("\n", " ")
  string = '"' + string + '"'
  string = unicode(string, errors="ignore")
  string = string.encode('utf-8')
  return string

def write_csv(filename, csv):
  f = open(filename + ".csv", "w+")
  f.writelines(csv)
  f.close()

def handle_filename(filename):
  a = ord('a')
  z = ord('z')
  A = ord('A')
  Z = ord('Z')
  c0 = ord('0')
  c9 = ord('9')

  filename = list(filename)

  for i in range(len(filename)):
    cr = ord(filename[i])
    if cr <= z and cr >= a or cr <= Z and cr >= A or cr <= c9 and cr >= c0:
      #filename[i] = cr
      pass
    else:
      filename[i] = '_'

  return "".join(filename)




if __name__ == '__main__':
  search_keyword = "honda civic'9"
  youtube_result = main(search_keyword)

  result = handle_videos(youtube_result)
  csv = result_to_csv(result)

  for string in result['id']:
    print string

  print len(csv)
  write_csv(handle_filename(search_keyword), csv)

