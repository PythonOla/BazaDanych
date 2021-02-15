from ...Model.InOut.Input import Input
from ...View.NameFinder.NameFinder import NameFinder
from ...View.Finder.finder import IdFinder
 

class User_search_controller:
    def __init__(self, *args):
        self.data = Input().user_list
        self.args = args

    def id_search(self, id):
        found = self.data.find_users_by_id(str(id))
        return self._parse_found(found)

    def _parse_found(self, found):
        if len(found) == 0:
            return {
                'id': None
            }
        else:
            return {
                'id': found[0].id,
                'name_and_surname': found[0].name + " " + found[0].surname
            }


    def fuzzy_search(self, txt):
        found = self.data.search_by_name(txt)
        return self._parse_found(found)

    def show_name_search(self, on_search, on_back):
        return NameFinder(on_search, on_back, self.fuzzy_search)

    def show_id_search(self, on_search, on_back):
        return IdFinder(on_search, on_back, self.id_search)
    