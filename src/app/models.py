from app import db

class AFWMailHistory(db.Model):
    __tablename__ = 'AFW_MAIL_HISTORY'
    
    mahi_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    mahi_receiver = db.Column(db.String(2000), nullable=False)
    mahi_subject = db.Column(db.String(255), nullable=False)
    mahi_body = db.Column(db.Text, nullable=False)
    mahi_status = db.Column(db.Integer, nullable=False)
    mahi_sender = db.Column(db.String(255), nullable=False)
    mahi_sender_name = db.Column(db.String(255), nullable=False)
    mahi_format = db.Column(db.Integer, nullable=False)
    mahi_category = db.Column(db.String(100), nullable=False)
    mahi_server = db.Column(db.String(255), nullable=False)
    mahi_port = db.Column(db.Integer, nullable=False)
    mahi_user_account = db.Column(db.String(255), nullable=True)
    mahi_user_password = db.Column(db.String(255), nullable=True)
    mahi_created = db.Column(db.DateTime, nullable=False)
    mahi_ssl = db.Column(db.Integer, nullable=False)
    mahi_modified_date = db.Column(db.DateTime, nullable=True)
    mahi_headers = db.Column(db.Text, nullable=True)
    mahi_message = db.Column(db.Text, nullable=True)
    data = db.Column(db.Text, nullable=True)
    type = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<AFWMailHistory {self.mahi_id}>'