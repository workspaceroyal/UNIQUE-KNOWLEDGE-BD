from core.models import Product
from django import forms
# from bootstrap_datepicker_plus import DatePickerInput



class AddProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "বইয়ের নাম", "class":"form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "বিবরণ", "class":"form-control"}))
    price = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': "বিক্রয় মূল্য", "class":"form-control"}))
    old_price = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': "পূর্বের মূল্য", "class":"form-control"}))
    type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "বইয়ের প্রকার", "class":"form-control"}))
    stock_count = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': "কতটি স্টক করবেন?", "class":"form-control"}))
    life = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "কত দিন এটা সাইটে থাকবে?", "class":"form-control"}))
    mfd = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': "আপলোডের তারিখ", "class":"form-control"}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "ট্যাগ", "class":"form-control"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"}))

    class Meta:
        model = Product
        fields = [
            'title',
            'image',
            'description',
            'price',
            'old_price',
            'specifications',
            'type',
            'stock_count',
            'life',
            'mfd',
            'tags',
            'digital',
            'category',
        ]

        widgets = {
        # 'mdf': DateTimePickerInput
    }