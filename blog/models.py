from django.db import models


class PortfolioPage(models.Model):
    name = models.CharField(max_length=50, verbose_name='Portfolio nomi')
    about = models.TextField(verbose_name='Portfolio haqida')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'PortfolioPage'
        managed = True
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'


class PortfolioManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')


class PortfolioPost(models.Model):
    OPTIONS = (
        ('deactive','deactive'),
        ('active','active'),
    )
    photo = models.ImageField(upload_to='portfolio/', verbose_name='Post rasmi')
    about = models.TextField(verbose_name = "Post haqida qisqacha ma'lumot")
    name = models.CharField(max_length=50, verbose_name='Post nomi')
    data = models.DateField(verbose_name="Post qo'yilgan sanasi")
    status = models.CharField(max_length=50,choices=OPTIONS, verbose_name='Post holati', default='deactive')

    objects = models.Manager()
    manager_objects = PortfolioManager()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'PortfolioPost'
        managed = True
        verbose_name = 'Portfolio posti'
        verbose_name_plural = 'Portfolio posti'


class StatisticsPage(models.Model):
    works_completed = models.IntegerField(default=0, verbose_name='Loyihalar soni') 
    years_of_experience = models.IntegerField(default=0, verbose_name='Yillik tajribasi')
    total_clients = models.IntegerField(default=0, verbose_name='Mijozlar soni')
    award_won = models.IntegerField(default=0, verbose_name='Mukofotlar soni')

    def __str__(self):
        return f"{self.works_completed}"
    
    class Meta:
        db_table = 'Statistics_Page'
        managed = True
        verbose_name = 'Statistikalar'
        verbose_name_plural = 'Statistikalar'    



class ServicesPageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')


class ServicesPage(models.Model):
    OPTIONS = (
        ('deactive', 'deactive'),
        ('active','active'),
    )


    ICON = (
        ('ion-monitor','Web Design'),
        ('ion-code-working','Web Development'),
        ('ion-camera','Photography'),
        ('ion-android-phone-portrait','Responsive Design'),
        ('ion-paintbrush','Graphic Design'),
        ('ion-stats-bars','Marketing Services'),
    )

    icon = models.ImageField(choices=ICON, verbose_name='Logo')
    name = models.CharField(max_length=255, verbose_name='Nomi')
    about = models.TextField(verbose_name='Haqida')
    status = models.CharField(max_length=50, choices=OPTIONS, default='deactive')

    objects = models.Manager()
    manager = ServicesPageManager()


    def __str__(self):
        return self.name
    

    class Meta:
        db_table = 'Services_Pages'
        managed = True
        verbose_name = 'Xizmatlar'
        verbose_name_plural = 'Xizmatlar'



class TeamPageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')
    

class TeamPage(models.Model):

    OPTIONS = (
        ('deactive', 'deactive'),
        ('active', 'active'),
    )

    photo = models.ImageField(upload_to='team/', verbose_name='Rasmi')
    name = models.CharField(max_length=50, verbose_name='Ism familiyasi')    
    about = models.TextField(verbose_name='Haqida')
    status = models.CharField(max_length=50, choices=OPTIONS, default='deactive', verbose_name='Post holati')

    objects = models.Manager()
    manager = TeamPageManager()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Team_page'
        managed = True
        verbose_name = 'Jamoa'
        verbose_name_plural = 'Jamoa'
    

class AboutMePage(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ism familiya")
    profile = models.CharField(max_length=250, verbose_name='Mutaxasisligi')
    email = models.EmailField(max_length=250, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Telefon raqami')
    photo = models.ImageField(upload_to='me/', verbose_name='Rasmi')
    content = models.TextField(verbose_name='Haqida')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'About_Me_Page'
        managed = True
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchi'


class Skill(models.Model):
    name = models.CharField(max_length=50)
    percent = models.IntegerField(default=0, null=True, verbose_name='Foiz')
    about_id = models.ForeignKey(AboutMePage, on_delete=models.CASCADE, related_name='Skill')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Skill'
        managed = True
        verbose_name = 'Mahorat'
        verbose_name_plural = 'Mahorat'
    
    

class MessagePage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Message_Page'
        managed = True
        verbose_name = 'Xabarlar'
        verbose_name_plural = 'Xabarlar'
    


class BlogDetailPageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')    


class BlogDetailPage(models.Model):
    OPTIONS = (
        ('active','active'),
        ('deactive','deactive'),
    )

    photo = models.ImageField(upload_to='blog/', verbose_name='Post rasmi')
    name = models.CharField(max_length=250, verbose_name='Post nomi')
    content = models.TextField(verbose_name="Post haqida qisqacha ma'lumot")
    about = models.TextField(verbose_name="Post haqida to'liq ma'lumot")
    user_photo = models.ImageField(upload_to='blog/', verbose_name='Foydalanuvchi rasmi')
    user_fullname = models.CharField(max_length=50, verbose_name="Foydalanuvchi ism familiyasi")
    note = models.TextField(blank=True, null=True, verbose_name='Eslatma uchun')
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=OPTIONS, default='deactive')

    objects = models.Manager()
    manager = BlogDetailPageManager()


    def __str__(self):
        return self.name
    
    class Meta:
        # ordering = ['-date']
        db_table = 'Blog_Page'
        managed = True
        verbose_name = 'Blog post'
        verbose_name_plural = 'Blog post'
    

   
class CommentPage(models.Model):
    blog = models.ForeignKey(BlogDetailPage, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, verbose_name="Email")
    website = models.CharField(max_length=255, blank=True, null=True)
    comment =   models.TextField()
    image = models.ImageField(upload_to='comment-image/', default='comment-image/user.jpg')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Comment_Page'
        managed = True
        verbose_name = 'Izohlar'
        verbose_name_plural = 'Izohlar'