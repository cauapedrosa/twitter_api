# key.py is the file where you'll need your API tokens
# check key.py.example for reference
import key
import tweepy

# Your twitter handle
user_screen_name = 'username'
# If tweet doesn't have X or more likes, delete it.
min_likes = 1


def main():
    # Setup auth
    auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_key_secret)
    auth.set_access_token(key.access_token, key.access_token_secret)
    api = tweepy.API(auth)
    # Display user info
    user = api.get_user(screen_name=user_screen_name)._json
    print('\nTweet Deleter v1\nStarting to work on user: ')
    print(user['name'] + ' (@' + user_screen_name + ')\n')

    # Gets tweets
    timelines = api.user_timeline(
        screen_name=user_screen_name, include_rts=True, count=500)

    # Iterates over tweets
    for n, status in enumerate(timelines):
        len_twts = len(timelines)
        # Extracts tweet json
        tweet = status._json
        twt_id = tweet['id']
        twt_metrics = int(tweet['favorite_count'])
        twt_content = tweet['text']
        
        print(f'\n#{n+1}/{len_twts} - ID:{twt_id} Metrics of {twt_metrics}')
        print(f'Content: "' + twt_content +'"')
        if twt_metrics < min_likes:
            print(f'#{n+1}/{len_twts} - ID:{twt_id} will be deleted. Metrics {twt_metrics} is less than {min_likes}')
            # Uncomment the next command to enable deleting. Leave it commented to perform a test run.
            # api.destroy_status(twt_id)
        else:
            print(f'#{n+1}/{len_twts} - ID:{twt_id} will be spared. Metrics {twt_metrics} is greater than {min_likes}')


if __name__ == "__main__":
    main()
