__author__ = "LACCI"

import urllib.request
import sys
import re


def main():
    wallet_id = 'Ezt nem tenném fel publikus repo-ba.'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en_US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = f'https://ethermine.org/miners/{wallet_id}}/dashboard'
    headers={'User-Agent':user_agent,}
    
    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    
    formatted_response = '\n'.join([line.decode('utf-8') for line in response])
    #sys.stdout.write(formatted_response)
    
    eth_line = re.search(r'<span data-v-46ce483c="" data-v-4060aaaf="" class="current-balance" data-v-0ef704b5="">'
    '(\d+)\.(\d+)', formatted_response)
    #if eth_line:
    sys.stdout.write(eth_line.group(1) + '.' + eth_line.group(2) + ' ETH')

main()