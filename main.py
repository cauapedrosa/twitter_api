# key.py is the file where you'll need your API tokens
# check key.py.example for reference
import key
import tweepy

# Your twitter handle
user_screen_name = 'username'
# If tweet doesn't have X likes, delete it.
min_likes = 1


def main():
    # Setup auth
    auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_key_secret)
    auth.set_access_token(key.access_token, key.access_token_secret)
    api = tweepy.API(auth)
    # Display user info
    user = api.get_user(screen_name=user_screen_name)._json
    print('Starting to work on user: ' + user['name'] + ' (@' + user_screen_name + ')\n')

    # Gets tweets
    timelines = api.user_timeline(
        screen_name=user_screen_name, include_rts=True, count=500)

    # Iterates over tweets
    for n, status in enumerate(timelines):
        twt_list_size = len(timelines)
        tweetid = status._json['id']
        like_count = status._json['favorite_count']
        metrics = int(like_count)
        print(f'\n#{n+1}/{twt_list_size} [ID:{tweetid}] Likes: {like_count}')
        if metrics < min_likes:
            print(f'#{n+1}/{twt_list_size} [ID:{tweetid}] Deleting...  - {metrics}')
            # Uncomment the next command to enable deleting
            # api.destroy_status(tweetid)
        else:
            print(f'#{n+1}/{twt_list_size} [ID:{tweetid}] will be spared. Metrics {metrics} surpass {min_likes}')


if __name__ == "__main__":
    main()
