
class FileNode:
    def __init__(self, name, parent=None, data=""):
        self.name = name
        self.parent = parent
        self.children = []
        self.data = data
        if parent:
            parent.children.append(self)

    def __str__(self):
        # I recommend ignoring this method
        bytestring = f"  ({len(self.data)} bytes)" if len(self.data) else ""
        childrenstring = (
            f"  (contains {len(self.children)} files)" if len(self.children) else ""
        )

        return f"{self.name}{bytestring}{childrenstring}"

    def __repr__(self):
        # I recommend ignoring this method
        return f"<solution.FileNode object at {id(self)} (name='{self.name}')>"
    
    # Q1
    def fullpath(self):
        pass

    # Q2
    def count_normal_files(self):
        pass

    # Q3
    def find_by_localpart(self, target_name):
        return []

    # Q4
    def format_tree_string(self, sort=False):
        return []
    
    # Q5
    def closest_common_ancestor(self, other_node):
        pass

