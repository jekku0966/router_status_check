import requests
from bs4 import BeautifulSoup


def RouterCheck(url):
    data_pwr = []
    data_snr = []
    data_up = []
    i = 0
    j = 0
    soup = BeautifulSoup(url.content, 'html5lib')
    table = soup.find('table', {'summary': 'Downstream Channels'})
    cols_pwr = table.findAll('td', {'headers': 'ch_pwr'})
    cols_snr = table.findAll('td', {'headers': 'ch_snr'})

    table = soup.find('table', {'summary': 'Upstream Channels'})
    cols_up_pwr = table.findAll('td', {'headers': 'up_pwr'})

    for power in cols_pwr:
        data_pwr.append(power.text[1:-11])
    for snr in cols_snr:
        data_snr.append(snr.text[:-9])
    for up_pwr in cols_up_pwr:
        data_up.append(up_pwr.text[:-11])
    for pwr, snr in zip(data_pwr, data_snr):
        i += 1
        print('Channel ' + str(i) + ': ' +
              str(pwr) + 'dBmV, ' + str(snr) + 'dB')
    print('')
    print('Upstream Channel data:')
    for up_data in data_up:
        j += 1
        print('Channel ' + str(j) + ': ' + str(up_data) + 'dB')


url = requests.get('http://192.168.100.1/Docsis_system.asp')
if __name__ == '__main__':
    if bridged.status_code != 200:
        RouterCheck(url)
    else:
        url = requests.get('http://192.168.0.1/Docsis_system.asp')
        RouterCheck(url)
