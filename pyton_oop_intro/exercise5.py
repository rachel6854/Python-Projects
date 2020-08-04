from string import punctuation

class YouTubeLessonManager:
    def __init__(self):
        self.lessons = {}

    def save(self, name, url):
        self.lessons[name] = url

    def get(self, name):
        [name.replace(p, '-') for p in punctuation]
        return self.lessons.get(name.title(), "")


lesson_manager = YouTubeLessonManager()

lesson_manager.save("For-Loops", "https://www.youtube.com/watch?v=OnDr4J2UXSA")

print(lesson_manager.get("for-loops"))  # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA'

print(lesson_manager.get("fOr-LooPS"))  # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA'﻿
