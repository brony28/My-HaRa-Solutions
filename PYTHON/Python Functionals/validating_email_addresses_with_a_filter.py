#VALIDATING EMAIL ADDRESSES WITH A FILTER

def fun(s):
    # return True if s is a valid email, else return False
    if "@" and "." in s:
        try:
            at = s.index('@')
            do = s.index('.')
            usern = s[:at]
            web = s[at+1:do]
            ext = s[do+1:]
        except ValueError:
            return False
    
        if web.isalnum() and len(ext)<=3 and usern.replace('_','').replace('-','').isalnum():
            return True
        else:
            return False
    else:
        return False



def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)