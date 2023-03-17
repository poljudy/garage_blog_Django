from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView)
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostVehicleForm, VehicleForm
from .forms import SparePartForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )


class Text:
    #  https://lookaway.info/zine/information/prepopulate-a-form-field-using-slugs-and-integers-django-20210410/

    def slugify_unique(model, title):
        '''
        Sourced this function as is from the link above.
        Given a DB model and a title, return a unique slug that is unique \
        to all other slug fields of the given DB model.

        Arguments
        model - Must be a Django database model that has \
                   a slug field called "slug".
        title - The string used to create the slug.

        Returns - A slug that is unique across all instances of the model.
        '''
        from django.utils.text import slugify
        slug = slugify(title)
        existing_slugs = []
        try:
            [existing_slugs.append(str(i.slug)) for i in model.objects.all()]
        except IndexError:
            print("There was no slug field found for {}".format(model))
            return slug
        if slug in existing_slugs:
            date_slug = slug + "-" + timezone.now().strftime("%Y%m%d")
            if date_slug in existing_slugs:
                long_slug = date_slug + timezone.now().strftime("%m%s")
                return long_slug
            else:
                return date_slug
        else:
            return slug


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


@login_required
def delete_post(request, post_id=None):
    post_to_delete = Post.objects.get(id=post_id)
    post_to_delete.delete()
    return HttpResponseRedirect(reverse('home'))


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def post_vehicle_view(request):
    if request.method == 'POST':
        form = PostVehicleForm(request.POST)
        if form.is_valid():
            # do something with the form data
            return render(request, 'index.html')
    else:
        form = PostVehicleForm()
    return render(request, 'PostVehicleForm.html', {'form': form})


@login_required
def post_vehicle(request):
    if request.method == 'POST':
        form = PostVehicleForm(request.POST)
        if form.is_valid():
            # do something with the form data
            return render(request, 'index.html')
    else:
        form = PostVehicleForm()
    return render(request, 'post_vehicle.html', {'form': form})


@login_required
def addVehicle(request):

    form = VehicleForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():

            vehicle = form.save(commit=False)
            vehicle.author = request.user
            vehicle.save()
            messages.success(request, 'Your vehicle post was created successfully!')  # noqa
            return HttpResponseRedirect(reverse('home'))

    else:
        form = VehicleForm()

    return render(request, 'PostVehicleForm.html', {'form': form})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title', 'excerpt', 'featured_image', 'content',
        'status', 'youtube_link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = Text.slugify_unique(self.model, form.instance.title)  # noqa
        return super().form_valid(form)


class PostUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    UpdateView
        ):
    model = Post
    fields = [
        'title', 'featured_image', 'excerpt', 'content',
        'status', 'youtube_link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = self.get_object()
        form.instance.slug = Text.slugify_unique(self.model, form.instance.title)  # noqa

#        form.instance.slug = post.slug
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_message(self, cleaned_data):
        return "%(slug)s updated successfully" % {'slug': self.object.slug}  # noqa


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        # making sure the user is the author before deleting
        if self.request.user == post.author:
            return True
        return False
