from datetime import datetime

#Insert the (year,month,day,hour,minute) separated by commas
end = datetime()
#Select the social media you want to block
social_media_block = ['www.facebook.com','facebook.com',
                       'www.instagram.com','instagram.com',
                       'www.twitter.com','twitter.com',
                       'www.youtube.com','youtube.com',
                       'www.tiktok.com','tiktok.com',
                       'www.kwai.com','kwai.com',
                       'www.pinterest.com','pinterest.com',
                       'www.snapchat.com','snapchat.com',
                       'www.tumblr.com','tumblr.com',
                       'www.reddit.com','reddit.com']

#Select the hosts path on your computer
hosts = '/etc/hosts'#for Linux and MacOS
#hosts = r"C:\Windows\System32\drivers\etc\hosts"#For Windows
redirect = '127.0.0.1'

def block_websites():
    if datetime.now() < end:
        print("All social media sites has been blocked.")
        with open(hosts, 'r+') as hostfile:
            hosts_content = hostfile.read()
            for site in  social_media_block:
                if site not in hosts_content:
                   hostfile.write(redirect + ' ' + site + '\n')
    else:
        print('All social media sites has been unblocked.')
        with open(hosts, 'r+') as hostfile:
            lines = hostfile.readlines()
            hostfile.seek(0)
            for line in lines:
                if not any(site in line for site in social_media_block):
                    hostfile.write(line)
            hostfile.truncate()

if __name__ == '__main__':
    block_websites()
