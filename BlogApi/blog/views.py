from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post,Tag,PostTagRelation
from rest_framework import viewsets, generics
from blog.serializers import UserSerializer, GroupSerializer , PostSerializer, TagSerializer ,PostTagRelationSerializer

from django.db.models import Q

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDescViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-pk")
    serializer_class = PostSerializer

# class ShowPostById(APIView):
#     def post(self,request):
#         # return Response("Posted ")
#         # queryset = Post.objects.all()
#         user_id = request.POST.get('user_id')
#         # id  = str(user_id)
#         print('user_id     ',user_id)
#
#         # return Response(" provide an user_id ")
#         if user_id :
#             queryset = Post.objects.filter(user_id=user_id)
#
#             # serializer_class = PostSerializer
#             viewsets.ModelViewSet.serializer_class = PostSerializer
#             return Response(queryset)
#         else :
#             return Response("Please provide an user_id ")

class ShowPostById(ListAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        queryset_list = Post.objects.all()
        query = self.request.POST.get('user_id')
        print("querry : ",query)
        queryset_list = queryset_list.filter(Q(user_id=query)).order_by("-post_id")
        return queryset_list

class ShowPostByTagId(ListAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        queryset_list = Post.objects.all()

        query = int(self.request.POST.get('tag_id'))
        print("querry : ",query)
        posttagrelation = PostTagRelation.objects.all().filter(id_tag=query)
        ids = []
        for x in posttagrelation:
            ids.append(x.id_post)

            # print(x)
            # queryset_list = Post.objects.get(post_id=x.id_post)
            # return queryset_list
        print("matching posts : ", ids)

        queryset_list = Post.objects.all().filter(post_id__in=ids)
        return queryset_list

# def search(request):
#     user_list = User.objects.all()
#     user_filter = Post(request.GET, queryset=user_list)
#
#     return render(request, 'search/user_list.html', {'filter': user_filter})




class FindPosts(generics.ListAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        queryset = Post.objects.all()
        username = self.request.POST.get('username')
        print("Search : ",username)
        for x in queryset:
            if username in x.post_name:
                # print ("result :",x.post_name)
                queryset = queryset.filter(post_name=x.post_name)
        return queryset

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class AddPost(APIView):
    def get(self, request):
        content = {'message': 'Hello, World! this is a get request'}
        return Response(content)

    def post(self,request,*args, **kwargs):
        try:
            user_id = request.POST.get('id')
            # user_id = token.user_id
            txtpost = request.POST.get('post')
            txtdesc = request.POST.get('desc')
            tag = request.POST.get('tag')

            if user_id:
                if txtpost:
                    if txtdesc:
                        # objuser = User.objects.get()
                        post_id = Post.objects.latest('post_id').post_id
                        post_obj = Post.objects.create(user_id=user_id, post_name=txtpost, post_description=txtdesc, post_tag_id=tag)


                        # post_id = query
                        print("Post id : ",post_id)
                        items = tag.split(',')
                    # try:
                        for item in items:
                            tag_id =  Tag.objects.get(tag_name=item).id
                            print('tag_id :',tag_id)
                            # tag_obj = PostTagRelation.objects.create(post_id=int(post_id), tag_id=int(tag_id))
                            tag_obj = PostTagRelation.objects.create(id_post=post_id+1,id_tag=tag_id)
                            tag_obj.save()
                            print("saved : Postid ",post_id," tagid : ",tag_id)

                        post_obj.save()
                        print("saved new post")

                    # except Exception as e:
                    #     print("error :",e)

                        return Response({
                            'user_id': user_id,
                            'post_name': txtpost,
                            'post_description': txtdesc,
                            # 'post_tag_id':tag,
                        })
                        # return Response("Record inserted")
                    else:
                        return HttpResponse("need desc")
                else:
                    return HttpResponse("name of post")
            else:
                return HttpResponse("need id")

        except Exception as e:
            # return JsonResponse(e)
            return HttpResponse(e )