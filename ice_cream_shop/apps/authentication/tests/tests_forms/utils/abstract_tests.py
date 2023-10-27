from abc import ABC, abstractmethod


class AbstractCharFieldTest(ABC):
    @property
    @abstractmethod
    def form(self):
        pass

    @property
    @abstractmethod
    def field_name(self):
        pass

    @property
    @abstractmethod
    def placeholder(self):
        pass

    @property
    @abstractmethod
    def label(self):
        pass

    @property
    @abstractmethod
    def required(self):
        pass

    @property
    @abstractmethod
    def incorrect_values(self):
        pass

    def test_field_invalid(self):
        if not hasattr(self, 'form_data'):
            raise AssertionError('self.form_data is not defined. Please define it in the successor class.')
        form_data = self.form_data
        for value in self.incorrect_values:
            form_data[self.field_name] = value
            form = self.form(data=form_data)
            self.assertFalse(form.is_valid())

    def test_widget_attrs(self):
        form = self.form()
        first_name_widget = form.fields[self.field_name].widget
        self.assertEqual(first_name_widget.attrs['placeholder'], self.placeholder)

    def test_label(self):
        form = self.form()
        self.assertEqual(form.fields[self.field_name].label, self.label)

    def test_required(self):
        form = self.form()
        self.assertEqual(form.fields[self.field_name].required, self.required)