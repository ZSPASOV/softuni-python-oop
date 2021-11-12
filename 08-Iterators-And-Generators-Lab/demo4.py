class TwitterPostsReader:
    def __init__(self, twitter_handle):
        self.twitter_handle = twitter_handle
        self.current_page = 1

    def __iter__(self):
        return self

    def __next__(self):
        pages = 5
        for page in range(pages):
            url = 'https://api.twitter.com/JordanJambazov/posts?page={'
            posts_on_page = self.__get_posts()
            return posts[0]

        def __get_posts()
            return [
                {'text': 'lorem'},
                {'text': 'lorem'},
                {'text': 'lorem'},
                {'text': 'lorem'},
            ]


ts_jordan = get_all_posts('JordanJambazov')