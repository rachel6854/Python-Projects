class YouTubeLessonManager:
    def __init__(self):
        self.lessons={}
    def save(self,name,url):
        self.lessons[name]=url
    def get(self,name):
        return self.lessons.get(name,"")


lesson_manager = YouTubeLessonManager()

lesson_manager.save("For-Loops", "https://www.youtube.com/watch?v=OnDr4J2UXSA")
print(lesson_manager.get("For-Loops")) # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA'