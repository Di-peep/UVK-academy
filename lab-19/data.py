import datetime


posts_data = [
    {
        "title": "My first post",
        "text": "Hello, my dear subscribers. Welcome to my blog. And bla-bla-bla..",
        "date": datetime.datetime(2023, 1, 1),
        "tags": ["daily"],
        "like_counter": 10,
        "comments": [
            {
                "nickname": "Randy",
                "comment": "cool!",
                "date": datetime.datetime(2023, 1, 1)
            }
        ]
    },
    {
        "title": "My second post",
        "text": "text-text-text, Mongo-mongo-Mongo",
        "date": datetime.datetime(2023, 1, 2),
        "tags": ["daily", "mongo"],
        "like_counter": 23,
        "comments": [
            {
                "nickname": "Randy",
                "comment": "cool!",
                "date": datetime.datetime(2023, 1, 2)
            },
            {
                "nickname": "Weirny",
                "comment": "Gratz :0",
                "date": datetime.datetime(2023, 1, 3)
            }
        ]
    },
    {
        "title": "My third post about news",
        "text": "news-news-news, sql-SQL-sql",
        "date": datetime.datetime(2023, 1, 3),
        "tags": ["news", "sql"],
        "like_counter": 14,
        "comments": [
            {
                "nickname": "Weirny",
                "comment": "I love SQL",
                "date": datetime.datetime(2023, 1, 3)
            },
            {
                "nickname": "Randy",
                "comment": "Gratz :0",
                "date": datetime.datetime(2023, 1, 4)
            }
        ]
    }
]

users_data = [
    {
        "nickname": "Randy",
        "email": "random@gmail.com"
    },
    {
        "nickname": "Weirny",
        "email": "weird@gmail.com"
    }
]
