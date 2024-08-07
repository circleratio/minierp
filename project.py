import sys
import common
from logging import getLogger

class Project:
    def __init__(self):
        self.db = common.DB().db
        self.logger = getLogger(__name__)

    def dump(self):
        for row in self.db.get('project'):
            print(row)

    def set(self, data):
        where = {'name': data['name'], 'fiscal_year': data['fiscal_year']}
        item = self.get(where)
        if item == None:
            self.logger.debug('set: new data')
            self.db.set('project', data)
            self.db.commit()
        else:
            self.logger.debug('set: the project already exists: {} (id={})'.format(data['name'], item['id']))
            self.db.set('project', data, dataid=item['id'])
            self.db.commit()

    def get(self, where):
        for row in self.db.get('project', where):
            return(row)
        return(None)
    
def main():
    db = Project()
    db.dump()
    
if __name__ == '__main__':
    sys.exit(main())
