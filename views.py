from django.http import HttpResponse

def index(request):
    """Главная страница Yatube"""
    return HttpResponse(
        "<h1 style='color: #2c3e50;'>Добро пожаловать в Yatube!</h1>"
        "<p>Yatube — это социальная сеть для публикации постов.</p>"
        "<p>Здесь вы можете делиться своими мыслями и находить друзей.</p>"
        "<hr>"
        "<h2>Последние посты:</h2>"
        "<ul>"
        "<li>Мой первый пост в Yatube! 🎉</li>"
        "<li>Как я изучаю Django</li>"
        "<li>10 причин любить Python</li>"
        "</ul>"
    )

def group_posts(request, slug):
    """Страница постов, отфильтрованных по группам"""
    return HttpResponse(
        f"<h1 style='color: #3498db;'>Сообщество: {slug}</h1>"
        f"<p>Здесь будут посты из группы <strong>{slug}</strong></p>"
        "<hr>"
        "<h2>Посты сообщества:</h2>"
        "<ul>"
        f"<li>Первый пост в сообществе {slug}</li>"
        f"<li>Как я вступил в группу {slug}</li>"
        f"<li>Полезные советы для {slug}</li>"
        "</ul>"
        "<p><a href='/'>← Вернуться на главную</a></p>"
    )