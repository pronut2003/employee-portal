from mongoengine import Document, StringField,IntField,DateField, LongField, EmailField


class Employee(Document):
    ID = IntField(primary_key=True)

    NAME = StringField(required=True, max_length=100)
    GENDER = StringField(required=True, choices=["MALE", "FEMALE", "OTHER"])

    DOB = DateField(required=True)
    DOJ = DateField(required=True)

    DEPARTMENT = StringField(required=True, max_length=50)
    DESIGNATION = StringField(required=True, max_length=50)

    SALARY = LongField(required=True, min_value=0)

    PHONE = StringField(required=True, max_length=15)
    EMAIL = EmailField(required=True, unique=True)

    def __str__(self):
        return f"{self.ID} - {self.NAME} - {self.GENDER} - {self.DOB} - {self.DOJ}"

class Promotion(Document):
    ID = IntField(primary_key=True)
    NAME = StringField(required=True, max_length=100)
    CURR_DESIGNATION = StringField(required=True, max_length=50)
    CURR_SALARY = LongField(required=True, min_value=0)
    ELIGIBLE_PROMOTION = StringField(required=True, max_length=50)

    def __str__(self):
        return f"{self.ID} - {self.NAME} - {self.CURR_DESIGNATION} - {self.CURR_SALARY} - {self.ELIGIBLE_PROMOTION}"