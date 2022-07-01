import requests
from uuid import uuid4

counters=1

def login():
        global counters , get_sessionid , get_csrftoken
        vote_user = input("""


If You Want Right Vote Choose 1
If You Want Left Vote Choose  0


Choose vote please: """)
        target = input("Enter your target: ")
        for account in accounts:
                username = account.split(':')[0]
                password = account.split(':')[1]

                url_login = "https://i.instagram.com/api/v1/accounts/login/"
                header_login = {

                        'X-Pigeon-Session-Id': str(uuid4()),
                        'X-IG-Device-ID': str(uuid4()),
                        'User-Agent': 'Instagram 159.0.0.40.122 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 245196089)',
                        'X-IG-Connection-Type': 'WIFI',
                        'X-IG-Capabilities': '3brTvx8=',
                        "Connection" : 'keep-alive',
                        "Accept-Language": "en-US",
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        "Accept-Encoding": "gzip, deflate",
                        'Host': 'i.instagram.com',
                        'Cookie': 'mid=YqejMwABAAExc4QmMCMsnq5YVuEw; csrftoken=BE0qlaD88tnB3vjkLhGksva9WFE2LPYB'
                        }

                data_login = {
                        'username': username,
                        'enc_password': f"#PWD_INSTAGRAM:0:&:{password}",
                        "adid": uuid4(),
                        "guid": uuid4(),
                        "device_id": uuid4(),
                        "phone_id": uuid4(),
                        "google_tokens": "[]",
                        'login_attempt_count': '0'
                        }

                req_login = requests.post(url=url_login,headers=header_login,data=data_login)

                if 'logged_in_user' in req_login.text:
                        get_sessionid = req_login.cookies.get("sessionid")
                        get_csrftoken =req_login.cookies.get("csrftoken")
                
                        print(f"\n{counters}. {username} Logged in √")
                        counters+=1
                else:
                        print(f"\n{counters}. {username} Error in X")
                        counters+=1
                        with open("Bad_accounts.txt",'a') as file:
                                file.write(f"{counters}. {username} {password}")
                        pass      
        
                url_userid = f'https://i.instagram.com/api/v1/fbsearch/topsearch_flat/?search_surface=top_search_page&timezone_offset=10800&count=30&query={target}'
                header_userid = {
                        'Host': 'i.instagram.com',
                        'Cookie': f'csrftoken={get_csrftoken}; sessionid={get_sessionid}',
                        'X-Ig-Www-Claim':'hmac.AR2OyTfT1R295O4lDaLa3KWTfnnUlpGCei-EHkXl3J6WD6aA',
                        'X-Ig-Connection-Type': 'WIFI',
                        'X-Ig-Capabilities': '3brTvx8=',
                        'User-Agent': 'Instagram 159.0.0.40.122 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 245196089)',
                        'Accept-Language': 'en-US',
                        'Accept-Encoding': 'gzip, deflate'
                        }
                req_userid = requests.get(url=url_userid,headers=header_userid).json()
                get_userid_him = req_userid['list'][0]["user"]["pk"]

                url_story = f"https://www.instagram.com/api/v1/feed/user/{get_userid_him}/story/"

                header_story = {

                        'X-Pigeon-Session-Id': str(uuid4()),
                        'X-IG-Device-ID': str(uuid4()),
                        'User-Agent': 'Instagram 159.0.0.40.122 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 245196089)',
                        'X-IG-Connection-Type': 'WIFI',
                        'X-IG-Capabilities': '3brTvx8=',
                        "Connection" : 'keep-alive',
                        "Accept-Language": "en-US",
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        "Accept-Encoding": "gzip, deflate",
                        'Host': 'i.instagram.com',
                        'Cookie': f'mid=YqejMwABAAExc4QmMCMsnq5YVuEw; csrftoken={get_csrftoken}; sessionid={get_sessionid}'
                        }

                req_story = requests.get(url=url_story,headers=header_story)
                media_ids = req_story.json()['reel']['media_ids'][0]
                poll_id = req_story.json()['reel']['items'][0]['story_polls'][0]['poll_sticker']['poll_id']    

                url_vote = f'https://www.instagram.com/api/v1/media/{media_ids}/{poll_id}/story_poll_vote/'

                header_vote = {

                        'X-Pigeon-Session-Id': str(uuid4()),
                        'X-IG-Device-ID': str(uuid4()),
                        'User-Agent': 'Instagram 159.0.0.40.122 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 245196089)',
                        'X-IG-Connection-Type': 'WIFI',
                        'X-IG-Capabilities': '3brTvx8=',
                        "Connection" : 'keep-alive',
                        "Accept-Language": "en-US",
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        "Accept-Encoding": "gzip, deflate",
                        'Host': 'i.instagram.com',
                        'Cookie': f'mid=YqejMwABAAExc4QmMCMsnq5YVuEw; csrftoken={get_csrftoken}; sessionid={get_sessionid}'
                        }
                data_vote = {

                'vote': vote_user
                }
                req_vote = requests.post(url_vote,headers=header_vote,data=data_vote).text

                if '"status":"ok"' in req_vote:
                        print( "\n[+] Done Voted" )
                else:
                        print("\n[-] Bad Voted")

        input("\n\nFinished Voted")     

if __name__ == '__main__':
        try:
                file = input("[+] Enter Your File Name: ")
                with open(file,'r') as account:
                        accounts = account.read().splitlines()
        except:
                input(f'Not Found {file}')
        login()