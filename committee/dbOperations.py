from django.db import connections


class events:
    conn = ""

    def __init__(self):
        self.conn = connections['default']

    def getCreatedEvents(self, cmid):
        query = "select * from events where cmid_fk="+str(cmid)
        cursor=self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
