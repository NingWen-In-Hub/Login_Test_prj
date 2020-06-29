import logging
# 　画面に表示するメッセージ用
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy
from django.views import generic

from login_test_app.forms.forms import *
from login_test_app.forms.forms2 import NewForm2 as NewForm2_2
from login_test_app.forms.forms3 import NewForm2 as NewForm3_2
from .models import Profile, UserSpecies
from accounts.models import CustomUser

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    # form_class = AddForm
    # form_class = NewForm3_2
    success_url = reverse_lazy('login_test_app:inquiry')  # 送信成功した遷移先

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'success：メッセージを送信しました。')
        # settings_common MESSAGE_TAGSに記述
        messages.info(self.request, 'info:メッセージを送信しました。')
        messages.error(self.request, 'error:メッセージを送信しませんでした（うそ）')
        messages.warning(self.request, 'warning:メッセージを送信チャいました。')
        # ログ出力
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


#  ログインリクエスト
class ProfileView(LoginRequiredMixin, generic.ListView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'member_list'
    # paginate_by = 2  # いらないけど

    def get_queryset(self):
        # 「object.get」はデータがない場合エラーが出るので「.first」を使う
        profiles = Profile.objects.filter(user=self.request.user).order_by('created_at').first()
        logger.info('User A= {}'.format(profiles))
        return profiles

    '''def get_profile(self):
        # 一つのデータを探す
        profiles = Profile.objects.get(user=self.request.user)
        logger.info('User A= {}'.format(profiles))
        return profiles'''

    """def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        profiles = Profile.objects.all()
        context['profiles'] = profiles

        return context"""


class ProfileCreateView(LoginRequiredMixin, generic.CreateView):
    """プロフィール作成"""
    model = Profile
    template_name = 'profile_create.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('login_test_app:profile')

    def form_valid(self, form):  # バリデーション成功
        # 元々のソース
        """
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        messages.success(self.request, 'プロフィール作成しました。')
        """
        form = form_save(self.request, form, 'プロフィール作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新が失敗しました。")
        return super().form_invalid(form)


class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    """プロフィール編集"""
    model = Profile
    # slug_url_kwarg = "id"
    # slug_field =
    template_name = 'profile_edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('login_test_app:profile')

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)

        my_data = get_object_or_404(Profile, user=self.request.user)
        edit_data = self.kwargs['pk']
        logger.info("\n編集のユーザー：{}\nログインユーザー：{}".format(edit_data, my_data.id))
        if my_data.id != edit_data:
            logger.error("自分のプロフィールではない！！！")
            raise PermissionDenied

        # form_kwargs['initial'] = {'test2': my_data.species}
        return form_kwargs

    def form_valid(self, form):
        # 元々のソース
        form = form_save(self.request, form, 'プロフィール更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新が失敗しました。")
        return super().form_invalid(form)



def form_save(request, form, messages_success):
    profile = form.save(commit=False)

    # profile.species = form.cleaned_data['test2']

    profile.user = request.user
    profile.save()
    messages.success(request, messages_success)
    return form


def MyView403(request):
    raise PermissionDenied


def MyView500(request):
    raise Exception


class UserListView(LoginRequiredMixin, generic.ListView):
    model = Profile
    template_name = 'user_list.html'
    context_object_name = 'member_list'
    paginate_by = 6

    def get_queryset(self):
        profiles = Profile.objects.order_by('updated_at')
        return profiles

class UserListAView(LoginRequiredMixin, generic.ListView):
    model = CustomUser
    template_name = 'user_listA.html'
    context_object_name = 'member_list'
    paginate_by = 6

    def get_queryset(self):
        users = CustomUser.objects.order_by('last_login')
        return users


class UserListBView(LoginRequiredMixin, generic.ListView):
    model = CustomUser
    template_name = 'user_listB.html'
    context_object_name = 'member_list'
    paginate_by = 6

    def get_queryset(self):
        users = CustomUser.objects.prefetch_related('p_names').order_by('last_login')
        # users = CustomUser.objects.profile_set.all()
        logger.info(users)
        return users
