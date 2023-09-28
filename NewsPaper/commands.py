
# >>> from news.models import *
# >>> u1 = User.objects.create_user(username='Andrey')
# >>> u1
# <User: Andrey>
# >>> u2 = User.objects.create_user(username='Vitala')
# >>> u2
# <User: Vitala>
# >>> u1
# <User: Andrey>
# >>> Author.objects.create(authorUser=u1)
# <Author: Author object (1)>
# >>> u1
# <User: Andrey>
# >>> Author.objects.create(authorUser=u2)
# <Author: Author object (2)>


# >>> Category.objects.create(name='IT')
# <Category: Category object (1)>
# >>> Category.objects.create(name='Russia')
# <Category: Category object (2)>
# >>> Category.objects.create(name='Football')
# <Category: Category object (3)>
# >>> Category.objects.create(name='World')
# <Category: Category object (4)>


# >>> author = Author.objects.get(id=1)
# >>> author
# <Author: Author object (1)>
# >>> author_2 = Author.objects.get(id=2)
# >>> author_2
# <Author: Author object (2)>


# >>> Post.objects.create(author=author, categoryType='NW', title='sometitle', text='somebigtext')
# <Post: Post object (1)>
# >>> Post.objects.create(author=author, categoryType='AR', title='Databse', text='База данных — это место для хранения данных')
# <Post: Post object (2)>
# >>> Post.objects.create(author=author_2, categoryType='AR', title='Europe championship 2024', text='17-й розыгрыш чемпионата Европы по футболу, футбольного ту
# рнира')
# <Post: Post object (3)>

# >>> Post.objects.get(id=1).title
# 'sometitle'
# >>> Post.objects.get(id=2).title
# 'Databse'
# >>> Post.objects.get(id=3).title
# 'Europe championship 2024'

# >>> Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
# >>> Post.objects.get(id=1).postCategory.add(Category.objects.get(id=4))
# >>> Post.objects.get(id=2).postCategory.add(Category.objects.get(id=1))
# >>> Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
# >>> Post.objects.get(id=3).postCategory.add(Category.objects.get(id=3))
# >>> Post.objects.get(id=3).postCategory.add(Category.objects.get(id=3))
# >>> Post.objects.get(id=3).postCategory.add(Category.objects.get(id=2))

# >>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='Good job')
# <Comment: Comment object (1)>
# >>> Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser, text='nice')
# <Comment: Comment object (2)>
# >>> Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=1).authorUser, text='perfect')
# <Comment: Comment object (3)>
# >>> Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=1).authorUser, text='Good')
# <Comment: Comment object (4)>


# >>> Post.objects.get(id=1).like()
# >>> Post.objects.get(id=1).rating
# 1
# >>> Post.objects.get(id=1).like()
# >>> Post.objects.get(id=1).like()
# >>> Post.objects.get(id=1).like()
# >>> Post.objects.get(id=2).like()
# >>> Post.objects.get(id=2).like()
# >>> Post.objects.get(id=3).like()
# >>> Post.objects.get(id=3).like()
# >>> Post.objects.get(id=3).like()

# >>> Comment.objects.get(id=1).dislike()
# >>> Comment.objects.get(id=2).like()
# >>> Comment.objects.get(id=3).like()
# >>> Comment.objects.get(id=3).like()
# >>> Comment.objects.get(id=4).dislike()
# >>> Comment.objects.get(id=4).dislike()

# >>> a = Author.objects.get(id=1)
# >>> a.update_rating()
# >>> a.ratingAuthor
# 17

# >>> b = Author.objects.get(id=2)
# >>> Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).authorUser, text='Very good')
# <Comment: Comment object (5)>
# >>> b.update_rating()'
# >>> b.ratingAuthor
# 9


# >>> a = Author.objects.order_by('-ratingAuthor')[:1]
# >>> a
# <QuerySet [<Author: Author object (1)>]>
# >>> a = Author.objects.order_by('-ratingAuthor')
# >>> a
# <QuerySet [<Author: Author object (1)>, <Author: Author object (2)>]>


# >>> for i in a:
# ...     i.ratingAuthor
# ...     i.authorUser.username
# ...
# 17
# 'Andrey'
# 9
# 'Vitala'
# >>>
