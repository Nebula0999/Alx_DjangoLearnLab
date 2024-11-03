book.delete()

# Confirm deletion by trying to retrieve all books
Book.objects.all()

output = <QuerySet []>