import xml.etree.ElementTree as ET

# XML Class
# Loads the inital file and stores it in a variable
# Saves the edited file
class XML():
    def __init__(self, file):
        self.file = file
        self.ref = ET.parse(file) #auto loads the file
    
    # Saves the file
    def save(self, path):
        try: 
            self.ref.write(path)
        except Exception as e:
            return e
        

# Permissions Class
# Represents indivual permissions in the XML file
# Can be used to add, view, check and remove permissions in the file
class Permissions():
    def __init__(self, ref):
        self.ref = ref
    
    # Iterates through the file and returns a list of members with the given permission name.
    # If no permission ID does not match the name, it returns False
    def retrieveMembers(self, name):
        for permission in self.ref.ref.getroot().iter('Group'):
            if (permission.find('Id').text.lower() == name.lower()):
                return permission.find('Members')
        return False
    
    # Returns True if given steamid is in the given permission group
    def checkPermission(self, permission, steamid):
        members = self.retrieveMembers(permission)
        if (members == False):
            return False
        for member in members:
            if (member.text == steamid):
                return True
        return False
    
    # Retrieves all the permissions of a given steamid
    def retrievePermissions(self, steamid):
        perms = []
        for permission in self.ref.ref.getroot().iter('Group'):
            if (self.checkPermission(permission.find('Id').text, steamid)):
                perms.append(permission.find('Id').text)
        return perms
    
    # Adds steamid to a given permission group
    # If the permission group does not exist, it returns False
    # Else returns True
    def addPermission(self, permission, steamid):
        # Check if steamid is already in the group
        members = self.retrieveMembers(permission)
        if (members == False):
            return False
        if (self.checkPermission(permission, steamid)):
            return False
        ET.SubElement(members, 'Member').text = steamid
        self.ref.save(self.ref.file)
        return True
    
    # Removes steamid from a give permission group
    # If the user if not in the permssion group, returns False
    # If the group does not exist, returns False
    # Else returns True
    def removePermission(self, permission, steamid):
        members = self.retrieveMembers(permission)
        if (members == False):
            return False
        if (self.checkPermission(permission, steamid) == False):
            return False
        for member in members:
            if (member.text.lower() == steamid.lower()):
                members.remove(member)
                self.ref.save(self.ref.file)
                return True
