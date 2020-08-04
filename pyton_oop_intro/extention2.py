from collections import defaultdict
from string import punctuation


class YouTubeLessonManager:
    count = defaultdict(int)

    def __init__(self):
        self.lessons = {}

    def save(self, name, url):
        self.lessons[name] = url[32:]

    def get(self, name):
        self.count[name] += 1
        [name.replace(p, '-') for p in punctuation]
        ret = self.lessons.get(name.title(), "")
        if ret != "":
            return "https://www.youtube.com/watch?v=" + ret
        else:
            ret = []
            for n, u in self.lessons.items():
                if name.title() in n.split("-"):
                    ret.append("https://www.youtube.com/watch?v=" + u)
        return ret

    def get_counts(self, name):
        return self.count.get(name, 0)


lesson_manager = YouTubeLessonManager()
lesson_manager.save("For-Loops", "https://www.youtube.com/watch?v=OnDr4J2UXSA")

lesson_manager.get("For-Loops")
lesson_manager.get("For-Loops")
lesson_manager.get("Dictionaries")
lesson_manager.get("For-Loops")
lesson_manager.get("Dictionaries")

print(lesson_manager.get_counts('For-Loops'))  # outputs: 3
print(lesson_manager.get_counts('Dictionaries'))  # outputs: 2 ﻿
