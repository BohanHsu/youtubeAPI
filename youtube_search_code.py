# -*- coding: utf-8 -*-

# This sample executes a search request for the specified search term.
# Sample usage:
#   python geolocation_search.py --q=surfing --location-"37.42307,-122.08427" --location-radius=50km --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse

# options must contains q and max_results
def youtube_search(service, options):

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = service.search().list(
    q=options['q'],
    type='video',
    part='id,snippet',
    maxResults=options['max_results']
  ).execute()

  search_videos = []

  # Merge video ids
  for search_result in search_response.get('items', []):
    search_videos.append(search_result['id']['videoId'])
  video_ids = ','.join(search_videos)

  return video_ids

  # There is another function for that job, comment out those things
  ## Call the videos.list method to retrieve location details for each video.
  #video_response = service.videos().list(
  #  id=video_ids,
  #  part='snippet, recordingDetails'
  #).execute()

  #videos = []

  ## Add each result to the list, and then display the list of matching videos.
  #for video_result in video_response.get('items', []):
  #  videos.append('%s, (%s,%s)' % (video_result['snippet']['title'],
  #                            video_result['recordingDetails']['location']['latitude'],
  #                            video_result['recordingDetails']['location']['longitude']))

  #print 'Videos:\n', '\n'.join(videos), '\n'


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--q', help='Search term', default='Google')
  #parser.add_argument('--location', help='Location', default='37.42307,-122.08427')
  #parser.add_argument('--location-radius', help='Location radius', default='5km')
  parser.add_argument('--max-results', help='Max results', default=25)
  args = parser.parse_args()

  try:
    youtube_search({'q': args.q, 'max_results': args.max_results})
  except HttpError, e:
    print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
