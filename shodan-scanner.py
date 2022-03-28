# api shodan
global SHODAN_API_KEY
SHODAN_API_KEY = "KP9p7Gq6NW7WNrYl444M2eIKlRMZOLvG"
# start import packages
import shodan

def search():

    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        # Search Shodan
        word = input("----------------------- \n Eter a word : ")
        print(("-----------------------"))
        results = api.search(word)

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                print('IP: {}'.format(result['ip_str']) , end="\n os : ")
                print(result['os'] , end="\n port : ")
                print(result['port'] , end="\n transport : ")
                print(result["transport"] , end="\n info : \n hostname : ")
                print(result["hostnames"] , end="\n location ~~~ \n ")
                location = result["location"]
                print("city : " , location['city'])
                print("country : " , location['country_name'])
                print("-----------------------")
    except shodan.APIError:
        print("""Error:
    There are several problems :
        Change api key in shodan-scanner.py 
         first go to shodan.io and login .
         in my account in AccountOverview Section
         copy api key and change api key in SHODAN_API_KEY

    cheke Internet . by {"ping google.com"}.

    """)

search()
