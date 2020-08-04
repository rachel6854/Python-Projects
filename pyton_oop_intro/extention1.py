from string import punctuation


class YouTubeLessonManager:
    def __init__(self):
        self.lessons = {}

    def save(self, name, url):
        self.lessons[name] = url[32:]

    def get(self, name):
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


lesson_manager = YouTubeLessonManager()
lesson_manager.save("For-Loops", "https://www.youtube.com/watch?v=OnDr4J2UXSA")

print(lesson_manager.lessons["For-Loops"])  # outputs: OnDr4J2UXSA
print(lesson_manager.get("For-Loops"))
# outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA'
