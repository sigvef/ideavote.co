import datetime
import math
import pytz

epoch = datetime.datetime(1970, 1, 1).replace(tzinfo=pytz.utc)


def epoch_seconds(date):
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)


def hot(idea, date):
    score = idea.upvoters.count()
    order = math.log(max(abs(score), 1), 10)
    sign = 1 if score > 0 else -1 if score < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(sign * order + seconds / 45000, 7)