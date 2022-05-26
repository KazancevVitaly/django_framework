from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['news_title'] = 'Громкий новостной заголовок'
        # context['news_preview'] = 'Предварительное описание, которое заинтересует каждого'
        context = {
            'news_title': 'Громкий новостной заголовок',
            'news_preview': 'Предварительное описание, которое заинтересует каждого',
            'range': range(5)
        }
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"