#utilities funtion

class LinkNode(object):
    def __init__(self, node_id):
        self.node_id = node_id
        self.path = [] #parent urls

def get_all_my_parents(node_id, session):
    parent_list = []
    for every_parent in session.query(Link).filter(Link.to_page_id==node_id,Link.number_of_separation==1):
        parent_node = Node(every_parent.from_page_id)
        parent_list.append(parent_node)
    return parent_list

def get_parent_id_list(parent_list):
    return [parent_node.node_id for parent_node in parent_list]

def get_url_path_from_page_ids(session, page_ids_list):
    path_url = []
    for page_id in page_ids_list:
        page_url = session.query(Page).filter(Page.id == page_id).first()
        path_url.append(page_url.url)
    path_url.reverse()
    return path_url
