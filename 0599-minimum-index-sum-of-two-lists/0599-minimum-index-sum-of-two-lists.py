class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        HashMap = {}
        G_Map = {}
        min_indices = 2147483647
        res = []
        
        for i, string in enumerate(list1):  # Save every String in List1 in HashMap
            HashMap[string] = i             # Set index as value

        for j, string in enumerate(list2):
            if string in HashMap:           # Add the second to HashMap
                G_Map[string] = j + HashMap[string]      # Add the indices

        
        for string in G_Map:                # Go trough the HashMap
            if min_indices > G_Map[string]: # Find min value
                min_indices = G_Map[string]
        
        for string in G_Map:                # Return all Strings with min value
            if G_Map[string] == min_indices:
                res.append(string)
        
        return res                          # Return all strings with min value