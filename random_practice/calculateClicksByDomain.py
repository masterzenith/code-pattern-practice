counts = [
    "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "5,com.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,mobile.sports",
    "1,google.co.uk"
]
import collections


def calculateClicksByDomain(counts):
    ans = collections.Counter()
    for domain in counts:
        count, domain = domain.split(',')
        count = int(count)
        frags = domain.split('.')
        for i in range(len(frags)):
            ans[".".join(frags[i:])] += count
    return ["{} {}".format(ct, dom) for dom, ct in ans.items()]


print(calculateClicksByDomain(counts))
