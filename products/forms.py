from django import forms

from .models import Review, Product, Category


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
           'product_id',
'review_title',
'review_content',
'review_date_posted',
'review_author'
        )


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'