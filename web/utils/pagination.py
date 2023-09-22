#!usr/env/python3
# -*- coding: utf-8 -*-

"""
# File       : pagination.py
# Time       : 2023/2/27 20:31
# Author     : Ron
# version    : python 3.9
# software   : Pycharm
# Description：自定义分页组件
以后如果想要使用这个分页组件，你需要做如下几件事：

在视图函数中：
    def pretty_list(request):

        # 1.根据自己的情况去筛选自己的数据
        queryset = models.PrettyNum.objects.all()

        # 2.实例化分页对象
        page_object = Pagination(request, queryset)

        context = {
            "queryset": page_object.page_queryset,  # 分完页的数据
            "page_string": page_object.html()       # 生成页码
        }
        return render(request, 'pretty_list.html', context)

在HTML页面中

    {% for obj in queryset %}
        {{obj.xx}}
    {% endfor %}

    <ul class="pagination">
        {{ page_string }}
    </ul>
"""
from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, request, page_queryset, plus=5, page_size=10, page_param="page"):
        """
        :param request: 请求的对象
        :param page_queryset: 符合条件的数据（根据这个数据进行分页处理）
        :param plus:显示当前页的后几页
        :param page_size: 每页显示多少条数据
        :param page_param: 在URL中传递的获取分页的参数，例如： /num/list/?page=1
        """

        import copy
        # from django.http.request import QueryDict
        query_dict = copy.deepcopy(request.GET)
        # print(type(query_dict))
        query_dict._mutable = True

        self.query_dict = query_dict

        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page_param = page_param
        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.plus = plus

        self.page_queryset = page_queryset[self.start: self.end]

        # 数据总条数
        total_count = page_queryset.count()
        # 总页码
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1

        self.total_page_count = total_page_count

    def html(self):
        # 显示当前页的前五页及后五页
        # 数据库中数据较少，都没有达到11页
        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count + 1

        else:
            # 数据库中数据较多，> 11页

            # 当前页<5时（小的极值）
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页>5
                # 当前页+5 > 总页码
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus + 1

        # 页码
        page_str_list = []  # 首先创建一个空的页码列表，用来存储页码

        self.query_dict.setlist(self.page_param, [1])
        # 首页
        page_str_list.append('<li class="page-item"><a class="page-link" href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))

        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li class="page-item"><a class="page-link" href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li class="page-item"><a class="page-link" href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())  # 如果当前页面为1，则无法再往上翻页
        page_str_list.append(prev)

        # 页面
        for i in range(start_page, end_page):
            if i == self.page:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li class="page-item active"><a class="page-link" href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li class="page-item"><a class="page-link" href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            next_page = '<li class="page-item"><a class="page-link" href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            next_page = '<li class="page-item"><a class="page-link" href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(next_page)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li class="page-item"><a class="page-link" href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))

        search_string = """
                <li>
                    <form method="get" style="float: left; margin-left: 5px">
                        <input type="text" class="form-control" placeholder="页码" name="page"
                               style="width: 250px;position: relative;display: inline-block;">
                        <button class="btn btn-info" type="submit">跳转</button>
                    </form>
                </li>
            """
        page_str_list.append(search_string)
        # 给页码进行安全标记
        page_string = mark_safe("".join(page_str_list))

        return page_string
