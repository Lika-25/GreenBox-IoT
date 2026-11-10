from django import forms

class MongoSecurityForm(forms.Form):
    name = forms.CharField(label="Назва загрози", widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(label="Категорія", choices=[
        ('network_attack', 'Мережеві атаки'),
        ('data_integrity', 'Цілісність даних'),
        ('unauthorized_access', 'Несанкціонований доступ'),
        ('physical_tampering', 'Фізичне втручання'),
    ], widget=forms.Select(attrs={'class': 'form-select'}))
    severity = forms.ChoiceField(label="Рівень", choices=[
        ('low', 'Низький'), ('medium', 'Середній'), 
        ('high', 'Високий'), ('critical', 'Критичний')
    ], widget=forms.Select(attrs={'class': 'form-select'}))
    vector = forms.CharField(label="Вектор атаки / Опис", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    target_node = forms.CharField(label="Цільовий вузол", widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(label="Статус", choices=[
        ('active', 'Активна'), ('neutralized', 'Нейтралізована')
    ], widget=forms.Select(attrs={'class': 'form-select'}))
