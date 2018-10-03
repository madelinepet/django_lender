from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
# receiver is a decorator


class Book(models.Model):
    STATES = [
        ('available', 'Available'),
        ('checked-out', 'Checked-Out'),
    ]
    YEARS = [
        ('2018', '2018'),
        ('2017', '2017'),
        ('2016', '2016'),
        ('2015', '2015'),
        ('2014', '2014'),
        ('2013', '2013'),
        ('2012', '2012'),
        ('2011', '2011'),
        ('2010', '2010'),
        ('2009', '2009'),
        ('2008', '2008'),
        ('2007', '2007'),
        ('2006', '2006'),
        ('2005', '2005'),
        ('2004', '2004'),
        ('2003', '2003'),
        ('2002', '2002'),
        ('2001', '2001'),
        ('2000', '2000'),
        ('1999', '1999'),
        ('1998', '1998'),
        ('1997', '1997'),
        ('1996', '1996'),
        ('1995', '1995'),
        ('1994', '1994'),
        ('1993', '1993'),
        ('1992', '1992'),
        ('1991', '1991'),
        ('1990', '1990'),
        ('1989', '1989'),
        ('1988', '1988'),
        ('1987', '1987'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    # cover_image = models.FileField(upload_to='uploads/')
    # cover_image = models.ImageField(upload_to=user_directory_path)
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=48)
    year = models.CharField(choices=YEARS, default='2018', max_length=48)
    status = models.CharField(choices=STATES, default='available', max_length=48)
    date_added = models.DateTimeField(auto_now_add=True)
    # Blank allows the field to be able to be left blank. arg has to be there,
    # but can be empty string
    last_borrowed = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Book: {self.title} ({self.status}) | Author: {self.author} | Year: {self.year} | Date_added: {self.date_added} | Last_borrowed: {self.last_borrowed}'

    def __repr__(self):
        return f'Book: {self.title} ({self.status}) | Author: {self.author} | Year: {self.year} | Date_added: {self.date_added} | Last_borrowed: {self.last_borrowed}'


# listens for a post-save signal on the model, sender is the Book class
@receiver(models.signals.post_save, sender=Book)
def set_book_checked_out_date(sender, instance, **kwargs):
    if instance.status == 'Checked-Out'and not instance.last_borrowed:
        instance.last_borrowed = timezone.now
        instance.save()
