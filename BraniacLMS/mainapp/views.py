<<<<<<< HEAD
from datetime import datetime

=======
>>>>>>> master
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

<<<<<<< HEAD
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['news_title'] = 'Громкий новостной заголовок'
        # context['news_preview'] = 'Предварительное описание, которое заинтересует каждого'
        context = {
            "news_title": "Громкий новостной заголовок",
            "news_preview": "Предварительное описание, которое заинтересует каждого",
            "range": range(1, 6),
            "datetime_obj": datetime.now(),
        }
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context

=======
>>>>>>> master

class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
<<<<<<< HEAD
    template_name = "mainapp/login.html"
=======
    template_name = "mainapp/login.html"
>>>>>>> master
