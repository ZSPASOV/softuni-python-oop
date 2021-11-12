class EmailValidator:
    def __init__(self, min_length, mails,  domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains
    def __validate_name(self, name):
        return len(name) >= self.min_length
    def __validate_mail(self, mail):
        return mail in self.mails
    def __validate_domain(self, domain):
        return domain in self.domains
    def validate(self, email):
        # TODO: Implement
