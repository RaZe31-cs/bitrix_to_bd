from fast_bitrix24 import Bitrix
import json
from data.database.db_session import create_session, global_init
from data.config import webhook
import logging


def connect_to_db():
    try:
        global_init('db_for_bitrix')
        logging.info('Connect goodness')
        return True
    except Exception as e:
        logging.error(e)
        logging.info('Connect badness')
        return False


bx = Bitrix(webhook)
cite_count = 0
cite_count_deals = 0
cite_count_good = 0
cite_count_not_called = 0
other_count = 0
other_count_deals = 0
other_count_good = 0
other_count_not_called = 0
data = bx.get_all('crm.lead.list', {'filter': {'STATUS_ID': 'ASSIGNED'}})
for i in data:
    if i['SOURCE_DESCRIPTION'] != None:
        if i['SOURCE_DESCRIPTION'].find('сайт') != -1 or i['SOURCE_DESCRIPTION'].find('форма') != -1:
            cite_count += 1
            if 'недозвон' in i['COMMENTS'] or 'автоответ' in i['COMMENTS'] or 'гудок' in i['COMMENTS']:
                cite_count_not_called += 1
            else:
                deals = bx.get_all('crm.deal.list', {'filter': {'ASSIGNED_BY_ID': i['ASSIGNED_BY_ID']}})
                for j in deals:
                    cite_count_deals += 1

        elif i['SOURCE_DESCRIPTION'].find('номер') != -1:
            other_count += 1
            if 'недозвон' in i['COMMENTS'] or 'автоответ' in i['COMMENTS'] or 'гудок' in i['COMMENTS']:
                other_count_not_called += 1
            else:
                deals = bx.get_all('crm.deal.list', {'filter': {'ASSIGNED_BY_ID': i['ASSIGNED_BY_ID']}})
                for j in deals:
                    other_count_deals += 1
        else:
            print(i['SOURCE_DESCRIPTION'])
cite_count_good = cite_count - cite_count_not_called
other_count_good = other_count - other_count_not_called
print(cite_count, cite_count_deals, cite_count_not_called, cite_count_good, other_count, other_count_deals,
      other_count_not_called, other_count_good)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s;%(levelname)s;%(message)s', level=logging.INFO,
                        filename='root/log/app2.log', filemode='w')
    logging.info('start')
