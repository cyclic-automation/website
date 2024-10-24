import re
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


class CorrectData:
    @staticmethod
    def init(val):
        val = str(val)
        val = val.lower()
        val = val.strip()
        return val

    def name(self, val):
        val = self.init(val)
        val = re.sub(r"\s+", " ", val)
        val = val.title()
        return val

    def id(self, val):
        val = self.init(val)
        val = re.sub(r"\s", "", val)
        return val

    def account_balance(self, val):
        val = self.init(val)
        val = re.sub(r"\s", "", val)
        val = re.sub(r"[$,]", "", val)
        if re.findall(r"k", val):
            val = re.sub(r"k", "", val)
            val = str(float(val) * 1e3)
        if re.findall(r"m", val):
            val = re.sub(r"m", "", val)
            val = str(float(val) * 1e6)
        val = str(round(float(val), 2))
        return val

    def phone(self, val):
        val = self.init(val)
        val = re.sub(r"\s", "", val)
        val = re.sub(r"[-.()]", "", val)
        return val

    def email(self, val):
        val = self.init(val)
        val = re.sub(r"\s", "", val)
        return val


class ValidateData:
    @staticmethod
    def name(val):
        val = CorrectData.init(val)
        if re.fullmatch(r"^[a-z\s]+$", val):
            return True
        return False

    @staticmethod
    def id(val):
        val = CorrectData.init(val)
        if re.fullmatch(r"^[\d]{4}$", val):
            return True
        return False

    @staticmethod
    def account_balance(val):
        val = CorrectData.init(val)
        if re.fullmatch(r"^\d+\.\d{0,2}$", val):
            return True
        return False

    @staticmethod
    def phone(val):
        val = CorrectData.init(val)
        if re.fullmatch(r"^[\d]{10}$", val):
            return True
        return False

    @staticmethod
    def email(val):
        val = CorrectData.init(val)
        if re.fullmatch(r"^[\w\.-]+@[\w\.-]+\.\w+$", val):
            return True
        return False


def process_df():
    contacts_df = pd.read_csv("data/contacts.csv")
    contacts_processed_df = pd.DataFrame(columns=contacts_df.columns.tolist())
    contacts_rejected_df = pd.DataFrame(columns=contacts_df.columns.tolist() + ['error'])
    contacts_columns = list(contacts_df.columns)

    for _, row in contacts_df.iterrows():
        row = row.to_dict()
        row_corrected = {
            'name': CorrectData().name(row['name']),
            'id': CorrectData().id(row['id']),
            'account_balance': CorrectData().account_balance(row['account_balance']),
            'phone': CorrectData().phone(row['phone']),
            'email': CorrectData().email(row['email']),
        }

        invalid_data_points = []
        if not ValidateData.name(row_corrected['name']):
            invalid_data_points.append('name')
        if not ValidateData.id(row_corrected['id']):
            invalid_data_points.append('id')
        if not ValidateData.account_balance(row_corrected['account_balance']):
            invalid_data_points.append('account_balance')
        if not ValidateData.phone(row_corrected['phone']):
            invalid_data_points.append('phone')
        if not ValidateData.email(row_corrected['email']):
            invalid_data_points.append('email')
        row['error'] = invalid_data_points

        is_valid = len(invalid_data_points) == 0

        if is_valid:
            contacts_processed_df = contacts_processed_df._append(pd.Series(row_corrected), ignore_index=True)
        else:
            contacts_rejected_df = contacts_rejected_df._append(pd.Series(row), ignore_index=True)

    # print(contacts_processed_df)
    # print(contacts_rejected_df)

    contacts_processed_df.to_csv("data/contacts_processed.csv", index=False)
    contacts_rejected_df.to_csv("data/contacts_rejected.csv", index=False)
