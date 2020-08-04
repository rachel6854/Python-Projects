from string import punctuation


class YouTubeLessonManager:
    def __init__(self):
        self.lessons = {}

    def save(self, name, url):
        self.lessons[name] = url

    def get(self, name):
        [name.replace(p, '-') for p in punctuation]
        ret = self.lessons.get(name.title(), "")
        if ret == "":
            ret = []
            for n, u in self.lessons.items():
                if name.title() in n.split("-"):
                    ret.append(u)
        return ret


lesson_manager = YouTubeLessonManager()

lesson_manager.save("For-Loops", "https://www.youtube.com/watch?v=OnDr4J2UXSA")
lesson_manager.save("While-Loops", "https://www.youtube.com/watch?v=6TEGxJXLAWQ")
lesson_manager.save("Functions", "https://www.youtube.com/watch?v=NSbOtYzIQI0")
lesson_manager.save("Dictionaries", "https://www.youtube.com/watch?v=ZEZdys-fHDw")

# print(lesson_manager.get("for loops"))  # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA'﻿

print(lesson_manager.get("for"))  # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA'﻿﻿

print(lesson_manager.get(
    "loops"))  # outputs ['https://www.youtube.com/watch?v=OnDr4J2UXSA', 'https://www.youtube.com/watch?v=6TEGxJXLAWQ']﻿
